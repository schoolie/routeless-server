from flask_jwt import verify_jwt

url_prefix = '/api_1_0'

def authenticate(**kw):
    print '\n'
    print kw
    try:
        verify_jwt()
    except Exception, err:
        print '\n Authentication Error '
        import pdb; pdb.set_trace()
    print 'Authenticated'