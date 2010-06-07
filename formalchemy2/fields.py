#coding: utf-8
from formalchemy2.exceptions import NoRendererError, NoValidatorError


class Field(object):
    """The base Field class.

    Arguments:
    id -- id of the field

    Keyword arguments:
    label -- label of the field (default value of id)
    value -- value of the field (default None)
    choices -- an iterable of (id, name) pair values (default None)
    renderer -- a renderer for this field (default None)
    validator -- a validator for this field (default None)
    prettifyer -- a label prettifyer (default None)

    """
    def __init__(self, id, label=None, value=None, choices=None,
                 renderer=None, validator=None, prettifyer=None):
        self.id = id
        self.label = label
        self.value = value
        self.choices = choices
        self.renderer = renderer
        self.validator = validator
        self.prettifyer = prettifyer

    def _get_label(self):
        if self.prettifyer:
            return self.prettifyer(self._label)
        return self._label

    def _set_label(self, label):
        if label is None:
            self._label = self.id
        else:
            self._label = label

    label = property(_get_label, _set_label)

    def validate(self):
        """Validate and update field value against validator.

        Raise NoValidatorError if no validator was set.

        """
        if self.validator is None:
            raise NoValidatorError('Field %s has no validator assigned.' %
                                   self.id)
        self.value = self.validator(self.value)

    def render(self):
        """Shortcut for field.renderer.render().

        Raise NoRendererError if no renderer is set.

        """
        if not self.renderer:
            raise NoRendererError('Field %s has no renderer assigned.' %
                                  self.id)
        return self.renderer.render(self)
