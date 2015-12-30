from routeless.extensions import ma
from routeless.models import Event, Course, CheckPoint, CheckPointLog, LogPoint

from marshmallow import fields

class LogPointSchema(ma.ModelSchema):
    class Meta:
        model = LogPoint
                
class CheckPointSchema(ma.ModelSchema):
    class Meta:
        model = CheckPoint
        
class CheckPointLogSchema(ma.ModelSchema):
    class Meta:
        model = CheckPointLog
        
    log_points = fields.Nested(LogPointSchema, 
                                 many=True)
                                 
class CourseSchema(ma.ModelSchema):
    class Meta:
        model = Course
        
    check_points = fields.Nested(CheckPointSchema, 
                                 many=True,
                                 exclude=('check_point_logs',))

class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event
    
    course = fields.Nested(CourseSchema)
    check_point_logs = fields.Nested(CheckPointLogSchema,
                                     many=True,
                                     exclude=('event', 'check_point'))
