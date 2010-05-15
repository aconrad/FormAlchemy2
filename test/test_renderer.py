#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.renderer import Renderer


class TestRenderer(TestCase):

    def test_renderer(self):
        renderer = Renderer()
        self.assertRaises(NotImplementedError, renderer.render)
