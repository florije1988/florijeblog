# coding=utf8

"""
    blog.views.page
    ~~~~~~~~~~~~~~~

    routes:

      page
        GET, `page/<int:page_number>`, display a page
"""

from flask import abort
from skylark import fn

from blog import app
from blog.models import Post
from blog.views.utils import render_public


@app.route('/page/<int:page_number>')
def page(page_number):
    if page_number <= 0:
        abort(404)

    n = 9

    query = Post.where(published=True).orderby(
        Post.datetime, desc=True).limit(n, offset=n * (page_number - 1)
                                        ).select()
    results = query.execute()
    count = results.count

    if count < 0:  # no posts
        abort(404)

    query = Post.where(published=True).select(fn.count(Post.id))
    result = query.execute()
    func = result.one()
    total_count = func.count

    is_first_page = True if page_number == 1 else False
    is_last_page = True if n * page_number >= total_count else False

    posts = tuple(results.all())

    page = dict(
        number=page_number,
        posts=posts,
        first=is_first_page,
        last=is_last_page
    )
    return render_public('page.html', page=page)
