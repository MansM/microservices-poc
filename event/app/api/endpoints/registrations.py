import logging

from flask import request
from flask_restplus import Resource
from api.business.registration import create_registration, delete_registration
from api.serializers import registration
from api.restplus import api
from database.models import Registration

log = logging.getLogger(__name__)

ns = api.namespace('registrations', description='Operations related to event registrations')


@ns.route('/')
class RegistrationCollection(Resource):

    @api.marshal_list_with(registration)
    def get(self):
        """
        Returns list of blog registrations.
        """
        registrations = Registration.query.all()
        return registrations

    @api.response(201, 'Registration successfully created.')
    @api.expect(registration)
    def post(self):
        """
        Creates a new blog registration.
        """
        data = request.json
        create_registration(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Registration not found.')
class RegistrationItem(Resource):

    @api.marshal_with(registration)
    def get(self, id):
        """
        Returns a registration with a list of posts.
        """
        return Registration.query.filter(Registration.id == id).one()

    # @api.expect(registration)
    # @api.response(204, 'Registration successfully updated.')
    # def put(self, id):
    #     """
    #     Updates a blog registration.

    #     Use this method to change the name of a blog registration.

    #     * Send a JSON object with the new name in the request body.

    #     ```
    #     {
    #       "name": "New Registration Name"
    #     }
    #     ```

    #     * Specify the ID of the registration to modify in the request URL path.
    #     """
    #     data = request.json
    #     update_registration(id, data)
    #     return None, 204

    @api.response(204, 'Registration successfully deleted.')
    def delete(self, id):
        """
        Deletes blog registration.
        """
        delete_registration(id)
        return None, 204
