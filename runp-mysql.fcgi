#!flask/bin/python

import os

from flup.server.fcgi import WSGIServer
from routeless import create_app

app = create_app('dev_server')

if __name__ == '__main__':
    WSGIServer(app).run()