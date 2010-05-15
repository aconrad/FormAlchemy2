#coding: utf-8

__all__ = ['FormAlchemyError', 'RendererError']

class FormAlchemyError(Exception):
    """Generic error class."""

class RendererError(FormAlchemyError):
    """Generic renderer error."""
