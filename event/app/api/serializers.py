from flask_restplus import fields
from api.restplus import api



user = api.model('user', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='user name'),
    'email': fields.String(required=True, description='email name'),
})

event = api.model('event', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an event'),
    'title': fields.String(required=True, description='title'),
    'date': fields.DateTime(required=True, description='date'),
    'location': fields.String(required=True, description='location'),
    'description': fields.String(required=True, description='description'),
    'maxpeople' : fields.Integer(description='max people'),

})

registration = api.model('registration', {
    'id': fields.Integer(readOnly=True, description='Registration number'),
    'user_id': fields.Integer(required=True),
    # 'user': fields.String(attribute='user.id'),
    'event_id': fields.Integer(required=True),
    # 'event': fields.String(attribute='event.id'),
})