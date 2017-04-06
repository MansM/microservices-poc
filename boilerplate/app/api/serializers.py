from flask_restplus import fields
from api.restplus import api



user = api.model('Blog user', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='user name'),
    'email': fields.String(required=True, description='email name'),
})