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

    def test_field_label(self):
        field = Field('unique')
        assert field.label == None
        field.label = 'label'
        assert field.label == 'label'

    def test_has_renderer(self):
        field = Field('name')
        assert field.has_renderer() is False

    def test_set_renderer(self):
        field = Field('name')
        field.renderer = Renderer()
        assert field.has_renderer() is True

    def test_field_render_with_no_renderer(self):
        field = Field('name')
        self.assertRaises(NoRendererError, field.render)

    def test_field_render_with_renderer(self):
        field = Field('name')
        field.renderer = Renderer()
        assert isinstance(field.render(), unicode)
