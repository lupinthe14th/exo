#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from exchangelib import EWSDateTime
from logging import getLogger

from . import account, tz

log = getLogger(__name__)


class Event(object):
    """Event Class via Exchange Web Application"""

    def __init__(self):
        pass

    def show(self, start, end):
        _start = tz.localize(EWSDateTime(
            int(start.strftime('%Y')),
            int(start.strftime('%m')),
            int(start.strftime('%d')) + 1,
        ))
        _end = tz.localize(EWSDateTime(
            int(end.strftime('%Y')),
            int(end.strftime('%m')),
            int(end.strftime('%d')),
        ))
        log.debug('start: {}'.format(_start))
        log.debug('end: {}'.format(_end))
        items = account.calendar.filter(
            start__lt=_start,
            end__gt=_end,
        )

        print("{}".format(start.strftime('%Y-%m-%d')))
        for item in items:
            print("- {0}\t{1} - {2}".format(
                item.subject,
                item.start.astimezone(tz).strftime('%H:%M'),
                item.end.astimezone(tz).strftime('%H:%M'),
            ))

# vim fileencoding=utf-8
