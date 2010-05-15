#coding: utf-8

class Field(object):
    def __init__(self, id):
        self.id = id

    def render(self):
        raise NotImplementedError
