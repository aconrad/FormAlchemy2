#coding: utf-8
from mako.template import Template

from formalchemy2.renderers import Renderer


INPUT_TEXT = u"""\
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

    def render(self, field):
        template = Template(INPUT_TEXT)
        return template.render_unicode(field=field)
