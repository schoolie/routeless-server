# Embedded file name: C:\Development\routeless-server\routeless\api_1_0\__init__.py
from flask import Blueprint
api = Blueprint('api', __name__)
from . import users, errors
from classy import *
from users2 import *