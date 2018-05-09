#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentParser
from logging import DEBUG, INFO, basicConfig, getLogger

from exchangelib.util import PrettyXmlHandler

import japandas as jpd
import pandas as pd

from exo_app.event import Event


def _next_bday():
    """Return next business day."""
    calendar = jpd.JapaneseHolidayCalendar()
    cday = pd.offsets.CDay(calendar=calendar)
    return (pd.to_datetime('today') + cday)


def main():
    eev = Event()
    eev.show(
        start=_next_bday(),
        end=_next_bday(),
    )


if __name__ == "__main__":
    log = getLogger(__name__)
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        help="debug mode",
        action="store_true"
    )
    args = parser.parse_args()
    if args.debug:
        basicConfig(level=DEBUG, handlers=[PrettyXmlHandler()])
    else:
        basicConfig(level=INFO)
    main()

# vim fileencoding=utf-8
