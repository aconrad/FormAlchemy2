#coding: utf-8

from unittest import TestCase
from ConfigParser import SafeConfigParser

from formalchemy2.forms.config import Config


class TestConfigForm(TestCase):

    def test_init(self):
        config = SafeConfigParser()
        form = Config(config)
        assert form.config is config
        assert not form.fields

    def test_fields_from_config(self):
        config = SafeConfigParser()
        config.add_section('foo')
        config.set('foo', 'key', 'value')
        form = Config(config)
        assert form.fields, 'No field found in form'
        field = form.fields['foo-key']
        assert field.id == 'foo-key'
        assert field.value == 'value'
        assert field.label == 'key'
