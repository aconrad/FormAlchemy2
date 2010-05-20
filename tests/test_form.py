#coding: utf-8

from unittest import TestCase

from formalchemy2.forms import Form
from formalchemy2.fields import Field
from formalchemy2.exceptions import NoRendererError


class TestForm(TestCase):

    def test_init(self):
        form = Form()
        assert not form.fields

    def test_add_field_to_form(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert form.fields

    def test_form_render(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        self.assertRaises(NoRendererError, form.render)

    def test_form_contains(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert field in form

    def test_for_len(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert len(form) == 1