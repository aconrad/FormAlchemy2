#coding: utf-8

from unittest import TestCase

from formalchemy2.registry import RendererRegistry
from formalchemy2.renderers import BaseRenderer

class TestRendererRegistry(TestCase):

    def test_class(self):
        assert RendererRegistry.renderers == {}

    def test_register(self):

        # Create a dummy renderer class
        class DummyRenderer(BaseRenderer):
            """A dummy renderer."""
            group = 'dummy_group'
            name = 'dummy_name'
            def render(self):
                return ""

        group = DummyRenderer.group
        name = DummyRenderer.name

        # Register DummyRenderer
        RendererRegistry.register(DummyRenderer)
        assert group in RendererRegistry.renderers
        assert name in RendererRegistry.renderers[group]
        assert RendererRegistry.renderers[group][name] is DummyRenderer 
