from abc import ABCMeta
from argparse import Action

__all__ = ["StoreMappedAction"]


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

        if choices is None:
            choices = self.default_choices()

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

    def mapping_function(self, value):
        return value

    def __call__(self, parser, namespace, values, option_string=None):
        if isinstance(values, list):
            values = [self.mapping_function(value) for value in values]
        else:
            values = self.mapping_function(values)

        setattr(namespace, self.dest, values)
