#coding: utf-8

from formalchemy2.exceptions import NoRendererError


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

    @classmethod
    def unregister(cls, renderer_group, renderer_name):
        """Unregister a renderer given its group and name. Or raise NoRendererError."""
        if renderer_group not in cls.renderers:
            raise NoRendererError('Invalid group "%s" for renderer name "%s".' % (renderer_group, renderer_name))

        group = cls.renderers[renderer_group]

        if renderer_name not in group:
            raise NoRendererError('Invalid renderer name "%s" in group "%s".' % (renderer_name, renderer_group))

        del group[renderer_name]

    @classmethod
    def get_renderer(cls, renderer_group, renderer_name):
        """Return a renderer given its group and name. Or raise NoRendererError."""
        if renderer_group not in cls.renderers:
            raise NoRendererError('Unregistered group "%s" for renderer name "%s".' % (renderer_group, renderer_name))

        group = cls.renderers[renderer_group]

        if renderer_name not in group:
            raise NoRendererError('Unregistered renderer name "%s" in group "%s".' % (renderer_name, renderer_group))

        return group[renderer_name]
