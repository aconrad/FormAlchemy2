#coding: utf-8

from formalchemy2.fields import Field, FieldMultiChoice


class RendererMixin(object):
    """Mixin class for all renderer tests."""

    def test_render_with_no_field(self):
        renderer = self.Renderer()
        self.assertRaises(TypeError, renderer.render)

    def test_render_unicode(self):
        raise NotImplementedError

    def test_render_with_encoding(self):
        raise NotImplementedError


class FieldRendererMixin(RendererMixin):
    """Mixin class for Field renderer tests.

    This class should be used by all Field renderer tests. The tested renderer
    should be instanciated on the 'renderer' attribute of the class.
    """

    def test_render_unicode(self):
        field = Field('id')
        renderer = self.Renderer()
        assert renderer.encoding is None
        assert isinstance(renderer.render(field), unicode)

    def test_render_with_encoding(self):
        field = Field('id')
        renderer = self.Renderer(encoding='utf-8')
        assert renderer.encoding == 'utf-8'
        assert isinstance(renderer.render(field), str)


class FieldMultiChoiceRendererMixin(RendererMixin):
    """Mixin class for FieldMultiChoice renderer tests.

    This class should be used by all FieldMultiChoice renderer tests. The
    tested renderer should be instanciated on the 'renderer' attribute of the
    class.
    """

    def test_render_unicode(self):
        choices = (('foo', 'Foo'), ('bar', 'Bar'))
        field = FieldMultiChoice('id', choices=choices)
        renderer = self.Renderer()
        assert renderer.encoding is None
        assert isinstance(renderer.render(field), unicode)

    def test_render_with_encoding(self):
        choices = (('foo', 'Foo'), ('bar', 'Bar'))
        field = FieldMultiChoice('id', choices=choices)
        renderer = self.Renderer(encoding='utf-8')
        assert renderer.encoding == 'utf-8'
        assert isinstance(renderer.render(field), str)
