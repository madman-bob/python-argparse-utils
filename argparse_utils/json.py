from argparse import ArgumentTypeError
from json import loads as json_loads

from argparse_utils.store_mapped_action import StoreMappedAction

__all__ = ["json_action"]


def json_action(**kwargs):
    class JSONAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return json_loads(value, **kwargs)
            except ValueError:
                raise ArgumentTypeError("invalid json: '{}'".format(value))

        @classmethod
        def default_help(cls):
            return "json literal"

    return JSONAction
