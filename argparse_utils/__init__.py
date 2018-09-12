from argparse import ArgumentParser

from argparse_utils.datetime import datetime_action, date_action, time_action, timedelta_action
from argparse_utils.json import json_action
from argparse_utils.mapping import mapping_action

__version__ = "1.1.0"

__all__ = [
    "ArgumentParser",
    "datetime_action", "date_action", "time_action", "timedelta_action",
    "json_action",
    "mapping_action", "enum_action"
]


def enum_action(enum_class):
    return mapping_action(enum_class.__members__)
