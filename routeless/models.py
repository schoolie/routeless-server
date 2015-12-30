from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for, jsonify
from flask.ext.login import UserMixin, AnonymousUserMixin

from routeless.exceptions import ValidationError
from routeless.extensions import db

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)


class AnonymousUser(db.Model):
    __tablename__ = 'anonymous_user'
    id = db.Column(db.Integer, primary_key=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    events = db.relationship('Event', backref='user', lazy='dynamic')
    courses = db.relationship('Course', backref='creator', lazy='dynamic')
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    
    def __repr__(self):
        return '<User %d: %s>' % (self.id, self.username)
    
    def to_json(self):
        json_user = {
            'url': url_for('UsersView:get', id=self.id, _external=True),
            'username': self.username,
            'email': self.email,
            'id': self.id,
            # 'member_since': self.member_since,
            # 'last_seen': self.last_seen,
            # 'posts': url_for('api.get_user_posts', id=self.id, _external=True),
            # 'followed_posts': url_for('api.get_user_followed_posts',
                                      # id=self.id, _external=True),
            # 'post_count': self.posts.count()
        }
        return json_user


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    check_points = db.relationship('CheckPoint', backref='course', lazy='dynamic')
    events = db.relationship('Event', backref='course', lazy='dynamic')

    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    map_layer = db.Column(db.String(10))
    zoom = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_edited = db.Column(db.DateTime(), default=datetime.utcnow)
    description = db.Column(db.Text())


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    
    routes = db.relationship('Route', backref='event', lazy='dynamic')
    check_point_logs = db.relationship('CheckPointLog', backref='event', lazy='dynamic')
    
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    time_elapsed = db.Column(db.Interval())


class CheckPoint(db.Model):
    __tablename__ = 'check_point'
    id = db.Column(db.Integer, primary_key=True)
    
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    
    check_point_logs = db.relationship('CheckPointLog', backref='check_point', lazy='dynamic')
    
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    title = db.Column(db.String(10))
    message = db.Column(db.String(140))


class CheckPointLog(db.Model):
    __tablename__ = 'check_point_log'
    id = db.Column(db.Integer, primary_key=True)
    
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    check_point_id = db.Column(db.Integer, db.ForeignKey('check_point.id'))
    
    log_points = db.relationship('LogPoint', backref='check_point_log', lazy='dynamic')
    
    found = db.Column(db.Integer, default=False)
    check_count = db.Column(db.Integer, default=0)


class Route(db.Model):
    __tablename__ = 'route'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    route_points = db.relationship('RoutePoint', backref='route', lazy='dynamic')


class RoutePoint(db.Model):
    __tablename__ = 'route_point'
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    time = db.Column(db.DateTime(), default=datetime.utcnow)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)


class LogPoint(db.Model):
    __tablename__ = 'log_point'
    id = db.Column(db.Integer, primary_key=True)
    check_point_log_id = db.Column(db.Integer, db.ForeignKey('check_point_log.id'))
    time = db.Column(db.DateTime(), default=datetime.utcnow)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    distance = db.Column(db.Float)
    type = db.Column(db.String(10))