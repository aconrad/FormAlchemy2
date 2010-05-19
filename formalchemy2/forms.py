#coding: utf-8


class Form(object):
    """The Form class.
    
    Represents a set of fields that can be rendered in one shot.
    
    """
    def __init__(self):
        self.fields = []

    def append(self, field):
        """Append a field to the form."""
        self.fields.append(field)

    def render(self):
        """Return all fields rendered and concatenated."""
        # Init output as str. If a field returns Unicode, output will be
        # overriden.
        output = ""
        for field in self.fields:
            output += field.render()
        return output
