#coding: utf-8

from formalchemy2.utils import OrderedDict


class Form(object):
    """The Form class.

    Represents a set of fields that can be rendered in one shot.

    Arguments:
    default_renderer -- the renderer used if a field doesn't have a
    renderer (default None).
    default_validator -- the validator used if a field doesn't have a
    validator (default None).

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
        """Append a field to the form."""
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

    def data(self):
        """Return a dict containing all fields ids and values."""
        return dict((field.id, field.value) for field in self)

    def validate(self, data):
        """Validate input data against form fields and return a dict
        containing field ids and their validated values.

        Arguments:
        data -- a dict of field ids and values to validate. Typically
        the content of an HTTP POST request.

        """
        self.input_data = data

        validation = {}
        for field in self:
            validation[field.id] = field.validate(data[field.id])
        return validation

    def render(self):
        """Return all fields rendered and concatenated."""
        output = u""
        for field in self:
            output += field.render()
        return output
