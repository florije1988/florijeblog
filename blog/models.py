# coding=utf8

"""
    blog.models
    ~~~~~~~~~~~

    tables to models mappings
"""

from hashlib import md5

from blog import app
from blog.markdown import markdown

from skylark import Model, Field, Database


class Author(Model):

    name = Field()
    email = Field()
    description = Field()
    url = Field()

    @property
    def gravatar_id(self):
        if self.email:
            return md5(self.email).hexdigest()
        return ''


class Blog(Model):

    name = Field()
    description = Field()
    disqus = Field()


class Post(Model):

    datetime = Field()
    title = Field()
    title_pic = Field()
    body = Field()
    published = Field()

    @property
    def summary(self):
        return markdown.render(self.body[:150])


class Admin(Model):

    passwd = Field()


Database.config(**app.config['DB_CFG'])
