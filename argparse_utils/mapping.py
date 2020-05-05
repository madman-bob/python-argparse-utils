from collections import OrderedDict

from argparse_utils.store_mapped_action import StoreMappedAction, Choice

__all__ = ["mapping_action"]


class MappingChoices:
    def __init__(self, choices, key_normalizer=None):
        if key_normalizer is None:
            key_normalizer = lambda x: x

        self.choices = OrderedDict(
            (key_normalizer(key), value)
            for key, value in choices.items()
        )
        self.key_normalizer = key_normalizer

    def __contains__(self, item):
        return item in self.choices.values()

    def __iter__(self):
        for name, value in self.choices.items():
            yield Choice(value, name)

    def map(self, key):
        key = self.key_normalizer(key)
        return self.choices.get(key, key)


def mapping_action(possible_values, key_normalizer=None):
    class MappingAction(StoreMappedAction):
        @classmethod
        def default_choices(cls):
            return MappingChoices(possible_values, key_normalizer)

        def mapping_function(self, value):
            return self.choices.map(value)

    return MappingAction
