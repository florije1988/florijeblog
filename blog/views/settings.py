# coding=utf8

"""
    blog.views.settings
    ~~~~~~~~~~~~~~~~~~~

    routes:

      settings
        GET, `/settings`, display settings

      update_settings
        POST, `/settings/update`, update settings
"""

from flask import render_template, request, redirect, url_for

from blog import app
from blog.models import Blog
from blog.views.login import login_required
from blog.utils import flashx


@app.route('/settings')
@login_required
def settings():

    blog = Blog.getone()

    if blog is None:
        blog = {}.fromkeys(Blog.get_fields(), '')
        flashx.warning('You have no settings, please eidt and save')
    return render_template('settings.html', active_tab='settings', blog=blog)


@app.route('/settings/update', methods=['POST'])
@login_required
def update_settings():

    name = request.form['name']
    description = request.form['description']
    disqus = request.form['disqus']

    blog = Blog.getone()

    if blog is None:  # insert
        blog = Blog.create(name=name, description=description, disqus=disqus)
        flashx.success('Create settings successfully')
    else:  # update
        blog.name = name
        blog.disqus = disqus
        blog.description = description
        blog.save()
        flashx.success('Save settings successfully')

    return redirect(url_for('settings'))

