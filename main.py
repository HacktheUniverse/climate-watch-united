import os
import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def mainfunc(self):
        user=None
        if users.get_current_user():
            user=users.get_current_user().nickname()
            limit='100'
        else:
            limit='10'

        template_values = {
                'user': user, 
                'logout':users.create_logout_url('/'),
                'limit': limit,
                'request': self.request,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class MainPage(webapp2.RequestHandler):
    def get(self):
        mainfunc(self)


application = webapp2.WSGIApplication([
    ('/', MainPage)

], debug=True)

