import logging

from flask import request
from flask_restplus import Resource
from api.business import create_event, delete_event, update_event
from api.serializers import event
from api.restplus import api
from database.models import Event

log = logging.getLogger(__name__)

ns = api.namespace('events', description='Operations related to blog events')


@ns.route('/')
class EventCollection(Resource):

    @api.marshal_list_with(event)
    def get(self):
        """
        Returns list of blog events.
        """
        events = Event.query.all()
        return events

    @api.response(201, 'Event successfully created.')
    @api.expect(event)
    def post(self):
        """
        Creates a new blog event.
        """
        data = request.json
        create_event(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Event not found.')
class EventItem(Resource):

    @api.marshal_with(event)
    def get(self, id):
        """
        Returns a event with a list of posts.
        """
        return Event.query.filter(Event.id == id).one()

    @api.expect(event)
    @api.response(204, 'Event successfully updated.')
    def put(self, id):
        """
        Updates a blog event.

        Use this method to change the name of a blog event.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Event Name"
        }
        ```

        * Specify the ID of the event to modify in the request URL path.
        """
        data = request.json
        update_event(id, data)
        return None, 204

    @api.response(204, 'Event successfully deleted.')
    def delete(self, id):
        """
        Deletes blog event.
        """
        delete_event(id)
        return None, 204
