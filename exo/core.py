#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from logging import getLogger

import pandas.tseries.offsets as offsets

from .event import Event
from .utils import next_bday

log = getLogger(__name__)


def main(date=None, n=1):
    eev = Event()
    _date = next_bday(day=date, n=n)

    log.debug("_date: {}".format(_date))
    eev.show(start=_date, end=_date + offsets.Day())


# vim: set fileencoding=utf-8 :
