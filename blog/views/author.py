# coding=utf8

"""
    blog.views.author
    ~~~~~~~~~~~~~~~~~

    routes:

      author
        GET, `/author`, display author
"""

from flask import render_template, request, redirect, url_for

from blog import app
from blog.models import Author
from blog.views.login import login_required
from blog.utils import flashx


@app.route('/author')
@login_required
def author():

    author = Author.getone()

    if author is None:
        author = {}.fromkeys(Author.get_fields(), '')
        flashx.warning('Please compelte author\'s information')
    return render_template('author.html', active_tab='author', author=author)


@app.route('/author/update', methods=['POST'])
@login_required
def update_author():

    name = request.form['name']
    email = request.form['email']
    url = request.form['url']
    description = request.form['description']

    if not name or not email:
        flashx.warning('Empty input')

    else:
        author = Author.getone()

        if author is None:  # do a insert
            author = Author.create(name=name, email=email, url=url, description=description)
            flashx.success('Create author information successfully')
        else:  # do a save
            author.name = name
            author.email = email
            author.url = url
            author.description = description
            author.save()
            flashx.success('Save author information successfully')
    return redirect(url_for('author'))
