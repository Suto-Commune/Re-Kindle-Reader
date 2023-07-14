from flask import Blueprint
from flask import render_template as template

page = Blueprint("bookshelf", __name__)


@page.route("/")
def bookshelf():
    return "hello,world"
