from database import db
from database.models import User

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
