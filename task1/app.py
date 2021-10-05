from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    author = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(128))
    pages = db.Column(db.Integer)
    price = db.Column(db.Integer)

@app.route('/')
def index():
    return 'Make GET request to "/books" to get all of the books'

@app.route('/books', methods=["GET"])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {"title" : book.title, "author": book.author}
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>', methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"title" : book.title, "author": book.author}

@app.route('/books/last/<n>', methods=["GET"])
def get_last_books(n):
    books = Book.query.limit(n)
    output = []
    for book in books:
        book_data = {"title" : book.title, "author": book.author}
        output.append(book_data)
    return {"books": output}

@app.route('/books', methods=["POST"])
def add_book():
    book = Book(title=request.json["title"], author=request.json["author"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route('/books/<id>', methods=["PUT"])
def update_book(id):
    book = Book.query.filter_by(id=id).first()
    book.title = request.json["title"]
    book.author = request.json["author"]
    db.session.commit()
    book_data = {"title" : book.title, "author": book.author}
    return {"updated book" : book_data}

@app.route('/books/<id>', methods=["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    book_data = {"title" : book.title, "author": book.author}
    db.session.delete(book)
    db.session.commit()
    return {"deleted book" : book_data}

if __name__ == "__main__":
    app.run()