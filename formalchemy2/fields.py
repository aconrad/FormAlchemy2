#coding: utf-8
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import *

class Field(object):
    def __init__(self, id):
        self.id = id
        self.renderer = None

    def has_renderer(self):
        return isinstance(self.renderer, Renderer)

    def render(self):
        """Call and return renderer's data."""
        if self.renderer is None:
            raise NoRendererError
        return self.renderer.render()
