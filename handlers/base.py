from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')
