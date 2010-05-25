#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput, HiddenInput, Select


class TestTextInputRenderer(TestCase):

    Renderer = TextInput


class TestSelectRenderer(TestCase):

    Renderer = Select

    def test_output(self):
        renderer = self.Renderer()
        choices = [('foo', 'Foo')]
        field = Field('id', choices=choices, renderer=renderer)
        output = field.render()
        assert 'name' in output
        assert 'select' in output
        assert 'option' in output
        assert 'foo' in output


class TestHiddenInputRenderer(TestCase):

    Renderer = HiddenInput

    def test_output(self):
        renderer = self.Renderer()
        field = Field('id', renderer=renderer)
        output = field.render()
        assert 'name' in output
        assert 'type=hidden' in output
        assert 'value' not in output
        field = Field('id', value='PUT', renderer=renderer)
        output = field.render()
        assert 'value' in output
