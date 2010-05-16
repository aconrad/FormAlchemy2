class Form(object):

    def __init__(self):
        self.fields = []

    def append(self, field):
        self.fields.append(field)

    def render(self):
        output = u""
        for field in self.fields:
            output += field.render()
        return output
