#!/usr/bin/python

import webapp2
from models import Item
from views import MainPage, About, New

app = webapp2.WSGIApplication([('/', MainPage), ('/about', About),('/new', New), ], debug=True)





#class MainHandler(webapp2.RequestHandler):
#   def get(self):
#       self.response.write('hi globe')
#
#app = webapp2.WSGIApplication([
#    ('/', MainHandler)
#],debug=True )
