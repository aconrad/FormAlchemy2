#coding: utf-8


class Renderer(object):
    """The base Renderer class."""

    group = None
    name = None
    encoding = None

    def __init__(self, encoding=None):
        self.encoding = encoding

    def render(self, field):
        if isinstance(self.encoding, basestring):
            return u"".encode(self.encoding)
        return u""
