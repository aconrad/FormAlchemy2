#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput


class TestRenderer(TestCase):

    def test_field_render(self):
        field = Field('id', label='foo')
        renderer = TextInput()
        out = renderer.render(field)
        assert isinstance(out, unicode)
        assert u'input' in out
        assert u'label' in out
