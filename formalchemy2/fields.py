#coding: utf-8
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import NoRendererError


class Field(object):
    """The base Field class.

    Takes the following arguments:
    * id: id of the field

    Optional keyword arguments:
    * label (None): label of the field
    * value (None): value of the field
    * renderer (None): renderer for this field
    """

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


class FieldMultiChoice(Field):
    """The base Field for multi-choice value.

    Takes the same arguments as Field, and the following:
    * choices: an iterable of (id, name) pair values
    """

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices')
        super(FieldMultiChoice, self).__init__(*args, **kwargs)
