#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from yaml import load
import os


def parse():
    try:
        with open(os.path.expanduser("~/.config/exo/config.exo"), "r") as f:
            settings = load(f)
            endpoint = settings.get(
                'endpoint', "https://mail.domain.com/ews/exchange.asmx")
            username = settings.get('username', "iij-taro@iij.ad.jp")
            password = settings.get('password', "topsecret")
            verify_ssl = settings.get('verify_ssl', True)
            return (endpoint, username, password, verify_ssl)
    except OSError as e:
        print("OS error: {}".format(e))


ENDPOINT, USERNAME, PASSWORD, VERIFY_SSL = parse()

# vim fileencoding=utf-8
