#coding: utf-8
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError


class Field(object):
    """The base Field class.

    Takes the following arguments:
    * id: id of the field

    Optional keyword arguments:
    * label (None): label of the field
    * value (None): value of the field
    * renderer (None): a valid renderer for this field.
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

    Takes the same arguments as Field, and the following:
    * choices: an iterable of (id, name) pair values
    """

    def __init__(self, *args, **kwargs):
        if not 'choices' in kwargs:
            raise ValueError("%s requires a 'choices' keyword argument." %
                             self.__class__.__name__)
        self.choices = kwargs.pop('choices')
        super(FieldMultiChoice, self).__init__(*args, **kwargs)
