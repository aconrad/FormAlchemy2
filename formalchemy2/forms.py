#coding: utf-8


class Form(object):

    def __init__(self):
        self.fields = []

    def append(self, field):
        self.fields.append(field)

    def render(self):
        # Init output as str. If a field returns Unicode, output will be
        # overriden.
        output = ""
        for field in self.fields:
            output += field.render()
        return output
