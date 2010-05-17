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

    renderer = None

    def test_render_with_no_field(self):
        self.assertRaises(TypeError, self.renderer.render)


class TestRenderer(TestCase, MixinRendererTest):
    """Test the Renderer class that other renderers will inherit from."""

    renderer = Renderer()

    def test_render_with_field(self):
        field = Field('name', label='label', value='value')
        self.assertRaises(NotImplementedError, self.renderer.render, field)
