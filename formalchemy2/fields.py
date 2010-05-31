#coding: utf-8
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError


class Field(object):
    """The base Field class.

    Arguments:
    id -- id of the field

    Keyword arguments:
    label -- label of the field (default None)
    value -- value of the field (default None)
    choices -- an iterable of (id, name) pair values (default None)
    renderer -- a valid renderer for this field (default None)

    """
    def __init__(self, id, label=None, value=None, choices=None,
                 renderer=None):
        self.id = id
        self.label = label
        self.value = value
        self.choices = choices
        self.renderer = renderer

    def _get_label(self):
        if self._label is None:
            return self.id
        return self._label

    def _set_label(self, label):
        self._label = label
    
    label = property(_get_label, _set_label)

    def render(self):
        """Shortcut for field.renderer.render().

        Raise NoRendererError if no renderer is set.

        """
        if not self.renderer:
            raise NoRendererError('Field %s has no renderer assigned.' % self.id)
        return self.renderer.render(self)
