#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import getLogger

from exchangelib import Credentials, Account, EWSTimeZone, \
    DELEGATE, Configuration

from .config import ENDPOINT, USERNAME, PASSWORD, VERIFY_SSL

log = getLogger(__name__)
tz = EWSTimeZone.localzone()

if not VERIFY_SSL:
    from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

    import warnings
    warnings.filterwarnings("ignore")


credentials = Credentials(USERNAME, PASSWORD)
config = Configuration(service_endpoint=ENDPOINT,
                       credentials=credentials,)
account = Account(primary_smtp_address=USERNAME,
                  config=config,
                  credentials=credentials,  access_type=DELEGATE,
                  autodiscover=False)

# vim fileencoding=utf-8
