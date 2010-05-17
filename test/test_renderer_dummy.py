#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers.dummy import Dummy

# relative import
import test_renderer


class TestDummyRenderer(TestCase, test_renderer.BaseRendererTest):

    renderer = Dummy()

    def test_field_render_with_renderer(self):
        field = Field('name', renderer=self.renderer)
        out = field.render()
        assert field.id in out
