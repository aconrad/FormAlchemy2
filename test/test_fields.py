#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import *


class TestField(TestCase):

    def test_field_id(self):
        field = Field('unique')
        assert field.id == 'unique'

    def test_has_renderer(self):
        field = Field('name')
        assert field.has_renderer() is False

    def test_field_render(self):
        field = Field('name')
        self.assertRaises(NoRendererError, field.render)
