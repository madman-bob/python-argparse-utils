from argparse import ArgumentParser
from collections import OrderedDict
from contextlib import redirect_stderr
from enum import Enum
from io import StringIO
from unittest import TestCase

from argparse_utils import mapping_action, enum_action


class TestMappingAction(TestCase):
    @property
    def options(self):
        return OrderedDict([
            ('x', 1),
            ('y', 2),
            ('z', object()),
        ])

    class Colours(Enum):
        red = 1
        green = 2
        blue = 3

    def test_basic_mapping_action(self):
        options = self.options

        parser = ArgumentParser()
        parser.add_argument('-a', action=mapping_action(options))

        with self.subTest(arg='x'):
            args = parser.parse_args('-a x'.split())

            self.assertEqual(args.a, 1)

        with self.subTest(arg='z'):
            args = parser.parse_args('-a z'.split())

            self.assertIs(args.a, options['z'])

    def test_mapping_action_multiple_keys(self):
        parser = ArgumentParser()
        parser.add_argument('-a', nargs='*', action=mapping_action(self.options))

        args = parser.parse_args('-a x y'.split())

        self.assertEqual(args.a, [1, 2])

    def test_mapping_action_invalid_key(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=mapping_action(self.options))

        error_message = StringIO()

        with redirect_stderr(error_message), self.assertRaises(SystemExit):
            parser.parse_args('-a w'.split())

        self.assertRegex(error_message.getvalue(), r"invalid choice: 'w' \(choose from x, y, z\)")

    def test_mapping_action_help(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=mapping_action(self.options))

        self.assertRegex(parser.format_help(), r"-a \{x,y,z\}")

    def test_basic_enum_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=enum_action(self.Colours))

        args = parser.parse_args('-a red'.split())

        self.assertEqual(args.a, self.Colours.red)

    def test_enum_action_multiple_keys(self):
        parser = ArgumentParser()
        parser.add_argument('-a', nargs='*', action=enum_action(self.Colours))

        args = parser.parse_args('-a red green'.split())

        self.assertEqual(args.a, [self.Colours.red, self.Colours.green])

    def test_enum_action_invalid_key(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=enum_action(self.Colours))

        error_message = StringIO()

        with redirect_stderr(error_message), self.assertRaises(SystemExit):
            parser.parse_args('-a purple'.split())

        self.assertRegex(error_message.getvalue(), r"invalid choice: 'purple' \(choose from red, green, blue\)")

    def test_enum_action_help(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=enum_action(self.Colours))

        self.assertRegex(parser.format_help(), r"-a \{red,green,blue\}")
