#coding: utf-8

from formalchemy2.renderers import Renderer


class Dummy(Renderer):
    """A dummy Renderer class."""

    group = u'dummy'
    name = u'dummy'

    def render(self, field):
        return u"%s (%s): %s\n" % (field.label, field.id, field.value)
