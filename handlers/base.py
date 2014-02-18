import functools

from tornado.web import RequestHandler
from tornado.web import HTTPError

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

class APIUserHandler(BaseHandler):
    @api_authenticated
    def get(self):
        self.write({})
