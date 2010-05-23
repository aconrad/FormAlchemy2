#coding: utf-8

from formalchemy2.fields import Field
from formalchemy2.forms import Form


class ConfigForm(Form):
    """The Config form.

    Return a Form-like object whose fields are populated given a
    ConfigParser instance.

    Arguments:
    config -- a ConfigParser instance

    """
    def __init__(self, config, section=None, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)

        self.section = section

        # Populate fields from config options
        for section in config.sections():
            for option, value in config.items(section):
                field_id = "%s-%s" % (section, option)
                field = Field(field_id, label=option, value=value)
                self.append(field)
