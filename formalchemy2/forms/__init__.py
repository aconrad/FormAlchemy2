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

    def __len__(self):
        return len(self.fields)

    def append(self, field):
        """Append a field to the form."""
        self.fields[field.id] = field

    def render(self):
        """Return all fields rendered and concatenated."""
        # Init output as str. If a field returns Unicode, output will be
        # overriden.
        output = ""
        for field in self.fields.values():
            output += field.render()
        return output