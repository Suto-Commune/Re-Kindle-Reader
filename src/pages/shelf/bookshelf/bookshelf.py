from flask import Blueprint
from flask import render_template as template
import src.book as book

name = "bookshelf"
page = Blueprint(name, __name__, template_folder=".\\files")

@page.route("/", methods=['GET', 'POST'])
def bookshelf():
    book_info = book.get_book_shelf()
    return template("bookshelf.html", book_info=book_info)
