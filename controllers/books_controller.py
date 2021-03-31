from flask import Flask, render_template, redirect, request
from repositories import book_repository
from repositories import author_repository
from models.book import Book
from models.author import Author

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('/books/index.html', all_books = books)


@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route('/books/new')
def new():
    return render_template('/books/new.html')


@books_blueprint.route('/books', methods = ["POST"])
def create():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author_first_name = request.form["first_name"]
    author_last_name = request.form["last_name"]
    author = Author(author_first_name, author_last_name)
    book = Book(title, genre, publisher, author)
    author_repository.save(author)
    book_repository.save(book)
    return redirect('/books')
    
@books_blueprint.route('/books/<id>', methods = ['GET'])
def show(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)

@books_blueprint.route('/books/<id>/edit', methods = ['GET'])
def edit(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)

@books_blueprint.route('/books/<id>', methods = ['POST'])
def update_book(id):
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author_first_name = request.form["first_name"]
    author_last_name = request.form["last_name"]
    author = Author(author_first_name, author_last_name, id)
    book = Book(title, genre, publisher, author, id)
    author_repository.update(author)
    book_repository.update(book)
    return redirect('/books')

