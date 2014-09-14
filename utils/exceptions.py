# -*- coding: utf-8 -*-

__all__ = (
    'MageError',

    'InstallError',
    'FlagValidationError',
    'MissingRequirements',

    'PluginError',
    'ParamProcessingError',
    'ParamValidationError',

    'NetworkError',
    'ScriptRuntimeError',
)


class MageError(Exception):
    """Default Exception class for Mage installer."""
    def __init__(self, *args, **kwargs):
        super(MageError, self).__init__(*args)
        self.stdout = kwargs.get('stdout', None)
        self.stderr = kwargs.get('stderr', None)


class PuppetError(Exception):
    """Raised when Puppet will have some problems."""


class MissingRequirements(MageError):
    """Raised when minimum install requirements are not met."""
    pass


class InstallError(MageError):
    """Exception for generic errors during setup run."""
    pass


class FlagValidationError(InstallError):
    """Raised when single flag validation fails."""
    pass


class ParamValidationError(InstallError):
    """Raised when parameter value validation fails."""
    pass


class PluginError(MageError):
    pass


class ParamProcessingError(PluginError):
    pass


class NetworkError(MageError):
    """Should be used for Mage's network failures."""
    pass


class ScriptRuntimeError(MageError):
    """
    Raised when utils.ScriptRunner.execute does not end successfully.
    """
    pass


class ExecuteRuntimeError(MageError):
    """Raised when utils.execute does not end successfully."""


class SequenceError(MageError):
    """Exception for errors during setup sequence run."""
    pass
