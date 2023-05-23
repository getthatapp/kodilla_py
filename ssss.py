# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import *
from data import generate_data

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/myapp.db'

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        generate_data()

    return app

# app/models.py
from . import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    release_date = db.Column(db.Date, nullable=False)
    is_loaned = db.Column(db.Boolean, default=False)

    author = db.relationship('Author', backref='books', lazy=True)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)

    book = db.relationship('Book', backref='loan', uselist=False)


# app/routes.py
from flask import Blueprint, request, jsonify
from myapp import db
from myapp.models.author import Author
from myapp.models.book import Book
from myapp.models.loan import Loan

main = Blueprint('main', __name__)

@main.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = Book.query.all()
        return jsonify([{'title': b.title, 'description': b.description} for b in books])
    else:
        data = request.get_json()
        new_book = Book(title=data['title'], description=data.get('description', ''))
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201

@main.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'title': book.title, 'description': book.description})
    elif request.method == 'PUT':
        data = request.get_json()
        book.title = data['title']
        book.description = data.get('description', book.description)
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200

@main.route('/authors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def author(id):
    author = Author.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'name': author.name})
    elif request.method == 'PUT':
        data = request.get_json()
        author.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Author updated successfully'}), 200
    else:
        db.session.delete(author)
        db.session.commit()
        return jsonify({'message': 'Author deleted successfully'}), 200

@main.route('/loans', methods=['GET', 'POST'])
def loans():
    if request.method == 'GET':
        loans = Loan.query.all()
        return jsonify([f"{l.book.title} - {l.loan_date}" for l in loans])
    else:
        data = request.get_json()
        new_loan = Loan(book_id=data['book_id'])
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({'message': 'Loan added successfully'}), 201

@main.route('/loans/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def loan(id):
    loan = Loan.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date})
    elif request.method == 'PUT':
        data = request.get_json()
        loan.return_date = data['return_date']
        db.session.commit()
        return jsonify({'message': 'Loan updated successfully'}), 200
    else:
        db.session.delete(loan)
        db.session.commit()
        return jsonify({'message': 'Loan deleted successfully'}), 200


# app/data.py

from faker import Faker
from myapp import db
from myapp.models.author import Author
from myapp.models.book import Book
from myapp.models.loan import Loan

fake = Faker()

def generate_authors(n):
    for _ in range(n):
        author = Author(name=fake.name())
        db.session.add(author)
    db.session.commit()

def generate_books(n):
    authors = Author.query.all()
    for _ in range(n):
        book = Book(title=fake.catch_phrase(), description=fake.text(), isbn=fake.isbn13(), release_date=fake.date_between('-10y', 'today'), borrowed=False)
        book.authors = fake.random_elements(authors, length=fake.random_int(min=1, max=3))
        db.session.add(book)
    db.session.commit()

def generate_loans(n):
    books = Book.query.all()
    for _ in range(n):
        book = fake.random_element(books)
        if not book.borrowed:
            loan = Loan(book_id=book.id, loan_date=fake.date_this_year())
            book.borrowed = True
            db.session.add(loan)
    db.session.commit()

def generate_data(authors=10, books=50, loans=20):
    generate_authors(authors)
    generate_books(books)
    generate_loans(loans)
