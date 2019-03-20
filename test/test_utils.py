#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from argparse import ArgumentTypeError

import freezegun
import pandas as pd

from exo.utils import next_bday, valid_date


class ValidDateTestCase(unittest.TestCase):
    def test_valid_date(self):
        """valid_date関数がpd.datetime型のデータを返すことをテストする
        """
        self.assertEqual(valid_date("2016-01-02"), pd.datetime(2016, 1, 2, 0, 0))

    def test_raises_valid_date(self):
        """valid_date関数がArgumentTypeErrorエラーをraiseすることをテストする
        """
        with self.assertRaises(ArgumentTypeError):
            """format error
            """
            valid_date("20160102")


class NextBusinessDayTestCase(unittest.TestCase):
    @freezegun.freeze_time("2016-01-02")
    def test_today_next_bday(self):
        """next_bday関数に引数を設定しない場合、当日の次営業日を返すことをテストする
        """
        actual = next_bday()
        test = pd.datetime(2016, 1, 4)
        self.assertEqual(actual, test, msg="{0}, {1}".format(actual, test))

    @freezegun.freeze_time("2016-01-02")
    def test_offsets_next_bday(self):
        """next_bday関数に引数を設定した場合、当日から引数に指定した日数分の営業日を返すことをテストする
        """
        tests = [
            (pd.datetime(2016, 1, 4), 1),
            (pd.datetime(2016, 1, 5), 2),
            (pd.datetime(2015, 12, 31), -1),
            (pd.datetime(2015, 12, 30), -2),
        ]
        for actual, n in tests:
            with self.subTest(actual=actual, n=n):
                expected = next_bday(n=n)
                self.assertEqual(
                    actual,
                    expected,
                    msg="actual: {0}, expected: {1}, n: {2}".format(
                        actual, expected, n
                    ),
                )

    def test_next_bday(self):
        """next_bday関数に引数を設定した場合、指定日の次営業日を返すことをテストする
        """
        actual = next_bday(day=pd.datetime(2016, 1, 2))
        test = pd.datetime(2016, 1, 4)
        self.assertEqual(actual, test, msg="{0}, {1}".format(actual, test))

    def test_day_offsets_next_bday(self):
        """next_bday関数に引数を設定した場合、指定日から指定した日数分の営業日を返すことをテストする
        """
        tests = [
            (pd.datetime(2016, 1, 4), pd.datetime(2016, 1, 2), 1),
            (pd.datetime(2016, 1, 5), pd.datetime(2016, 1, 2), 2),
            (pd.datetime(2015, 12, 31), pd.datetime(2016, 1, 2), -1),
            (pd.datetime(2015, 12, 30), pd.datetime(2016, 1, 2), -2),
        ]
        for actual, day, n in tests:
            with self.subTest(actual=actual, day=day, n=n):
                expected = next_bday(day=day, n=n)
                self.assertEqual(
                    actual,
                    expected,
                    msg="actual: {0}, expected: {1}, day: {2}, n: {3}".format(
                        actual, expected, day, n
                    ),
                )


if __name__ == "__main__":
    unittest.main()

# vim: set fileencoding=utf-8 :
