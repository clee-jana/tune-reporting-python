#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (c) 2014 Tune, Inc
#    All rights reserved.
#    
#    Permission is hereby granted, free of charge, to any person obtaining 
#    a copy of this software and associated documentation files 
#    (the "Software"), to deal in the Software without restriction, including 
#    without limitation the rights to use, copy, modify, merge, publish, 
#    distribute, sublicense, and/or sell copies of the Software, and to permit 
#    persons to whom the Software is furnished to do so, subject to the 
#    following conditions: 
#    
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software. 
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
#    DEALINGS IN THE SOFTWARE.
#
#    Python 2.7
#
#    category    Tune
#    package     SDK
#    version     2014-10-01
#    copyright   Copyright (c) 2014, Tune (http://www.tune.com)
#


from __future__ import with_statement
import os
import sys

import tune

from setuptools import setup, find_packages

__version__ = None
with open('tune/version.py') as f:
    exec(f.read())

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

PACKAGES = [
    'tune',
    'tune.shared',
    'tune.management',
    'tune.management.api',
    'tune.management.api.account',
    'tune.management.api.account.users',
    'tune.management.api.advertiser',
    'tune.management.api.advertiser.stats',
    'tune.management.shared',
    'tune.management.shared.reports',
    'tune.management.shared.service'
]

REQUIRES = [
]

FILES = ["tune/*"]

setup(
    name='tune',
    version=__version__,
    description='Tune Helper Library to Management API.',
    author='Tune',
    author_email='sdk@tune.com',
    url = "https://github.com/tune/tune-management-python/",
    keywords = ["tune", "management"],
    install_requires = REQUIRES,
    packages = PACKAGES,
    package_data={'tune': FILES},
    package_dir={'tune': 'tune'},
    license='',
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python Tune Helper Library
    ----------------------------

    DESCRIPTION
    The Tune SDK simplifies the process of making calls using the Tune Management API.
    The Tune Management API is for advertisers to export data and manage their account programmatically.  
    See https://www.github.com/tune/tune-python for more information.

    LICENSE The Tune Python Helper Library is distributed under the MIT
    License """
)
