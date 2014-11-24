import logging
import functools

from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado.web import asynchronous

from duck import *

class BaseHandler(RequestHandler):
    def initialize(self, db):
        if db:
            logging.debug('db ready')
            self.db = db

    # def prepare(self):
    #     # finish or redirect
    #     pass

    # def on_finish(self):
    #     pass

    # def on_connection_close:
    #     pass

    # def get_user_locale:
    #     pass

    def set_default_headers(self):
        self.set_header('Server', '')

    def get_current_user(self):
        token = self.get_secure_cookie('token')
        return token

    # def write_error(self, exc_info):
    #     # HTTPError 
    #     traceback.format_exception

    # default_handler_class for 404
    # prepare

    def get_template_namespace(self):
        namespace = super(BaseHandler, self).get_template_namespace()
        namespace.update(dict(debug=self.settings['debug']))
        return namespace

    # def stream_request_body(self):
    #     pass

    # def data_received(self, data):
    #     pass

class IndexHandler(BaseHandler):
    @asynchronous
    def get(self):
        # self.request
        # - get_query_argument(s)
        # - get_body_argument(s)
        # - files: {filename:, content_type:, body:} stream_request_body

        # prepare
        self.render('index.html')

def api_authenticated(method):
    """Decorate api methods with this to require that the user be logged in."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.get_current_user():
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
        self.write(self.current_user)

class APIUserAuthHandler(APIHandler):
    def post(self):
        # TODO: security logging. ip and failed
        self.arguments_required(['aid', 'password'])

        aid = self.clean_get('aid')
        password = self.clean_get('password')

        token = user_auth(aid, password)
        if token is None:
            raise HTTPError(403)
        self.set_secure_cookie('token', token, expire_days=30)
        data = user_auth_token(token)
        self.write(data)

class APIUserLogoutHandler(APIHandler):
    def post(self):
        self.clear_cookie('token')
        self.write({})
