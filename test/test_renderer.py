#!/bin/env python
#coding: utf-8

from unittest import TestCase

from formalchemy2.renderers import FieldRenderer, FieldMultiChoiceRenderer

# relative import
import base_renderers


class TestFieldRenderer(TestCase, base_renderers.FieldRendererMixin):
    """Test the Renderer class that other renderers will inherit from."""

    Renderer = FieldRenderer


class TestFieldMultiChoiceRenderer(TestCase, base_renderers.FieldMultiChoiceRendererMixin):
    """Test the Renderer class that other renderers will inherit from."""

    Renderer = FieldMultiChoiceRenderer
