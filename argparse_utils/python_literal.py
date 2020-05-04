from argparse import ArgumentTypeError
from ast import literal_eval

from argparse_utils.store_mapped_action import StoreMappedAction

__all__ = ["python_literal_action"]


def python_literal_action():
    class PythonLiteralAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return literal_eval(value)
            except (SyntaxError, ValueError):
                raise ArgumentTypeError("invalid Python literal: '{}'".format(value))

        @classmethod
        def default_help(cls):
            return "Python literal"

    return PythonLiteralAction
