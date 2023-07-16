from flask import Blueprint, request
from flask import render_template as template
import src.book as book

name = "bookinfo"
page = Blueprint(name, __name__, template_folder=".\\files")


@page.route("/shelf/bookinfo", methods=['GET', 'POST'])
def bookshelf():
    data = request.args
    return data
