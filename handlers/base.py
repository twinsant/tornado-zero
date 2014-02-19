import functools

from tornado.web import RequestHandler
from tornado.web import HTTPError

from duck import *

class BaseHandler(RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

def api_authenticated(method):
    """Decorate api methods with this to require that the user be logged in."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            raise HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper

class APIHandler(BaseHandler):
    def arguments_required(self, arguments):
        for argument in arguments:
            if self.get_argument(argument, None) is None:
                # TODO: better error info
                raise HTTPError(400)

    def clean_get(self, name, default=''):
        ret = self.get_argument(name, default)
        ret = ret.strip()
        if ret == '':
            return None
        return ret

class APIUserHandler(APIHandler):
    @api_authenticated
    def get(self):
        self.write({})

class APIUserAuthHandler(APIHandler):
    def post(self):
        # TODO: security logging. ip and failed
        self.arguments_required(['aid', 'password'])

        aid = self.clean_get('aid')
        password = self.clean_get('password')

        token = user_auth(aid, password)
        if token is None:
            raise HTTPError(403)
        self.set_secure_cookie('token', token)
        self.write({'token':token})
