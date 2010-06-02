#coding: utf-8

from unittest import TestCase

from formalchemy2.forms import Form
from formalchemy2.fields import Field
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError, NoValidatorError


class DummyRenderer(BaseRenderer):
    """A dummy renderer."""
    def render(self, field):
        return ""


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

    def test_form_len(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert len(form) == 1

    def test_form_field_iter(self):
        form = Form()
        foo = Field('foo')
        form.append(foo)
        bar = Field('bar')
        form.append(bar)

        fields = (foo, bar)
        for field in form:
            assert field in fields

    def test_form_field_remove(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert field in form
        form.remove(field)
        assert field not in form

    def test_form_validate(self):
        form = Form()
        validator = lambda x: int(x)
        field = Field('foo', validator=validator)
        form.append(field)
        field = Field('bar', validator=validator)
        form.append(field)
        assert form.validate({'foo': '10', 'bar': '3'}) == {'foo': 10, 'bar': 3}

    def test_form_data(self):
        form = Form()
        field = Field('foo', value='Foo')
        form.append(field)
        field = Field('bar', value='Bar')
        form.append(field)
        assert form.data() == {'foo': 'Foo', 'bar': 'Bar'}

    def test_render_with_no_default_renderer(self):
        form = Form()
        field = Field('foo', value='Foo')
        form.append(field)
        self.assertRaises(NoRendererError, form.render)

    def test_render_with_default_renderer(self):
        renderer = DummyRenderer()
        form = Form(default_renderer=renderer)
        field = Field('foo', value='Foo')
        form.append(field)
        output = form.render()
        assert isinstance(output, basestring)
        assert field.renderer is renderer

    def test_validate_with_no_default_validator(self):
        form = Form()
        field = Field('foo')
        form.append(field)
        assert field.validator is None
        self.assertRaises(NoValidatorError, form.validate, {'foo': '10'})

    def test_validate_with_default_validator(self):
        validator = int
        form = Form(default_validator=validator)
        field = Field('foo')
        form.append(field)
        assert field.validator is validator
        assert form.validate({'foo': '10'}) == {'foo': 10}
