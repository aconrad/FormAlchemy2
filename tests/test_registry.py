#coding: utf-8

from unittest import TestCase

from formalchemy2.registry import RendererRegistry
from formalchemy2.renderers import BaseRenderer
from formalchemy2.exceptions import NoRendererError


class DummyRenderer(BaseRenderer):
    """A dummy renderer."""
    group = 'dummy_group'
    name = 'dummy_name'

    def render(self):
        return ""


class TestRendererRegistry(TestCase):

    @classmethod
    def setUp(cls):
        """Register DummyRenderer."""
        RendererRegistry.register(DummyRenderer)

    @classmethod
    def tearDown(cls):
        """Unregister DummyRenderer."""
        group = DummyRenderer.group
        name = DummyRenderer.name
        try:
            RendererRegistry.unregister(group, name)
        except NoRendererError:
            # Some tests may have unregistered DummyRenderer
            pass

    def test_register(self):
        group = DummyRenderer.group
        name = DummyRenderer.name

        assert group in RendererRegistry.renderers
        assert name in RendererRegistry.renderers[group]
        assert RendererRegistry.renderers[group][name] is DummyRenderer

    def test_get_renderer(self):
        group = DummyRenderer.group
        name = DummyRenderer.name
        assert RendererRegistry.get_renderer(group, name) is DummyRenderer

    def test_get_renderer_with_correct_group_and_incorrect_name(self):
        group = DummyRenderer.group
        name = "bar"
        self.assertRaises(NoRendererError, RendererRegistry.get_renderer,
                          group, name)

    def test_get_renderer_with_incorrect_group_and_incorrect_name(self):
        group = "foo"
        name = "bar"
        self.assertRaises(NoRendererError, RendererRegistry.get_renderer,
                          group, name)

    def test_get_unregistered_renderer(self):
        group = "foo"
        name = "bar"
        self.assertRaises(NoRendererError, RendererRegistry.get_renderer,
                          group, name)

    def test_unregister_correct_group_and_incorrect_name(self):
        group = DummyRenderer.group
        name = "bar"
        self.assertRaises(NoRendererError, RendererRegistry.unregister,
                          group, name)

    def test_unregister_incorrect_group_and_incorrect_name(self):
        group = "foo"
        name = "bar"
        self.assertRaises(NoRendererError, RendererRegistry.unregister,
                          group, name)

    def test_unregister_renderer(self):
        group = DummyRenderer.group
        name = DummyRenderer.name
        assert RendererRegistry.unregister(group, name) is None
