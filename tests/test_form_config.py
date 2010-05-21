#coding: utf-8

from unittest import TestCase
from ConfigParser import SafeConfigParser

from formalchemy2.forms.config import Config


class TestConfigForm(TestCase):

    def test_init(self):
        config = SafeConfigParser()
        form = Config(config)
        assert not form.fields

    def test_fields_from_config(self):
        # Setup config
        config = SafeConfigParser()
        config.add_section('section')
        config.set('section', 'option', 'value')

        # Generate form from config
        form = Config(config)
        assert form.fields, 'No field found in form'
        field = form.fields['section-option']
        assert field.id == 'section-option'
        assert field.label == 'option'
        assert field.value == 'value'
