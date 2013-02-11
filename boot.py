#!/usr/bin/env python

import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, parse_config_file, parse_command_line

import base.handler

parse_config_file(os.path.join(os.path.dirname(__file__), "setting.py"))
parse_command_line()


class Application(tornado.web.Application):

  def __init__(self):
    tornado.web.Application.__init__(self,
      [(r"/(.*)$", base.handler.not_found)],
      static_path = os.path.join(os.path.dirname(__file__), './'),
      static_url_prefix = '',
      debug = options.debug,
    )

    self.auto_load_domain()

  def auto_load_domain(self):
    for dir in os.listdir():
      '''
        the domain dirname use '__' instead '.' for pypackage: a__com a__b__com
      '''
      if os.path.isdir(os.path.dirname(__file__) + dir) and '__' in dir:
        module = __import__(dir, fromlist = ["handler"])
        domain = dir.replace('__', '.')
        module.handler.router.extend([
          (r"/(favicon.ico)", tornado.web.StaticFileHandler,
            {'path': os.path.join(os.path.dirname(__file__), dir, "static")}),
          (r"/static/(.*)", tornado.web.StaticFileHandler,
            {'path': os.path.join(os.path.dirname(__file__), dir, "static")}),
        ])
        if options.debug:
          domain = __import__('re').sub(r'\.(\w+)$', '.dev', domain)
        self.add_handlers(domain, module.handler.router)

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
