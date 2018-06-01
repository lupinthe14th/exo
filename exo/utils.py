#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentTypeError

import datetime as dt
import japandas as jpd
import pandas as pd


def next_bday(day=None):
    """Returns the next business day after argument day.
    """
    if day is None:
        day = dt.date.today()
    calendar = jpd.JapaneseHolidayCalendar()
    cday = pd.offsets.CDay(calendar=calendar)
    return (pd.to_datetime(day) + cday)


def valid_date(s):
    try:
        return pd.datetime.strptime(s, "%Y-%m-%d")
    except ValueError as e:
        msg = "Not a valid date: '{0}'\ndetails: {1}.".format(s, e)
        raise ArgumentTypeError(msg)

# vim: set fileencoding=utf-8 :
