from argparse import ArgumentTypeError
from datetime import datetime

from argparse_utils.store_mapped_action import StoreMappedAction

__all__ = ["datetime_action", "date_action", "time_action"]


def datetime_action(fmt='%Y-%m-%dT%H:%M:%S'):
    class StoreDateTimeAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                raise ArgumentTypeError("invalid datetime: '{}' (accepted format: {})".format(value, fmt))

    return StoreDateTimeAction


def date_action(fmt='%Y-%m-%d'):
    class StoreDateAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                raise ArgumentTypeError("invalid date: '{}' (accepted format: {})".format(value, fmt))

    return StoreDateAction


def time_action(fmt='%H:%M:%S'):
    class StoreTimeAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt).time()
            except ValueError:
                raise ArgumentTypeError("invalid time: '{}' (accepted format: {})".format(value, fmt))

    return StoreTimeAction
