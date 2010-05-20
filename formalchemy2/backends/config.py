#coding: utf-8

from formalchemy2.forms import Form


class Config(Form):
    """The Config form.

    Return a Form-like object whose fields are populated given a
    ConfigParser instance.

    Arguments:
    config -- a ConfigParser instance

    """
    def __init__(self, config, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        self.config = config
