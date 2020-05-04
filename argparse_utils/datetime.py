from argparse import ArgumentTypeError
from datetime import datetime

from argparse_utils.store_mapped_action import StoreMappedAction

__all__ = ["datetime_action", "date_action", "time_action", "timedelta_action"]


def datetime_action(fmt='%Y-%m-%dT%H:%M:%S'):
    class StoreDateTimeAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                raise ArgumentTypeError("invalid datetime: '{}' (accepted format: {})".format(value, fmt))

        @classmethod
        def default_help(cls):
            return "datetime (accepted format: {})".format(fmt).replace('%', '%%')

    return StoreDateTimeAction


def date_action(fmt='%Y-%m-%d'):
    class StoreDateAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                raise ArgumentTypeError("invalid date: '{}' (accepted format: {})".format(value, fmt))

        @classmethod
        def default_help(cls):
            return "date (accepted format: {})".format(fmt).replace('%', '%%')

    return StoreDateAction


def time_action(fmt='%H:%M:%S'):
    class StoreTimeAction(StoreMappedAction):
        def mapping_function(self, value):
            try:
                return datetime.strptime(value, fmt).time()
            except ValueError:
                raise ArgumentTypeError("invalid time: '{}' (accepted format: {})".format(value, fmt))

        @classmethod
        def default_help(cls):
            return "time (accepted format: {})".format(fmt).replace('%', '%%')

    return StoreTimeAction


def timedelta_action(fmt='%H:%M:%S'):
    class StoreTimeDeltaAction(StoreMappedAction):
        def mapping_function(self, value):
            start_datetime = datetime(1899, 12, 31) if '%d' in fmt or '%j' in fmt else datetime(1900, 1, 1)

            try:
                return datetime.strptime(value, fmt) - start_datetime
            except ValueError:
                raise ArgumentTypeError("invalid timedelta: '{}' (accepted format: {})".format(value, fmt))

        @classmethod
        def default_help(cls):
            return "timedelta (accepted format: {})".format(fmt).replace('%', '%%')

    return StoreTimeDeltaAction
