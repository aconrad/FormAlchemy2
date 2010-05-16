#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field, FieldMultiChoice
from formalchemy2.renderer import Renderer
from formalchemy2.exceptions import *


class TestField(TestCase):

    def test_field_id(self):
        field = Field('unique')
        assert field.id == 'unique'

    def test_field_label(self):
        field = Field('unique')
        assert field.label == None
        field = Field('unique', label='label')
        assert field.label == 'label'

    def test_field_value(self):
        field = Field('name')
        assert field.value == None
        field = Field('name', value='value')
        assert field.value == 'value'

    def test_has_renderer(self):
        field = Field('name')
        assert field.has_renderer() is False

    def test_set_renderer(self):
        field = Field('name', renderer=Renderer())
        assert field.has_renderer() is True

    def test_field_render_with_no_renderer(self):
        field = Field('name')
        self.assertRaises(NoRendererError, field.render)

    def test_field_render_with_renderer(self):
        field = Field('name')
        field.renderer = Renderer()
        self.assertRaises(NotImplementedError, field.render)


class TestFieldMultiChoice(TestField):

    def test_field_choices(self):
        menu = (
            ('C6', '2 sushis, 6 california, 5 brochettes, riz'),
            ('N', 'shirashi saumon'),
            )
        field = FieldMultiChoice('name', choices=menu)
        assert field.choices == menu
