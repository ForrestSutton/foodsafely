from google.appengine.ext import ndb
import datetime

class Item(ndb.Model):
    name    = ndb.StringProperty()
    itemNum = ndb.StringProperty()
    origin  = ndb.StringProperty()
    facility_id = ndb.StringProperty() 
    nuts    = ndb.BooleanProperty()	
    peanuts = ndb.BooleanProperty()	
    eggs    = ndb.BooleanProperty()	
    dairy   = ndb.BooleanProperty()	
    wheatGluten = ndb.BooleanProperty()	
    soy    = ndb.BooleanProperty()	
    update = ndb.DateTimeProperty(auto_now_add=True)
