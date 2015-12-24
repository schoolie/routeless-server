from flask_jwt import jwt_required, current_identity
from flask.ext.restless import ProcessingException

url_prefix = '/api_1_0'

@jwt_required()
def authenticate(**kw):
    print '\n'
    print kw
    # try:
        # verify_jwt()
    # except Exception, err:
        # print '\nAuthentication Error '
        # raise ProcessingException(description='Authentication Required',
                                  # code=401)        
        # import pdb; pdb.set_trace()
    print 'Authenticated'
    
def create_user(data=None, **kw):
    print data

    if User.query.filter(User.username == data.username).count() > 0:
        raise ProcessingException(description='Username not unique',
                                  code=422)        
        if User.query.filter(User.email == data.email).count() > 0:
            raise ProcessingException(description='Email not unique',
                                      code=422)