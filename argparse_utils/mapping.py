from argparse_utils.store_mapped_action import StoreMappedAction, Choice

__all__ = ["mapping_action"]


def mapping_action(possible_values):
    class MappingAction(StoreMappedAction):
        @classmethod
        def default_choices(cls):
            return [Choice(value, key) for key, value in possible_values.items()]

        def mapping_function(self, value):
            return possible_values.get(value, value)

    return MappingAction
