#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentParser
from logging import DEBUG, INFO, basicConfig

from exchangelib.util import PrettyXmlHandler

from core import main
from utils import valid_date


def cli():
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


if __name__ == '__main__':
    cli()

# vim fileencoding=utf-8
