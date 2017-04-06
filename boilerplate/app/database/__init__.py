from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)

from database import models

def reset_database():
    from database.models import User  # noqa
    db.drop_all()
    db.create_all()
