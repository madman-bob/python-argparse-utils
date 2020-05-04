from argparse import ArgumentParser
from contextlib import redirect_stderr
from io import StringIO
from re import escape as re_escape
from unittest import TestCase

from argparse_utils import python_literal_action


class TestPythonLiteralAction(TestCase):
    def test_basic_python_literal_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=python_literal_action())

        tests = [
            ('[1, 2, 3]', [1, 2, 3]),
            ('{"a": 1, "b": 2}', {"a": 1, "b": 2}),
            ('None', None),
            ('{"nested": {"Python": ["objects"]}}', {"nested": {"Python": ["objects"]}}),
            ('("some", "tuple")', ("some", "tuple")),
            ("'Single quotes'", 'Single quotes'),
        ]

        for literal_str, literal_obj in tests:
            with self.subTest(literal_obj=literal_obj):
                args = parser.parse_args(['-a', literal_str])
                self.assertEqual(args.a, literal_obj)

    def test_invalid_python_literals(self):
        invalid_python_literals = [
            'variable_name',
            'not a literal',
            '{"incomplete": "dict"',
            'null',
            '2 * 3'
        ]

        parser = ArgumentParser()
        parser.add_argument('-a', action=python_literal_action())

        for invalid_python_literal in invalid_python_literals:
            with self.subTest(invalid_python_literal=invalid_python_literal):
                error_message = StringIO()

                with redirect_stderr(error_message), self.assertRaises(SystemExit):
                    parser.parse_args(['-a', invalid_python_literal])

                self.assertRegex(
                    error_message.getvalue(),
                    re_escape("invalid Python literal: '{}'".format(invalid_python_literal))
                )

    def test_python_literal_action_help(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=python_literal_action())

        self.assertRegex(parser.format_help(), "Python literal")
