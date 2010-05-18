#coding: utf-8


class Renderer(object):
    """The base Renderer class for all renderers."""

    group = None
    name = None

    def __init__(self, encoding=None):
        self.encoding = encoding

    def render(self, field):
        if self.encoding is None:
            return u""
        return u"".encode(self.encoding)


class FieldRenderer(Renderer):
    """The base Renderer class for Field objects."""


class FieldMultiChoiceRenderer(Renderer):
    """The base Renderer class for FieldMultiChoice objects."""
