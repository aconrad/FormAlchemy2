#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput

# relative import
import test_renderer


class TestTextInputRenderer(TestCase, test_renderer.MixinRendererTest):

    Renderer = TextInput

    def test_field_render(self):
        field = Field('id', label='my field')
        renderer = self.Renderer()
        out = renderer.render(field)
        assert isinstance(out, unicode)
        assert u'label' in out
        assert u'input' in out
