#coding: utf-8

from unittest import TestCase

from formalchemy2.forms import Form
from formalchemy2.renderers import Renderer
from formalchemy2.fields import Field


class TestForm(TestCase):

    def test_add_fields_to_form(self):
        form = Form()

        foo = Field('foo')
        form.append(foo)

        bar = Field('bar')
        form.append(bar)

        assert foo in form.fields
        assert bar in form.fields

    def test_form_render(self):
        form = Form()
        renderer = Renderer()

        foo = Field('foo', renderer=renderer)
        form.append(foo)

        bar = Field('bar', renderer=renderer)
        form.append(bar)

        output = form.render()
        assert isinstance(output, basestring)
