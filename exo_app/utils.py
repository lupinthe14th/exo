#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentTypeError

import japandas as jpd
import pandas as pd


def next_bday():
    """Return next business day."""
    calendar = jpd.JapaneseHolidayCalendar()
    cday = pd.offsets.CDay(calendar=calendar)
    return (pd.to_datetime('today') + cday)


def valid_date(s):
    try:
        return pd.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise ArgumentTypeError(msg)

# vim: set fileencoding=utf-8 :
