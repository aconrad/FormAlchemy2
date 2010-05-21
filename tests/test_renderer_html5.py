#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.html5 import TextInput, Select


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
