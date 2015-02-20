from .. import api_manager
from ..models import User

print api_manager.app
user_api = api_manager.create_api_blueprint(User, methods=['GET', 'POST'])