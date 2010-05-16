#coding: utf-8


class FormAlchemyError(Exception):
    """Generic error class."""


class RendererError(FormAlchemyError):
    """Generic renderer error."""


class NoRendererError(RendererError):
    """Raised when no renderer is set."""
