from argparse_utils.store_mapped_action import StoreMappedAction

__all__ = ["mapping_action"]


def mapping_action(possible_values):
    class MappingAction(StoreMappedAction):
        @classmethod
        def default_choices(cls):
            return possible_values.keys()

        def mapping_function(self, value):
            return possible_values[value]

    return MappingAction
