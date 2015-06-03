# Embedded file name: C:\Development\routeless-server\routeless\api_1_0\users2.py
from flask import jsonify, request, url_for
from flask.ext.classy import FlaskView
from routeless.extensions import db
from routeless.models import User

class UsersView(FlaskView):
    
    def index(self):
        users = User.query.all()
        return jsonify({
                        'objects':[user.to_json() for user in users],
                        'num_results': len(users),
                        'page': 1,
                        'total_pages': 1
                       })
    
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return jsonify(user.to_json())
        else:
            return ('Not Found', 404)
    
    def post(self):
        print request.json
        # import pdb; pdb.set_trace()
        user = User(username = request.json['username'])
        
        if User.query.filter(User.username == user.username).count() > 0:
            return ('Already Exists', 422)
            
        
        db.session.add(user)
        db.session.commit()
        print 'worked'
        # except: #####################FIX THIS
            # db.session.rollback()
        
        return jsonify(user.to_json()), 201, \
            {'Location': url_for('UsersView:get', id=user.id, _external=True)}