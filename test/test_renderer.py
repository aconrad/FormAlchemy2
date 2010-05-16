#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers import Renderer


class TestRenderer(TestCase):

    def test_render_with_no_field(self):
        renderer = Renderer()
        self.assertRaises(TypeError, renderer.render)

    def test_render_with_field(self):
        field = Field('name', label='label', value='value')
        renderer = Renderer()
        self.assertRaises(NotImplementedError, renderer.render, field)

    def test_renderer_name(self):
        renderer = Renderer()
        assert renderer.name == 'dummy'
