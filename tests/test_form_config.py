#coding: utf-8

from unittest import TestCase
from ConfigParser import SafeConfigParser

from formalchemy2.forms.config import ConfigForm
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError


class DummyRenderer(BaseRenderer):
    """A dummy renderer."""
    def render(self, field):
        return ""


class TestConfigForm(TestCase):

    @classmethod
    def setUp(cls):
        # Setup config
        config = SafeConfigParser()
        config.add_section('foo')
        config.set('foo', 'foo_option1', 'foo_value1')
        config.set('foo', 'foo_option2', 'foo_value2')
        config.add_section('bar')
        config.set('bar', 'bar_option1', 'bar_value1')
        config.set('bar', 'bar_option2', 'bar_value2')

        cls.config = config

    @classmethod
    def tearDown(cls):
        del cls.config

    def test_init(self):
        form = ConfigForm(self.config)
        assert form.fields, 'No field found in form'
        field = form.fields['foo-foo_option1']
        assert field.id == 'foo-foo_option1'
        assert field.label == 'foo_option1'
        assert field.value == 'foo_value1'
        assert form.fields['bar-bar_option1']

    def test_init_empty_config(self):
        config = SafeConfigParser()
        form = ConfigForm(config)
        assert not form.fields

    def test_fields_from_config_section(self):
        form = ConfigForm(self.config, sections=['foo'])
        assert form.fields['foo-foo_option1']
        self.assertRaises(KeyError, form.fields.__getitem__, 'bar-bar_option1')

    def test_render_with_no_default_renderer(self):
        form = ConfigForm(self.config)
        self.assertRaises(NoRendererError, form.render)

    def test_render_with_default_renderer(self):
        renderer = DummyRenderer()
        form = ConfigForm(self.config, default_renderer=renderer)
        output = form.render()
        assert isinstance(output, basestring)

    def test_prettifyer(self):
        prettifyer = lambda txt: txt.replace('_', ' ').capitalize()
        form = ConfigForm(self.config, prettifyer=prettifyer)
        field = form.fields['foo-foo_option1']
        assert field.label == 'Foo option1'
