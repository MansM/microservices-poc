from database import db
from database.models import Registration

def create_registration(data):
    registration_id = data.get('id')
    user_id = data.get('user_id')
    # user = User.query.filter(User.id == user_id).one()
    event_id = data.get('event_id')
    # event = Event.query.filter(Event.id == event_id).one()
    registration = Registration(user_id, event_id)
    db.session.add(registration)
    db.session.commit()


def delete_registration(registration_id):
    registration = Registration.query.filter(Registration.id == registration_id).one()
    db.session.delete(registration)
    db.session.commit()