#coding: utf-8

from unittest import TestCase

from formalchemy2.renderers import BaseRenderer


class TestBaseRenderer(TestCase):

    Renderer = BaseRenderer

    def test_render(self):
        renderer = self.Renderer()
        self.assertRaises(NotImplementedError, renderer.render, 'fake field')
