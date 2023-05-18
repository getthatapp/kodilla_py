from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api, abort
from flask_bootstrap import Bootstrap
from faker import Faker

app = Flask(__name__)
api = Api(app)
bootstrap = Bootstrap(app)

faker = Faker()

books = [{
    'id': i,
    "author": faker.name(),
    'title': faker.catch_phrase(),
    'description': faker.text(),
    'cover': faker.image_url(),
} for i in range(10)]


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Nie odnaleziono strony'}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Niepoprawne zapytanie'}), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': "Błąd serwera"}), 500


@app.route('/books')
def book_view():
    return render_template('books.html', books=books)


@app.route('/book/<int:id>')
def single_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is not None:
        return render_template('book.html', book=book)
    else:
        return {'error': "Nie odnaleziono książki"}, 404


class BookListAPI(Resource):
    def get(self):
        return {'books': books}, 200

    def post(self):
        if not request.json or not 'title' in request.json or not 'author' in request.json:
            abort(400)
        book = {
            'id': books[-1]['id'] + 1 if books else 0,
            'title': request.json['title'],
            'author': request.json['author'],
            'description': request.json.get('description', ""),
            'cover': request.json.get('cover', "")
        }
        books.append(book)
        return book, 201


class BookAPI(Resource):
    def find_book(self, id):
        for book in books:
            if book['id'] == id:
                return book
        return None

    def get(self, id):
        book = next((book for book in books if book['id'] == id), None)
        if book is not None:
            return book, 200
        else:
            return {'error': "Nie odnaleziono książki"}, 404

    def put(self, id):
        data = request.get_json()
        book = self.find_book(id)
        if book:
            book.update(data)
            return book
        else:
            return {'error': "Nie odnaleziono książki"}, 404

    def delete(self, id):
        global books
        books = [book for book in books if book['id'] != id]
        return {'result': "Książka usunięta"}


api.add_resource(BookListAPI, '/api/books/')
api.add_resource(BookAPI, '/api/books/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
