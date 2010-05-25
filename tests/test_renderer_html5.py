#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput, HiddenInput, Select


class TestTextInputRenderer(TestCase):

    Renderer = TextInput

    def test_output(self):
        renderer = self.Renderer()
        field = Field('id', renderer=renderer)
        output = field.render()
        assert 'type=text' in output
        assert 'id' in output
        assert 'label' in output
        assert 'name' in output
        assert 'value' not in output

    def test_output_with_value(self):
        renderer = self.Renderer()
        field = Field('id', value='foo', renderer=renderer)
        output = field.render()
        assert 'type=text' in output
        assert 'id' in output
        assert 'label' in output
        assert 'name' in output
        assert 'value="foo"' in output


class TestSelectRenderer(TestCase):

    Renderer = Select

    def test_output(self):
        renderer = self.Renderer()
        choices = [('foo', 'Foo')]
        field = Field('id', choices=choices, renderer=renderer)
        output = field.render()
        assert 'name' in output
        assert '<select' in output
        assert 'option' in output
        assert 'foo' in output
        assert 'selected' not in output

    def test_output_with_seclected(self):
        renderer = self.Renderer()
        choices = [('foo', 'Foo')]
        field = Field('id', value='foo', choices=choices, renderer=renderer)
        output = field.render()
        assert 'name' in output
        assert '<select' in output
        assert 'option' in output
        assert 'value="foo" selected' in output


class TestHiddenInputRenderer(TestCase):

    Renderer = HiddenInput

    def test_output(self):
        renderer = self.Renderer()
        field = Field('id', renderer=renderer)
        output = field.render()
        assert 'type=hidden' in output
        assert 'name' in output
        assert 'value' not in output

    def test_output_with_value(self):
        renderer = self.Renderer()
        field = Field('id', value='PUT', renderer=renderer)
        output = field.render()
        assert 'type=hidden' in output
        assert 'name' in output
        assert 'value="PUT"' in output
