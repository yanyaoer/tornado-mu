import tornado.web


class _base(tornado.web.RequestHandler):
  pass


class not_found(_base):
  def get(self, uri=''):
    self.write(str(self.request))
