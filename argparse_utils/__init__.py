from argparse import ArgumentParser
from collections import OrderedDict

from argparse_utils.datetime import datetime_action, date_action, time_action, timedelta_action
from argparse_utils.json import json_action
from argparse_utils.mapping import mapping_action
from argparse_utils.python_literal import python_literal_action

__version__ = "1.3.0"

__all__ = [
    "ArgumentParser",
    "datetime_action", "date_action", "time_action", "timedelta_action",
    "json_action",
    "mapping_action", "enum_action",
    "python_literal_action"
]


def enum_action(enum_class, key_normalizer=None):
    return mapping_action(OrderedDict(enum_class.__members__), key_normalizer)
