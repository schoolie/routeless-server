from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from routeless.models import User, Course, Event, CheckPoint, CheckPointLog
from routeless.extensions import db

admin = Admin(name='Routeless')


class RoutelessView(ModelView):
    column_display_pk = True # optional, but I like to see the IDs in the list

class CourseView(RoutelessView):
    inline_models = (CheckPoint, Event)
    can_delete = False
    
class EventView(RoutelessView):
    inline_models = (CheckPointLog,)
    # can_delete = False


admin.add_view(RoutelessView(User, db.session))
admin.add_view(CourseView(Course, db.session))
admin.add_view(EventView(Event, db.session))
