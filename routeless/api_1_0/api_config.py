from flask_jwt import jwt_required, current_identity
from flask.ext.restless import ProcessingException

from routeless.models import User, Course, Event, CheckPointLog
from routeless.schemas import EventSchema
from routeless.extensions import db

url_prefix = '/api_1_0'

@jwt_required()
def authenticate(**kw):
    print '\n'
    print 'auth kwargs:', kw
    # try:
        # verify_jwt()
    # except Exception, err:
        # print '\nAuthentication Error '
        # raise ProcessingException(description='Authentication Required',
                                  # code=401)        
        # import pdb; pdb.set_trace()
    print 'Authenticated'
    
def create_user(data=None, **kw):
    print data

    if User.query.filter(User.username == data.username).count() > 0:
        raise ProcessingException(description='Username not unique',
                                  code=422)        
        if User.query.filter(User.email == data.email).count() > 0:
            raise ProcessingException(description='Email not unique',
                                      code=422)
                                      
def create_check_point_logs(data=None, **kw):
    print kw
    event_id = kw['result']['id']
    course_id = kw['result']['course']['id']
    
    course = Course.query.filter(Course.id == course_id).first()
    for cp in course.check_points:
        cplog = CheckPointLog(event_id=event_id,
                              check_point_id=cp.id
                             )
        db.session.add(cplog)
    db.session.commit()
    
    # import pdb; pdb.set_trace()

    
event_schema = EventSchema()

def event_serializer(instance):
    return event_schema.dump(instance).data

def event_deserializer(data):
    return event_schema.load(data).data