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
    
    def post(self):
        user = User.from_json(request.json)

        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_json()), 201, \
            {'Location': url_for('api.get_post', id=user.id, _external=True)}