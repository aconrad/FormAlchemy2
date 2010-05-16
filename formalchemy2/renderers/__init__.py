#coding: utf-8


class Renderer(object):
    """The base Renderer class."""

    group = u'dummy'
    name = u'dummy'

    def render(self, field):
        raise NotImplementedError
