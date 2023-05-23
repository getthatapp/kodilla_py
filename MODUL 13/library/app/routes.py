from flask import Blueprint, request, jsonify
from . import db
from .models import Author, Book, Loan

main = Blueprint('main', __name__)


@main.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = Book.query.all()
        return jsonify([{'title': b.title, 'description': b.description} for b in books])
    else:
        data = request.get_json()
        new_book = Book(title=data['title'], description=data.get('description', ''),
                        author_id=data['author_id'], isbn=data['isbn'],
                        release_date=data['release_date'], is_loaned=data['is_loaned'])
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
        return jsonify([f'{l.book.title} - {l.loan.date}' for l in loans])
    else:
        data = request.get_json()
        new_loan = Loan(book_id=data['book_id'])
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({'message': 'Book loaned successfully'}), 201

@main.route('/loans/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def loan(id):
    loan = Loan.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date})
    elif request.method == 'PUT':
        data = request.get_json()
        loan.return_date = data['return_date']
        db.session.commit()
        return jsonify({'message': "Loan updated successfully"}), 200
    else:
        db.session.delete(loan)
        db.session.commit()
        return jsonify({'message': 'Book returned successfully'}), 200
