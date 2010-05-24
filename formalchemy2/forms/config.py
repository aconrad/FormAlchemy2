#coding: utf-8

from formalchemy2.fields import Field
from formalchemy2.forms import Form


class ConfigForm(Form):
    """The Config form.

    Return a Form-like object whose fields are populated given a
    ConfigParser instance.

    Arguments:
    config -- a ConfigParser instance

    Keyword arguments:
    sections -- an iterable of section names to be included
    default_renderer -- a default renderer to be set to each generated field

    """
    def __init__(self, config, sections=None, default_renderer=None,
                 *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)

        # Put all fields when no section is given
        if sections is None:
            sections = config.sections()

        # Populate fields from config options
        for section in sections:
            for option, value in config.items(section):
                field_id = "%s-%s" % (section, option)
                field = Field(field_id, label=option, value=value, renderer=default_renderer)
                self.append(field)
