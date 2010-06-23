#coding: utf-8
from mako.template import Template

from formalchemy2.renderers import BaseRenderer

__all__ = [u'find_renderer' u'TextInput', u'Select', u'HiddenInput']


def find_renderer(field):
    """Return a renderer.

    This function attempts to find an appropriate renderer according to
    the field's properties. It will always fallback returning the
    TextInput renderer.

    """
    if field.choices:
        return Select()

    return TextInput()


class MakoRenderer(BaseRenderer):

    def render(self, field):
        return self.template.render_unicode(field=field)


class TextInput(MakoRenderer):

    WIDGET = u"""\
<label for=${field.id}>${field.label}</label>
<input type=text id=${field.id} name=${field.id} \\
% if field.value:
value="${field.value}" \\
% endif
% if field.required:
required \\
% endif
/>
"""

    template = Template(WIDGET)


class HiddenInput(MakoRenderer):

    WIDGET = u"""\
<input type=hidden id=${field.id} name=${field.id} \\
% if field.value:
value="${field.value}" \\
% endif
/>
"""

    template = Template(WIDGET)


class Select(MakoRenderer):

    WIDGET = u"""\
<label for=${field.id}>${field.label}</label>
<select id=${field.id} name=${field.id}>
% for (id, name) in field.choices:
  % if not field.required:
  <option value="" />
  % endif
  % if field.value == id:
  <option value="${id}" selected>${name}</option>
  % else:
  <option value="${id}">${name}</option>
  % endif
% endfor
</select>
"""

    template = Template(WIDGET)
