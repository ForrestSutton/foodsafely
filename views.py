import os
import jinja2
import webapp2
from models import Item
from datetime import datetime
from google.appengine.ext import ndb

template_dir=os.path.join(os.path.dirname(__file__),"templates")
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(BaseHandler):
    def get(self):
	items = ndb.gql("SELECT * FROM Item LIMIT 10")
	item_dic = {"items": items }
        self.render('index.html', **item_dic)

    def post(self):
        title   = self.request.get('name')
        itemNum = self.request.get('itemNum')
        origin  = self.request.get('origin')
        self.write(name)
        self.write("<br />")
        self.write(itemNum)
        self.write("<br />")
        self.write(origin)

class New(BaseHandler):
    def get(self):
        self.render('new.html')
  
    def post(self):
        name    = self.request.get('name')
        itemNum = self.request.get('itemNum')
        origin = self.request.get('origin')
        
        item_post = Item(name=name, itemNum=itemNum, origin=origin)
        item_post.put()
        self.redirect('/')    

class About(BaseHandler):
    def get(self):
        self.render('about.html')
