import re
from flask import Flask, request, redirect, render_template
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
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

#API Part 
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


#UI Part
@app.route('/ui')
def get_site():
    return render_template("index.html")

@app.route('/ui/get', methods=["POST", "GET"])
def ui_get():
    return render_template("get.html")

@app.route('/ui/get/id', methods=["POST", "GET"])
def ui_get_book():
    if request.method == "POST":
        id = request.form["id"]
        book = Book.query.get_or_404(id)
        return {"title" : book.title, "author": book.author}
    else:
        return render_template("get_id.html")

@app.route('/ui/get/last', methods=["POST", "GET"])
def ui_get_last_books():
    if request.method == "POST":
        n = request.form["n"]
        books = Book.query.limit(n)
        output = []
        for book in books:
            book_data = {"title" : book.title, "author": book.author}
            output.append(book_data)
        return {"books": output}
    else:
        return render_template("get_last.html")

@app.route('/ui/post', methods=["POST", "GET"])
def ui_post():
    if request.method == "POST":
        book = Book(title=request.form["title"], author=request.form["author"])
        db.session.add(book)
        db.session.commit()
        return {"id": book.id}
    else:
        return render_template("post.html")

@app.route('/ui/put', methods=["POST", "GET"])
def ui_put():
    if request.method == "POST":
        id = request.form["id"]
        book = Book.query.filter_by(id=id).first()
        book.title = request.form["title"]
        book.author = request.form["author"]
        db.session.commit()
        book_data = {"title" : book.title, "author": book.author}
        return {"updated book" : book_data}
    else:
        return render_template("put.html")

@app.route('/ui/delete', methods=["POST", "GET"])
def ui_delete():
    if request.method == "POST":
        id = request.form["id"]
        book = Book.query.get_or_404(id)
        book_data = {"title" : book.title, "author": book.author}
        db.session.delete(book)
        db.session.commit()
        return {"deleted book" : book_data}
    else:
        return render_template("delete.html")

if __name__ == "__main__":
    app.run()