#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from logging import getLogger

import pandas as pd
import pandas.tseries.offsets as offsets

from .event import Event
from .utils import next_bday

log = getLogger(__name__)


def main(date):
    eev = Event()
    if date:
        _date = pd.to_datetime(date)
    else:
        _date = next_bday()

    log.debug("_date: {}".format(_date))
    eev.show(start=_date, end=_date + offsets.Day(),)

# vim: set fileencoding=utf-8 :
