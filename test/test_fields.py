#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.fields import Field


class TestField(TestCase):

    def test_field(self):
        field = Field('name')
        assert field.id == 'name'

    def test_field_render(self):
        field = Field('name')
        self.assertRaises(NotImplementedError, field.render)
