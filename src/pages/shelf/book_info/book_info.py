from flask import Blueprint, request
from flask import render_template as template
import src.book as book

page = Blueprint(book.get_name(__name__), book.get_name(__name__),
                 template_folder=book.get_path(__name__))


@page.route("/shelf/book_info", methods=['GET', 'POST'])
def bookshelf():
    data = request.args
    return data
