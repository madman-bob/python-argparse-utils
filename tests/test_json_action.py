from argparse import ArgumentParser
from contextlib import redirect_stderr
from io import StringIO
from unittest import TestCase

from argparse_utils import json_action


class TestJSONAction(TestCase):
    def test_basic_json_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=json_action())

        tests = [
            ('[1, 2, 3]', [1, 2, 3]),
            ('{"a": 1, "b": 2}', {"a": 1, "b": 2}),
            ('null', None),
            ('{"nested": {"json": ["obj"]}}', {"nested": {"json": ["obj"]}})
        ]

        for json_str, json_obj in tests:
            with self.subTest(json_obj=json_obj):
                args = parser.parse_args(['-a', json_str])
                self.assertEqual(args.a, json_obj)

    def test_invalid_json(self):
        invalid_json_objects = [
            'json',
            'not json',
            '{"incomplete": "json"'
        ]

        parser = ArgumentParser()
        parser.add_argument('-a', action=json_action())

        for invalid_json in invalid_json_objects:
            with self.subTest(invalid_json=invalid_json):
                error_message = StringIO()

                with redirect_stderr(error_message), self.assertRaises(SystemExit):
                    parser.parse_args(['-a', invalid_json])

                self.assertRegex(error_message.getvalue(), "invalid json: '{}'".format(invalid_json))
