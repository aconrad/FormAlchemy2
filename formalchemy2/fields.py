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
    renderer -- a valid renderer for this field (default None)

    """
    def __init__(self, id, label=None, value=None, renderer=None):
        self.id = id
        self.label = label
        self.value = value
        self.renderer = renderer

    def has_renderer(self):
        """Return True if the field has a valid renderer."""
        return isinstance(self.renderer, BaseRenderer)

    def render(self):
        """Shortcut for field.renderer.render().

        Raise NoRendererError if no renderer is set.

        """
        if not self.has_renderer():
            raise NoRendererError
        return self.renderer.render(self)


class FieldMultiChoice(Field):
    """The base Field for multi-choice value.

    Arguments:
    id -- id of the field
    choices -- an iterable of (id, name) pair values

    Keyword arguments:
    Takes the same keyword arguments as Field.

    """
    def __init__(self, id, choices, *args, **kwargs):
        super(FieldMultiChoice, self).__init__(id, *args, **kwargs)
        self.choices = choices
