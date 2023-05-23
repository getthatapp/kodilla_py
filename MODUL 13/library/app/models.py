from .database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    release_date = db.Column(db.Date, nullable=False)
    is_loaned = db.Column(db.Boolean, nullable=False)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)

    books = db.relationship('Book', backref='author', lazy=True)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)

    book = db.relationship('Book', backref='loan', uselist=False)