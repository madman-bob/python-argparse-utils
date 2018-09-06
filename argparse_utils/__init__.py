from argparse import ArgumentParser

from argparse_utils.mapping import mapping_action

__version__ = "1.0.0"

__all__ = ["ArgumentParser", "mapping_action", "enum_action"]


def enum_action(enum_class):
    return mapping_action(enum_class.__members__)
