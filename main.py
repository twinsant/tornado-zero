import logging
import os
import sys

from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line
from tornado.web import Application
from tornado.web import URLSpec
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

try:
    from local_conf import DEFAULT_PORT
except ImportError:
    logging.error('Please setup a local config file: cp local_conf.py.sample local_conf.py')
    sys.exit(-1)

from handlers.base import IndexHandler
from handlers.base import APIUserHandler
from handlers.base import APIUserAuthHandler

handlers = [
    URLSpec('/', IndexHandler, name='index'),

    URLSpec('/api/user', APIUserHandler, name='api_user'),
    URLSpec('/api/user/auth', APIUserAuthHandler, name='api_user_auth'),
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
