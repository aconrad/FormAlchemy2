#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError


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

    def test_field_init_with_args(self):
        renderer = DummyRenderer()
        menu = (
            ('C6', '2 sushis, 6 california, 5 brochettes, riz'),
            ('N', 'shirashi saumon'),
        )
        field = Field('id', label='label', value='value', choices=menu,
                      renderer=renderer)
        assert field.id == 'id'
        assert field.label == 'label'
        assert field.value == 'value'
        assert field.choices == menu
        assert field.renderer == renderer

    def test_field_has_renderer(self):
        field = Field('id')
        assert field.has_renderer() is False

        renderer = DummyRenderer()
        field = Field('id', renderer=renderer)
        assert field.has_renderer() is True

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
        assert field.has_renderer()
        field = Field('id')
        assert not field.has_renderer()
        field.renderer = renderer
        assert field.has_renderer()
