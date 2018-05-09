#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from yaml import load
from os.path import join, dirname

with open(join(dirname(__file__), 'settings.yml')) as f:
    settings = load(f)
    ENDPOINT = settings['endpoint']
    USERNAME = settings['username']
    PASSWORD = settings['password']
    VERIFY_SSL = settings.get('verify_ssl', True)

# vim fileencoding=utf-8
