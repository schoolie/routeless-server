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
    # cors.init_app(app, resources={"/api_1_0/*": {"origins": "http://localhost:8383"}})
    # cors.init_app(app, resources={"/*": {"origins": "http://localhost:8383"}})
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
    # if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        # from flask.ext.sslify import SSLify
        # sslify = SSLify(app)

    from api_1_0 import UsersView
    UsersView.register(app, route_base='/api_1_0/users_', trailing_slash=False)
    
    with app.app_context():
        url_prefix = '/api_1_0'
        
        # def print_request(**kw):
            # pass
        def print_request(**kw):
            # pdb.set_trace()
            try:
                print 'request'
                print request.data
            except:
                pass
        '''
        user_api = api_manager.create_api_blueprint(
                            User, 
                            collection_name='users_',
                            url_prefix=url_prefix, 
                            methods=['GET', 'POST', 'PUT'], 
                            preprocessors={
                                    'GET_SINGLE': [print_request],
                                    'PUT_SINGLE': [print_request]
                                     },
                            # postprocessors={
                                    # 'GET_SINGLE': [teardown],
                                    # 'PUT_SINGLE': [teardown]
                                     # },
                            app=app
                           )
        app.register_blueprint(user_api)       
        '''
        
        course_api = api_manager.create_api_blueprint(
                            Course, 
                            collection_name='courses',
                            url_prefix=url_prefix, 
                            methods=['GET', 'POST', 'PUT'], 
                            preprocessors={
                                    'GET_SINGLE': [print_request],
                                    'PUT_SINGLE': [print_request],
                                    'POST': [print_request]
                                     },
                            # postprocessors={
                                    # 'GET_SINGLE': [teardown],
                                    # 'PUT_SINGLE': [teardown]
                                     # },
                            app=app
                           )
        app.register_blueprint(course_api)       
        
        checkpoint_api = api_manager.create_api_blueprint(
                            CheckPoint, 
                            collection_name='checkpoints',
                            url_prefix=url_prefix, 
                            methods=['GET', 'POST', 'PUT', 'DELETE'], 
                            preprocessors={
                                    'GET_SINGLE': [print_request],
                                    'PUT_SINGLE': [print_request],
                                    'DELETE_SINGLE': [print_request]
                                     },
                            # postprocessors={
                                    # 'GET_SINGLE': [teardown],
                                    # 'PUT_SINGLE': [teardown],
                                    # 'DELETE_SINGLE': [teardown]
                                     # },
                            app=app
                           )
        app.register_blueprint(checkpoint_api)
            
        event_api = api_manager.create_api_blueprint(
                            Event, 
                            collection_name='events',
                            url_prefix=url_prefix, 
                            methods=['GET', 'POST', 'PUT', 'DELETE'], 
                            preprocessors={
                                    'GET_SINGLE': [print_request],
                                    'PUT_SINGLE': [print_request],
                                    'DELETE_SINGLE': [print_request]
                                     },
                            # postprocessors={
                                    # 'GET_SINGLE': [teardown],
                                    # 'PUT_SINGLE': [teardown],
                                    # 'DELETE_SINGLE': [teardown]
                                     # },
                            app=app
                           )
        app.register_blueprint(event_api)
    

    
    @app.route('/test', methods = ['POST'])
    def test():
        print request.data
        # pdb.set_trace()
        return 'done'
    
    print app.url_map
    
    return app
    
    