#coding: utf-8
from mako.template import Template

from formalchemy2.renderers import Renderer


TEXT_INPUT = u"""\
<label for=${field.id}>${field.label}</label>
% if field.value:
<input id=${field.id} type=text value="${field.value}"/>
% else:
<input id=${field.id} type=text/>
% endif
"""


class TextInput(Renderer):

    group = u'html5'
    name = u'text_input'

    _template = Template(TEXT_INPUT)

    def render(self, field):
        output = self._template.render_unicode(field=field)
        if self.encoding is None:
            return output
        return output.encode(self.encoding)
