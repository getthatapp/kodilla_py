from flask import Blueprint, request, jsonify
from .database import db
from .models import Author, Book, Loan

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@main.route('/books', methods=['GET', 'POST'])
def books():
    books = Book.query.all()
    return jsonify([{
        'id': b.id,
        'author': b.author.name,
        'title': b.title,
        'description': b.description,
        'isbn': b.isbn,
        'is_loaned': b.is_loaned,
    } for b in books])


@main.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'author': book.author.name,
        'title': book.title,
        'description': book.description,
        'isbn': book.isbn,
        'is_loaned': book.is_loaned
    })


@main.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data['title']
    book.description = data.get('description', book.description)
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200


@main.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
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