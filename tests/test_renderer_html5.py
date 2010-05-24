#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput, HiddenInput, Select


class MixinRendererTest(object):

    def test_render_unicode(self):
        """Test that rendering output is unicode."""
        raise NotImplementedError

    def test_render_encoding(self):
        """Test that rendering output is str."""
        raise NotImplementedError


class TestTextInputRenderer(TestCase, MixinRendererTest):

    Renderer = TextInput

    def test_render_unicode(self):
        field = Field('id', label='my field')
        renderer = self.Renderer()
        output = renderer.render(field)
        assert isinstance(output, unicode)

    def test_render_encoding(self):
        field = Field('id', label='my field')
        renderer = self.Renderer(encoding='utf-8')
        output = renderer.render(field)
        assert isinstance(output, str)


class TestSelectRenderer(TestCase, MixinRendererTest):

    Renderer = Select

    def test_render_unicode(self):
        choices = [('foo', 'Foo')]
        field = Field('id', label='my choices', choices=choices)
        renderer = self.Renderer()
        output = renderer.render(field)
        assert isinstance(output, unicode)

    def test_render_encoding(self):
        choices = [('foo', 'Foo')]
        field = Field('id', label='my choices', choices=choices)
        renderer = self.Renderer(encoding='utf-8')
        output = renderer.render(field)
        assert isinstance(output, str)

    def test_output(self):
        renderer = self.Renderer()
        choices = [('foo', 'Foo')]
        field = Field('id', choices=choices, renderer=renderer)
        output = field.render()
        assert 'name' in output
        assert 'select' in output
        assert 'option' in output
        assert 'foo' in output


class TestHiddenInputRenderer(TestCase, MixinRendererTest):

    Renderer = HiddenInput

    def test_render_unicode(self):
        field = Field('id', label='_method', value='PUT')
        renderer = self.Renderer()
        output = renderer.render(field)
        assert isinstance(output, unicode)

    def test_render_encoding(self):
        field = Field('id', label='_method', value='PUT')
        renderer = self.Renderer(encoding='utf-8')
        output = renderer.render(field)
        assert isinstance(output, str)

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
