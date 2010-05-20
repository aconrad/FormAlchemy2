#coding: utf-8

from unittest import TestCase
from ConfigParser import SafeConfigParser

from formalchemy2.backends.config import Config


class TestConfigBackend(TestCase):

    def test_init(self):
        config = SafeConfigParser()
        backend = Config(config)
        assert backend.config is config
        assert backend.fields == []
