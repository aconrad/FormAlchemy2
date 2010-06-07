#coding: utf-8

from formalchemy2.fields import Field
from formalchemy2.forms import Form


SECTION_OPTION_SEP = u"-"


def serialize_id(section, option):
    """Return a config's section and option serialized to some id."""
    return SECTION_OPTION_SEP.join([section, option])


def deserialize_id(id):
    """Return a tuple (section, option) given an id serialized by
    serialize_id().

    """
    return id.split(SECTION_OPTION_SEP, 1)


class ConfigForm(Form):
    """The Config form.

    Return a Form-like object whose fields are populated given a
    ConfigParser instance.

    Arguments:
    config -- a ConfigParser instance

    Keyword arguments:
    sections -- an iterable of section names to be included (default
    None)

    """
    def __init__(self, config, sections=None, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)

        # Put all fields when no section is given
        if sections is None:
            sections = config.sections()

        # Populate fields from config options
        for section in sections:
            for option, value in config.items(section):
                field_id = serialize_id(section, option)
                field = Field(field_id, label=option, value=value)
                self.append(field)

    def sync(self, config):
        """Sync form's data to given config."""
        for field in self:
            section, option = deserialize_id(field.id)
            config.set(section, option, str(field.value))
