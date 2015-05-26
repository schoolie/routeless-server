from .. import api_manager
from ..models import User

print api_manager.app
course_api = api_manager.create_api_blueprint(Course, methods=['GET', 'POST'])