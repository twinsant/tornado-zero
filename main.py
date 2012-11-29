import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir) 

import tornado.ioloop
import tornado.web

import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'text/html')
        self.render('templates/index.html', title='%s %s' % (settings.NAME, settings.VERSION), version=settings.VERSION)

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=settings.DEBUG)

if __name__ == '__main__':
    application.listen(settings.PORT)
    tornado.ioloop.IOLoop.instance().start()
