#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import exo

setup(
    name='exo',
    version=exo.__version__,
    url='https://github.com/lupinthe14th/exo',
    license=exo.__licence__,
    author=exo.__author__,
    author_email='hideosuzuki@ordinarius-fectum.net',
    description='Event check via Exchange Online with python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=list(open('requirement/base.txt').read().splitlines()),
    packages=find_packages(exclude=['test']),
    tests_require=['freezegun'],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'exo=exo.__main__:cli',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        # 'Operating System :: MacOS',
        # 'Operating System :: Unix',
        # 'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ]
)

# vim: set fileencoding=utf-8 :
