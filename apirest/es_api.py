from api_mdb import *


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


# TEST working
@route('/')
def get_test():
    log_api.info(request.method + '/')
    return j.dumps({'test': 'ok'})


# Start api
run(host='0.0.0.0', port=config.port, debug=True)
