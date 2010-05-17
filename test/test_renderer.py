#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers import Renderer


class MixinRendererTest(object):
    """Mixin class for renderer tests.

    This class should be used by all renderer tests. The tested renderer should
    be instanciated on the 'renderer' attribute of the class.
    """

    def test_render_with_no_field(self):
        renderer = self.Renderer()
        self.assertRaises(TypeError, renderer.render)

    def test_render_with_encoding(self):
        renderer = self.Renderer()
        assert renderer.encoding is None
        renderer = self.Renderer(encoding='utf-8')
        assert renderer.encoding == 'utf-8'


class TestRenderer(TestCase, MixinRendererTest):
    """Test the Renderer class that other renderers will inherit from."""

    Renderer = Renderer

    def test_render_with_field(self):
        field = Field('id', label='label', value='value')
        renderer = self.Renderer()
        assert isinstance(renderer.render(field), unicode)
