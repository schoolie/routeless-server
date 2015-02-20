# Embedded file name: C:\Development\routeless-server\routeless\__init__.py
from flask import Flask
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.restless import APIManager


from api_1_0 import QuotesView, UsersView
from routeless.core import db
from config import config

mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
api_manager = APIManager(flask_sqlalchemy_db=db)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    api_manager.init_app(app)
    
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)
        
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')
    
    from .models import Course
    user_bp = api_manager.create_api(Course, methods=['GET', 'POST', 'DELETE'])
    
    QuotesView.register(app, route_base='/api/')
    # UsersView.register(app)
    
    print app.url_map
    
    return app
    
    