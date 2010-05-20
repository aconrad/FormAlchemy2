#coding: utf-8

from formalchemy2.registry import RendererRegistry
from formalchemy2.renderers import html5

modules = [html5]

# Register renderers
for module in modules:
    for cls_name in module.__all__:
        cls = getattr(html5, cls_name)
        RendererRegistry.register(cls)
