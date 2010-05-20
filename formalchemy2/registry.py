#coding: utf-8


class RendererRegistry(object):
    """This class serves as the registry for renderers.

    The purpose of registering a renderer is still unclear at that
    point. :)

    A renderer can be registered in the renderer registry by calling
    the .register(renderer_cls) method of the registry, passing the
    renderer class as first argument. Each class must have a 'group' and
    a 'name' attribute returning the renderer's group and name as a
    string.

    """
    renderers = {}

    @classmethod
    def register(cls, renderer_cls):
        """Register the given renderer class in the registry."""
        group = renderer_cls.group
        name = renderer_cls.name

        d = cls.renderers.setdefault(group, {})
        d.update({name: renderer_cls})
