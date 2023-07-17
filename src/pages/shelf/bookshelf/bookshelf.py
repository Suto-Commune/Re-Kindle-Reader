from flask import Blueprint
from flask import render_template as template
import src.book as book

page = Blueprint(book.get_name(__name__), book.get_name(__name__),
                 template_folder=book.get_path(__name__))


@page.route("/", methods=['GET', 'POST'])
def bookshelf():
    book_info = book.get_book_shelf()
    return template("index.html", book_info=book_info)
