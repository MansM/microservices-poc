from database import db
from database.models import Event


def create_event(data):
    date = data.get('date')
    event_id = data.get('id')
    title = data.get('title')
    location = data.get('location')
    description = data.get('description')
    maxpeople = data.get('maxpeople')

    # event = Event(title, date, location, description, maxpeople)
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