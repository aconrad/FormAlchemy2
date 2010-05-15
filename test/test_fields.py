#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import *


class TestField(TestCase):

    def test_field(self):
        field = Field('name')
        assert field.id == 'name'

    def test_field_render(self):
        field = Field('name')
        self.assertRaises(NoRendererError, field.render)
