# Embedded file name: C:\Development\routeless-server\routeless\api_1_0\users2.py
from flask.ext.classy import FlaskView
from routeless.core import db
from routeless.models import User

class UsersView(FlaskView):

    def index(self):
        return 'testing'

    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return '<p>%s</p>' % user.email
        else:
            return ('Not Found', 404)