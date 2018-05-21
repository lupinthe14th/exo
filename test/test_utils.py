#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from argparse import ArgumentTypeError

import pandas as pd

from exo_app.utils import valid_date


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


if __name__ == '__main__':
    unittest.main()

# vim: set fileencoding=utf-8 :
