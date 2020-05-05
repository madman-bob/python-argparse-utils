from abc import ABCMeta
from argparse import Action

__all__ = ["StoreMappedAction", "Choice"]


class Choice:
    """
    Wrapper class for an Action choice

    Allows you to override the display name for a given Python object
    """

    def __init__(self, value, name=None):
        if name is None:
            name = str(value)

        self.name = name
        self.value = value

    def __repr__(self):
        return self.name


class StoreMappedAction(Action, metaclass=ABCMeta):
    def __init__(
        self,
        option_strings,
        dest,
        nargs=None,
        const=None,
        default=None,
        type=None,
        choices=None,
        required=False,
        help=None,
        metavar=None
    ):

        if type is None:
            type = lambda value: self.mapping_function(value)

        if choices is None:
            choices = self.default_choices()

        if help is None:
            help = self.default_help()

        super().__init__(
            option_strings,
            dest,
            nargs=nargs,
            const=const,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar
        )

    @classmethod
    def default_choices(cls):
        return None

    @classmethod
    def default_help(cls):
        return None

    def mapping_function(self, value):
        return value

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
