from google.appengine.ext import ndb

class Message(ndb.Model):
    message_text = ndb.StringProperty()

class Guestbook(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    text = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)