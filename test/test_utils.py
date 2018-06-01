#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from argparse import ArgumentTypeError

import pandas as pd
import freezegun

from exo.utils import valid_date, next_bday


class ValidDateTestCase(unittest.TestCase):

    def test_valid_date(self):
        """valid_date関数がpd.datetime型のデータを返すことをテストする
        """
        self.assertEqual(valid_date("2016-01-02"),
                         pd.datetime(2016, 1, 2, 0, 0))

    def test_raises_valid_date(self):
        """valid_date関数がArgumentTypeErrorエラーをraiseすることをテストする
        """
        with self.assertRaises(ArgumentTypeError):
            """format error
            """
            valid_date("20160102")


class NextBusinessDayTestCase(unittest.TestCase):

    @freezegun.freeze_time('2016-01-02')
    def test_today_next_bday(self):
        """next_bday関数に引数を設定しない場合、当日の次営業日を返すことをテストする
        """
        actual = next_bday()
        test = pd.datetime(2016, 1, 4)
        self.assertEqual(actual,
                         test,
                         msg='{0}, {1}'.format(actual, test))

    def test_next_bday(self):
        """next_bday関数に引数を設定した場合、指定日の次営業日を返すことをテストする
        """
        actual = next_bday(day=pd.datetime(2016, 1, 2))
        test = pd.datetime(2016, 1, 4)
        self.assertEqual(actual,
                         test,
                         msg='{0}, {1}'.format(actual, test))


if __name__ == '__main__':
    unittest.main()

# vim: set fileencoding=utf-8 :
