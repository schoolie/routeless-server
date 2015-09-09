# Embedded file name: C:\Development\routeless-server\routeless\__init__.py
from datetime import datetime
from flask import Flask, jsonify, request, current_app
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask.ext.cors import CORS
from flask_jwt import JWT, jwt_required


from routeless.extensions import db, api_manager
from routeless.models import User, Course, CheckPoint, Event
from routeless.api_1_0 import course_api_config, checkpoint_api_config, event_api_config
from config import config

import pdb

mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
cors = CORS()
jwt = JWT()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    api_manager.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "http://*"}})
    jwt.init_app(app)
    

    @jwt.authentication_handler
    def authenticate(username, password):
        user = User.query.filter(User.username == username).first()
        print 'User:', user
        if user is not None:
            if password == user.password:
                return user

    @jwt.user_handler
    def load_user(payload):
        if 'id' in payload.keys():
            user = User.query.filter_by(id=payload['id']).first()
            return user
            
    @jwt.payload_handler
    def make_payload(user):
        payload = {
            'id': user.id,
            'username': user.username,
            # 'exp': datetime.utcnow() + current_app.config['JWT_EXPIRATION_DELTA']
        }
        print 'payload:', payload
        return payload

    from api_1_0 import UsersView
    UsersView.register(app, route_base='/api_1_0/users_', trailing_slash=False)
    
    with app.app_context():
        
        course_api = api_manager.create_api_blueprint(Course, app=app, **course_api_config)
        app.register_blueprint(course_api)       
        
        
        checkpoint_api = api_manager.create_api_blueprint(CheckPoint, app=app, **checkpoint_api_config)
        app.register_blueprint(checkpoint_api)
            
        event_api = api_manager.create_api_blueprint(Event, app=app, **event_api_config)
        app.register_blueprint(event_api)
        
    @app.route('/test', methods = ['POST'])
    def test():
        print request.data
        # pdb.set_trace()
        return 'done'
    
    print app.url_map
    
    return app
    
    