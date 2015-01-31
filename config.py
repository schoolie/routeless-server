import os

basedir = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = basedir
    
    

SQLALCHEMY_DATABASE_URI = os.environ['SS_DATABASE_URL']


SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    
SQLALCHEMY_POOL_RECYCLE = 200

# email server
MAIL_SERVER='mail.schoolcraftspecialties.com'
MAIL_PORT=26
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


# administrator list
ADMINS = ['admin@schoolcraftspecialties.com',
          'brian@schoolcraftspecialties.com']
