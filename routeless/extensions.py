# Embedded file name: C:\Development\routeless-server\routeless\core.py
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

db = SQLAlchemy()
api_manager = APIManager(flask_sqlalchemy_db=db)
