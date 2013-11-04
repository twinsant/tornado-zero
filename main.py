import logging
import os

from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line
from tornado.web import Application
from tornado.web import URLSpec
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from local_conf import DEFAULT_PORT
from handlers.base import IndexHandler

handlers = [
    URLSpec('/', IndexHandler, name='index'),
]

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies = True,
    cookie_secret = 'openssl rand 32 -base64',
    # Other settings
)

if __name__ == '__main__':
    define('port', default=DEFAULT_PORT, help='port', type=int)
    define('debug', default=False, help='debug', type=bool)
    parse_command_line()

    settings['debug'] = options.debug
    application = Application(handlers, **settings)
    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    logging.info('Listen on %d, debug=%s' % (options.port, options.debug))

    IOLoop.instance().start()
