#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.renderer import Renderer


class TestRenderer(TestCase):

    def test_renderer(self):
        renderer = Renderer()
        txt = renderer.render()
        assert isinstance(txt, unicode)

    def test_renderer_name(self):
        renderer = Renderer()
        assert renderer.name == 'dummy'
