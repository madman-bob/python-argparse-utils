from argparse import Action

__all__ = ["mapping_action"]


def mapping_action(possible_values):
    class MappingAction(Action):
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
                choices = possible_values.keys()

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

        def __call__(self, parser, namespace, values, option_string=None):
            if isinstance(values, list):
                values = [possible_values[value] for value in values]
            else:
                values = possible_values[values]

            setattr(namespace, self.dest, values)

    return MappingAction
