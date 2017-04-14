# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    email = db.Column(db.String(50), index=True, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    date = db.Column(db.DateTime, index=True)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    maxpeople = db.Column(db.Integer)

    def __init__(self, title, date, location, description, maxpeople):
        self.title = title
        self.date = date
        self.location = location
        self.description = description
        self.maxpeople = maxpeople

    def __repr__(self):
        return '<Event %r>' % self.title