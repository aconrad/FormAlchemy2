#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError, NoValidatorError


class DummyRenderer(BaseRenderer):
    """A dummy renderer."""
    def render(self, field):
        return ""


class TestField(TestCase):

    def test_field_init(self):
        field = Field('id')
        assert field.id == 'id'
        assert field.label == 'id'
        assert field.value == None
        assert field.choices == None
        assert field.renderer == None
        assert field.prettifyer == None
        assert field.required == False
        assert field.hidden == False

    def test_field_init_with_args(self):
        renderer = DummyRenderer()
        prettifyer = lambda x: x.capitalize()
        menu = (
            ('C6', '2 sushis, 6 california, 5 brochettes, riz'),
            ('N', 'shirashi saumon'),
        )
        field = Field('id', label='label', value='value', choices=menu,
                      renderer=renderer, prettifyer=prettifyer, required=True,
                      hidden=True)
        assert field.id == 'id'
        assert field.label == 'Label'
        assert field.value == 'value'
        assert field.choices == menu
        assert field.renderer == renderer
        assert field.prettifyer == prettifyer
        assert field.required == True
        assert field.hidden == True

    def test_field_render_with_no_renderer(self):
        field = Field('id')
        self.assertRaises(NoRendererError, field.render)

    def test_field_render_with_renderer(self):
        renderer = DummyRenderer()
        field = Field('id', renderer=renderer)
        output = field.render()
        assert isinstance(output, basestring)

    def test_field_set_renderer(self):
        renderer = DummyRenderer()
        field = Field('id', renderer=renderer)
        assert field.renderer
        field = Field('id')
        assert not field.renderer
        field.renderer = renderer
        assert field.renderer

    def test_field_validator_no_validator(self):
        field = Field('id')
        self.assertRaises(NoValidatorError, field.validate)

    def test_field_validator_fail(self):
        validator = int
        field = Field('id', value='a', validator=validator)
        self.assertRaises(ValueError, field.validate)

    def test_field_validator_success(self):
        validator = int
        field = Field('id', value='10', validator=validator)
        field.validate()
        assert field.value == 10

    def test_field_none_value_validation(self):
        validator = int
        field = Field('id', validator=validator)
        self.assertRaises(TypeError, field.validate)
        assert field.value is None

    def test_field_prettifyer(self):
        prettifyer = lambda x: x.replace('_', ' ').capitalize()
        field = Field('some_id', prettifyer=prettifyer)
        field.label == 'Some id'
