#coding: utf-8

from formalchemy2.utils import OrderedDict


class Form(object):
    """The Form class.

    Represents a set of fields that can be rendered in one shot.

    """
    def __init__(self):
        self.fields = OrderedDict()

    def __contains__(self, field):
        return field.id in self.fields

    def __iter__(self):
        return self.fields.itervalues()

    def __len__(self):
        return len(self.fields)

    def append(self, field):
        """Append a field to the form."""
        self.fields[field.id] = field

    def remove(self, field):
        """Remove field from the form."""
        del self.fields[field.id]

    def validate(self):
        """Validate all fields and return a dict containing field ids
        and their validated values.

        """
        validation = {}
        for field in self:
            validation[field.id] = field.validate()
        return validation

    def render(self):
        """Return all fields rendered and concatenated."""
        output = u""
        for field in self:
            output += field.render()
        return output
