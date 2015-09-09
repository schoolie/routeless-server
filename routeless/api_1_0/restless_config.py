from flask import current_app

from routeless.extensions import api_manager
from routeless.api_1_0.api_config import url_prefix, authenticate

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
                   }