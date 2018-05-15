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

    def show(self, start_lt, end_gt):
        _start_lt = tz.localize(EWSDateTime(
            int(start_lt.strftime('%Y')),
            int(start_lt.strftime('%m')),
            int(start_lt.strftime('%d')),
        ))
        _end_gt = tz.localize(EWSDateTime(
            int(end_gt.strftime('%Y')),
            int(end_gt.strftime('%m')),
            int(end_gt.strftime('%d')),
        ))
        log.debug('start_lt: {}'.format(_start_lt))
        log.debug('end_gt: {}'.format(_end_gt))
        items = account.calendar.view(
            start=_end_gt,
            end=_start_lt,
        )

        print("{}".format(end_gt.strftime('%Y-%m-%d')))
        for item in items:
            print("- {0}\t{1} - {2}".format(
                item.subject,
                item.start.astimezone(tz).strftime('%H:%M'),
                item.end.astimezone(tz).strftime('%H:%M'),
            ))

# vim fileencoding=utf-8
