# Embedded file name: C:\Development\routeless-server\routeless\api_1_0\users2.py
from flask import jsonify
from flask.ext.classy import FlaskView
from routeless.core import db
from routeless.models import User

class CoursesView(FlaskView):
    
    def index(self):
        users = User.query.all()
        return jsonify({'list':[user.to_json() for user in users]})
    
    def get(self, username):
        user = User.query.filter(User.username == username).first()
        if user:
            return jsonify(user.to_json())
        else:
            return ('Not Found', 404)
    
    def post(self):
        user = User.from_json(request.json)

        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_json()), 201, \
            {'Location': url_for('api.get_post', id=user.id, _external=True)}