#coding: utf-8
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import *

class Field(object):
    """The base Field class."""

    def __init__(self, id, label=None, value=None, renderer=None):
        self.id = id
        self.renderer = renderer
        self.label = label
        self.value = value

    def has_renderer(self):
        return isinstance(self.renderer, Renderer)

    def render(self):
        """Shortcut for field.renderer.render().

        Raise NoRendererError if not renderer is set.
        """
        if not self.has_renderer():
            raise NoRendererError
        return self.renderer.render(self)
