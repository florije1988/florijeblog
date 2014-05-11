# coding=utf8

from blog import app
from blog.views.utils import render_public
from blog.views.page import page


@app.route('/')
def index():
    return page(1)


@app.errorhandler(404)
def page_not_found(error):
    return render_public('404.html'), 404
