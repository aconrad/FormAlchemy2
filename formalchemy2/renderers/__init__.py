#coding: utf-8


class Renderer(object):
    """The base Renderer class."""

    group = None
    name = None

    def render(self, field):
        raise NotImplementedError
