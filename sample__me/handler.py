import os
from base.handler import _base


class base(_base):
  def static_url(self, path, include_host=None):
    fixd_path = os.path.join(__package__, 'static', path)
    return  _base.static_url(self, fixd_path, include_host).replace(__package__, '')


class index(base):
  def get(self):
    self.render('tpl/index.html')


router = [
  (r"/", index),
]
