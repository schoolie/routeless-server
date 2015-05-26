from flask import current_app

from routeless.extensions import api_manager
from ..models import Course

print api_manager.app
course_api = api_manager.create_api_blueprint(Course, methods=['GET', 'POST'], app=current_app())