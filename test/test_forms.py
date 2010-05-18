#coding: utf-8

from unittest import TestCase

from formalchemy2.forms import Form
from formalchemy2.fields import Field
from formalchemy2.exceptions import NoRendererError


class TestForm(TestCase):

    def test_init(self):
        form = Form()
        assert form.fields == []

    def test_add_field_to_form(self):
        form = Form()

        foo = Field('foo')
        form.append(foo)

        assert foo in form.fields

    def test_form_render(self):
        form = Form()

        foo = Field('foo')
        form.append(foo)

        self.assertRaises(NoRendererError, form.render)
