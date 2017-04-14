import logging

from flask import request
from flask_restplus import Resource
from api.business import create_user, delete_user, update_user
from api.serializers import user
from api.restplus import api
from database.models import User

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to blog users')


@ns.route('/')
class UserCollection(Resource):

    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list of blog users.
        """
        users = User.query.all()
        return users

    @api.response(201, 'User successfully created.')
    @api.expect(user)
    def post(self):
        """
        Creates a new blog user.
        """
        data = request.json
        create_user(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class UserItem(Resource):

    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user with a list of posts.
        """
        return User.query.filter(User.id == id).one()

    @api.expect(user)
    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates a blog user.

        Use this method to change the name of a blog user.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New User Name"
        }
        ```

        * Specify the ID of the user to modify in the request URL path.
        """
        data = request.json
        update_user(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes blog user.
        """
        delete_user(id)
        return None, 204
