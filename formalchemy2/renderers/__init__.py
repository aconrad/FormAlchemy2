#coding: utf-8


class BaseRenderer(object):
    """The base Renderer class.

    This class must be subclassed by all renderers.

    """
    def render(self, field):
        raise NotImplementedError
