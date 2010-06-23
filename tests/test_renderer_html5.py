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
        assert 'required' not in output

    def test_output_with_value(self):
        renderer = self.Renderer()
        field = Field('id', value='foo', renderer=renderer)
        output = field.render()
        assert 'type=text' in output
        assert 'id' in output
        assert 'label' in output
        assert 'name' in output
        assert 'value="foo"' in output

    def test_required_field(self):
        renderer = self.Renderer()
        field = Field('id', value='value', renderer=renderer, required=True)
        output = field.render()
        assert 'required' in output


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

    def test_output_with_required(self):
        renderer = self.Renderer()
        choices = [('foo', 'Foo')]
        # Test not required
        field = Field('id', value='foo', choices=choices, renderer=renderer,
                      required=False)
        output = field.render()
        assert '<option value="" />' in output

        # Test required
        field = Field('id', value='foo', choices=choices, renderer=renderer,
                      required=True)
        output = field.render()
        assert '<option value="" />' not in output


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
