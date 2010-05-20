#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.renderers import BaseRenderer


class TestBaseRenderer(TestCase):

    Renderer = BaseRenderer

    def test_init(self):
        renderer = self.Renderer()
        assert renderer.encoding is None

    def test_init_with_encoding(self):
        renderer = self.Renderer(encoding='utf-8')
        assert renderer.encoding == 'utf-8'

    def test_render(self):
        renderer = self.Renderer()
        self.assertRaises(NotImplementedError, renderer.render, 'fake field')
