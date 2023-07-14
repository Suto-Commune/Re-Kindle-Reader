from flask import Blueprint
from flask import render_template as template
import src.book as book

page = Blueprint("bookshelf", __name__, template_folder=".\\files")


@page.route("/")
def bookshelf():
    book_info = book.get_book_shelf()
    return template("index.html", book_info=book_info)
