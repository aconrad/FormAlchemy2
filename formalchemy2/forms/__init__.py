#coding: utf-8

from formalchemy2.utils import OrderedDict


class Form(object):
    """The Form class.

    Represents a set of fields that can be rendered in one shot.

    Arguments:
    default_renderer -- the renderer to be set to a field if not
    present (default None).
    default_validator -- the validator to be set to a field if not
    present (default None).
    default_prettifyer -- the label prettifyer to be set to a field if
    not present (default None).

    """

    input_data = None

    def __init__(self, default_renderer=None, default_validator=None,
                 default_prettifyer=None):
        self.default_renderer = default_renderer
        self.default_validator = default_validator
        self.default_prettifyer = default_prettifyer
        self.fields = OrderedDict()

    def __contains__(self, field):
        return field.id in self.fields

    def __iter__(self):
        return self.fields.itervalues()

    def __len__(self):
        return len(self.fields)

    def append(self, field):
        """Append given field to the form.

        If the form has a default renderer, a default validator or a
        default prettifyer, the field will have them set if any of them
        are missing on the field itself, respectively.

        """
        if self.default_renderer and field.renderer is None:
            field.renderer = self.default_renderer
        if self.default_validator and field.validator is None:
            field.validator = self.default_validator
        if self.default_prettifyer and field.prettifyer is None:
            field.prettifyer = self.default_prettifyer
        self.fields[field.id] = field

    def remove(self, field):
        """Remove field from the form."""
        del self.fields[field.id]

    def _get_data(self):
        return dict((field.id, field.value) for field in self)

    def _set_data(self, data):
        for field in self:
            field.value = data[field.id]

    data = property(_get_data, _set_data, None, "Return a dict of all fields "
                    "ids and values. A similar dict can be given to set field "
                    "values all in once.")

    def validate(self):
        """Validate all field values."""
        for field in self:
            field.validate()

    def render(self):
        """Return all fields rendered and concatenated."""
        output = u""
        for field in self:
            output += field.render()
        return output
