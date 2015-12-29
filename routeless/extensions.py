
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
api_manager = APIManager(flask_sqlalchemy_db=db)
ma = Marshmallow()
