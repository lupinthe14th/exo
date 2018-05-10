#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentParser, ArgumentTypeError
from logging import DEBUG, INFO, basicConfig, getLogger

from exchangelib.util import PrettyXmlHandler

import japandas as jpd
import pandas as pd
import pandas.tseries.offsets as offsets

from exo_app.event import Event


def _next_bday():
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


def main(date):
    eev = Event()
    if date:
        _date = pd.to_datetime(date)
    else:
        _date = _next_bday()

    log.debug("_date: {}".format(_date))
    eev.show(start_lt=_date + offsets.Day(), end_gt=_date,)


if __name__ == "__main__":
    log = getLogger(__name__)
    parser = ArgumentParser()
    parser.add_argument(
        "--date", help="Date formats. (YYYY-MM-DD)", type=valid_date)
    parser.add_argument("-d", "--debug", help="debug mode",
                        action="store_true")
    args = parser.parse_args()
    if args.debug:
        basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    level=DEBUG, handlers=[PrettyXmlHandler()])
    else:
        basicConfig(level=INFO)
    main(args.date)

# vim fileencoding=utf-8
