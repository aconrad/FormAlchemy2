#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field, FieldMultiChoice
from formalchemy2.renderers import Renderer
from formalchemy2.exceptions import NoRendererError


class TestField(TestCase):

    def test_field_id(self):
        field = Field('id')
        assert field.id == 'unique'

    def test_field_label(self):
        field = Field('id')
        assert field.label == None
        field = Field('id', label='label')
        assert field.label == 'label'

    def test_field_value(self):
        field = Field('id')
        assert field.value == None
        field = Field('id', value='value')
        assert field.value == 'value'

    def test_has_renderer(self):
        field = Field('id')
        assert field.has_renderer() is False

    def test_set_renderer(self):
        field = Field('id', renderer=Renderer())
        assert field.has_renderer() is True

    def test_field_render_with_no_renderer(self):
        field = Field('id')
        self.assertRaises(NoRendererError, field.render)


class TestFieldMultiChoice(TestField):

    def test_field_choices(self):
        # Make sure it breaks when 'choices' is not given.
        self.assertRaises(ValueError, FieldMultiChoice, 'name')

        menu = (
            ('C6', '2 sushis, 6 california, 5 brochettes, riz'),
            ('N', 'shirashi saumon'),
            )
        field = FieldMultiChoice('name', choices=menu)
        assert field.choices == menu
