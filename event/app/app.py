import logging.config

from flask import Flask, Blueprint
import settings
from api.endpoints.users import ns as users_namespace
from api.endpoints.events import ns as events_namespace
from api.endpoints.registrations import ns as registrations_namespace
from api.restplus import api
from database import db
from datetime import datetime

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['HOST'] = settings.FLASK_HOST


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(users_namespace)
    api.add_namespace(events_namespace)
    api.add_namespace(registrations_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)



def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    log.info(datetime.now())
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_HOST)

if __name__ == "__main__":
    main()
