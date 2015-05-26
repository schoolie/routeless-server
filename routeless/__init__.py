# Embedded file name: C:\Development\routeless-server\routeless\__init__.py
from flask import Flask, jsonify
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask.ext.cors import CORS

from routeless.extensions import db, api_manager
from routeless.models import User, Course
from config import config

import pdb

mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
cors = CORS()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    api_manager.init_app(app)
    cors.init_app(app, resources={"/api_1_0/*": {"origins": "http://localhost:8383"}})
    
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)

    from api_1_0 import UsersView
    UsersView.register(app, route_base='/api_1_0/users/')
    
    with app.app_context():
        course_api = api_manager.create_api_blueprint(Course, 
                                                      methods=['GET', 'POST'],
                                                      app=app)
        app.register_blueprint(course_api)
    
    print app.url_map
    
    return app
    
    