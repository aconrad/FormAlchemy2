#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field, FieldMultiChoice
from formalchemy2.renderers.html5 import TextInput, Select

# relative import
import base_renderers


class TestTextInputRenderer(TestCase, base_renderers.FieldRendererMixin):

    Renderer = TextInput

    def test_field_render(self):
        field = Field('id', label='my field')
        renderer = self.Renderer()
        output = renderer.render(field)
        assert u'label' in output
        assert u'input' in output


class TestSelectRenderer(TestCase, base_renderers.FieldMultiChoiceRendererMixin):

    Renderer = Select

    def test_field_render(self):
        menu = (
            ('C6', '2 sushis, 6 california, 5 brochettes, riz'),
            ('N', 'shirashi saumon'),
        )
        field = FieldMultiChoice('id', choices=menu, label='my menu')
        renderer = self.Renderer()
        output = renderer.render(field)
        assert u'california' in output
        assert u'my menu' in output
