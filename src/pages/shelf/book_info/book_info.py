from flask import Blueprint, request
from flask import render_template as template
import src.book as book

name = "book_info"
page = Blueprint(name, __name__, template_folder=".\\files")


@page.route("/shelf/book_info", methods=['GET', 'POST'])
def bookshelf():
    data = request.args
    return data
