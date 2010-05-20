#coding: utf-8

from unittest import TestCase
from ConfigParser import SafeConfigParser

from formalchemy2.backends.config import Config


class TestConfigBackend(TestCase):

    def test_init(self):
        config = SafeConfigParser()
        form = Config(config)
        assert form.config is config
        assert form.fields == []

    def test_fields_from_config(self):
        config = SafeConfigParser()
        config.add_section('foo')
        config.set('foo', 'key', 'value')
        form = Config(config)
        assert form.fields, 'No field found in form'
        field = form.fields[0]
        assert field.id == 'foo-key'
        assert field.value == 'value'
        assert field.label == 'key'
