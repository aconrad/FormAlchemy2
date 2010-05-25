#coding: utf-8
from mako.template import Template

from formalchemy2.renderers import BaseRenderer

__all__ = [u'TextInput', u'Select', u'HiddenInput']


class MakoRenderer(BaseRenderer):

    def render(self, field):
        output = self.template.render_unicode(field=field)
        if self.encoding is None:
            return output
        return output.encode(self.encoding)


class TextInput(MakoRenderer):

    TEMPLATE = u"""\
<label for=${field.id}>${field.label}</label>
% if field.value:
<input id=${field.id} type=text name=${field.id} value="${field.value}"/>
% else:
<input id=${field.id} type=text name=${field.id}/>
% endif
"""

    template = Template(TEMPLATE)


class HiddenInput(MakoRenderer):

    TEMPLATE = u"""\
% if field.value:
<input id=${field.id} type=hidden name=${field.id} value="${field.value}"/>
% else:
<input id=${field.id} type=hidden name=${field.id}/>
% endif
"""

    template = Template(TEMPLATE)


class Select(MakoRenderer):

    TEMPLATE = u"""\
<label for=${field.id}>${field.label}</label>
<select id=${field.id} name=${field.id}>
% for (id, name) in field.choices:
  % if field.value == id:
  <option value="${id}" selected>${name}</option>
  % else:
  <option value="${id}">${name}</option>
  % endif
% endfor
</select>
"""

    template = Template(TEMPLATE)
