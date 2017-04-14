from database import db
from database.models import User, Event

def create_user(data):
    name = data.get('name')
    user_id = data.get('id')
    email = data.get('email')

    user = User(name, email)
    if user_id:
        user.id = user_id

    db.session.add(user)
    db.session.commit()


def update_user(user_id, data):
    user = User.query.filter(User.id == user_id).one()
    user.name = data.get('name')
    user.email = data.get('email')
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    user = User.query.filter(User.id == user_id).one()
    db.session.delete(user)
    db.session.commit()

def create_event(data):
    date = data.get('date')
    title = data.get('title')
    location = data.get('location')
    description = data.get('description')
    maxpeople = data.get('maxpeople')

    event = Event(title, date, location, description, maxpeople)
    if event_id:
        event.id = event_id

    db.session.add(event)
    db.session.commit()

def update_event(event_id, data):
    event = Event.query.filter(Event.id == event_id).one()
    title = data.get('title')
    date = data.get('date')
    location = data.get('location')
    description = data.get('description')
    maxpeople = data.get('maxpeople')
    db.session.add(event)
    db.session.commit()

def delete_event(event_id):
    event = Event.query.filter(Event.id == event_id).one()
    db.session.delete(event)
    db.session.commit()