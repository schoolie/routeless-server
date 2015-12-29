from flask import current_app
from flask.ext.restless import ProcessingException

from routeless.extensions import api_manager
from routeless.api_1_0.api_config import url_prefix, authenticate, create_user, create_check_point_logs, \
                                         event_serializer, event_deserializer
from routeless.models import User
from routeless.extensions import db


course_api_config = {'collection_name': 'courses',
                    'url_prefix': url_prefix, 
                    'methods': ['GET', 'POST', 'PUT'], 
                    'preprocessors': {
                            'GET_MANY': [authenticate],
                            'GET_SINGLE': [authenticate],
                            'PUT_SINGLE': [authenticate],
                            'POST': [authenticate]
                             },
                    # postprocessors': {
                            # 'GET_SINGLE': [teardown],
                            # 'PUT_SINGLE': [teardown]
                             # },
                   }
                   
checkpoint_api_config = {'collection_name': 'checkpoints',
                    'url_prefix': url_prefix, 
                    'methods': ['GET', 'POST', 'PUT', 'DELETE'], 
                    'preprocessors': {
                            'GET_MANY': [authenticate],
                            'GET_SINGLE': [authenticate],
                            'PUT_SINGLE': [authenticate],
                            'POST': [authenticate]
                             },
                   }      
                   
event_api_config = {'collection_name': 'events',
                    'url_prefix': url_prefix, 
                    'methods': ['GET', 'POST', 'PUT', 'DELETE'], 
                    'preprocessors': {
                            'GET_MANY': [authenticate],
                            'GET_SINGLE': [authenticate],
                            'PUT_SINGLE': [authenticate],
                            'POST': [authenticate]
                             },
                    'postprocessors': {'POST': [create_check_point_logs]},
                    'serializer': event_serializer,
                    'deserializer': event_deserializer
                   }
                   
user_api_config = {'collection_name': 'users',
                    'url_prefix': url_prefix, 
                    'methods': ['GET', 'POST', 'PUT', 'DELETE'], 
                    'preprocessors': {
                            'GET_MANY': [authenticate],
                            'GET_SINGLE': [authenticate],
                            'PUT_SINGLE': [authenticate],
                            'POST': [create_user]
                             },
                   }