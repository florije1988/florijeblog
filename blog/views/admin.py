# coding=utf8

"""
    blog.views.admin
    ~~~~~~~~~~~~~~~~~
"""

from flask import redirect, url_for

from blog import app
from blog.views.login import login_required


@app.route('/admin/')
@login_required
def admin():
    return redirect(url_for('write'))
