from argparse import ArgumentParser
from contextlib import redirect_stderr
from datetime import date, time, datetime
from io import StringIO
from unittest import TestCase

from argparse_utils import datetime_action, date_action, time_action


class TestDatetimeAction(TestCase):
    def test_basic_datetime_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=datetime_action())

        args = parser.parse_args('-a 2001-02-03T04:05:06'.split())
        self.assertEqual(args.a, datetime(2001, 2, 3, 4, 5, 6))

    def test_datetime_action_formats(self):
        test_datetime = datetime(2001, 2, 3, 4, 5, 6)
        formats = ['%Y-%m-%dT%H:%M:%S', '%d/%m/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S', '%H %Y %S %m %d %M']

        for fmt in formats:
            with self.subTest(fmt=fmt):
                parser = ArgumentParser()
                parser.add_argument('-a', action=datetime_action(fmt))

                args = parser.parse_args(['-a', test_datetime.strftime(fmt)])
                self.assertEqual(args.a, test_datetime)

    def test_invalid_datetime(self):
        invalid_datetimes = ['date', 'not-a-date', 'still not a date', '2001-02-03', '2001-02-03T04:05:60']

        parser = ArgumentParser()
        parser.add_argument('-a', action=datetime_action())

        for invalid_datetime in invalid_datetimes:
            with self.subTest(invalid_datetime=invalid_datetime):
                error_message = StringIO()

                with redirect_stderr(error_message), self.assertRaises(SystemExit):
                    parser.parse_args(['-a', invalid_datetime])

                self.assertRegex(error_message.getvalue(), "invalid datetime: '{}'".format(invalid_datetime))

    def test_basic_date_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=date_action())

        args = parser.parse_args('-a 2001-02-03'.split())
        self.assertEqual(args.a, date(2001, 2, 3))

    def test_date_action_formats(self):
        test_date = date(2001, 2, 3)
        formats = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%m %Y %d']

        for fmt in formats:
            with self.subTest(fmt=fmt):
                parser = ArgumentParser()
                parser.add_argument('-a', action=date_action(fmt))

                args = parser.parse_args(['-a', test_date.strftime(fmt)])
                self.assertEqual(args.a, test_date)

    def test_invalid_date(self):
        invalid_dates = ['date', 'not-a-date', 'still not a date', '2001-02-31']

        parser = ArgumentParser()
        parser.add_argument('-a', action=date_action())

        for invalid_date in invalid_dates:
            with self.subTest(invalid_date=invalid_date):
                error_message = StringIO()

                with redirect_stderr(error_message), self.assertRaises(SystemExit):
                    parser.parse_args(['-a', invalid_date])

                self.assertRegex(error_message.getvalue(), "invalid date: '{}'".format(invalid_date))

    def test_basic_time_action(self):
        parser = ArgumentParser()
        parser.add_argument('-a', action=time_action())

        args = parser.parse_args('-a 04:05:06'.split())
        self.assertEqual(args.a, time(4, 5, 6))

    def test_time_action_formats(self):
        test_time = time(4, 5, 6)
        formats = ['%H:%M:%S', '%S %H %M']

        for fmt in formats:
            with self.subTest(fmt=fmt):
                parser = ArgumentParser()
                parser.add_argument('-a', action=time_action(fmt))

                args = parser.parse_args(['-a', test_time.strftime(fmt)])
                self.assertEqual(args.a, test_time)

    def test_invalid_time(self):
        invalid_times = ['time', 'not:a:time', 'still not a time', '2001-02-03', '04:05:60']

        parser = ArgumentParser()
        parser.add_argument('-a', action=time_action())

        for invalid_time in invalid_times:
            with self.subTest(invalid_time=invalid_time):
                error_message = StringIO()

                with redirect_stderr(error_message), self.assertRaises(SystemExit):
                    parser.parse_args(['-a', invalid_time])

                self.assertRegex(error_message.getvalue(), "invalid time: '{}'".format(invalid_time))
