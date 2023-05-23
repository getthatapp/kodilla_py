from faker import Faker
from .database import db
from .models import Author, Book, Loan

fake = Faker()


def generate_authors(n):
    for _ in range(n):
        author = Author(name=fake.name())
        db.session.add(author)
    db.session.commit()


def generate_books(n):
    authors = Author.query.all()
    for _ in range(n):
        book = Book(title=fake.catch_phrase(), description=fake.text(), isbn=fake.isbn13(),
                    release_date=fake.date_between('-10y', 'today'), is_loaned=False,
                    author_id=fake.random_element(authors).id)
        db.session.add(book)
    db.session.commit()


def generate_loans(n):
    books = Book.query.filter_by(is_loaned=False).all()
    for _ in range(n):
        if not books:
            break
        book = fake.random_element(books)
        books.remove(book)
        loan = Loan(book_id=book.id, loan_date=fake.date_this_year())
        book.is_loaned = True
        db.session.add(loan)
    db.session.commit()


def generate_data(authors=10, books=50, loans=20):
    generate_authors(authors)
    generate_books(books)
    generate_loans(loans)
