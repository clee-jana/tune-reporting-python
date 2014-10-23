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

# To install the tune-api-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
from setuptools import setup, find_packages

__version__ = None
with open('tune/version.py') as f:
    exec(f.read())

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

REQUIRES = [
]

setup(
    name='tune',
    version=__version__,
    description='Tune API client library.',
    author='Tune',
    author_email='sdk@tune.com',
    url = "https://github.com/MobileAppTracking/tune-api-python",
    keywords = ["tune", "mobileapptracking", "management api"],
    install_requires = REQUIRES,
    packages = find_packages(),
    package_dir={'tune': 'tune'},
    classifiers= [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    long_description = """\
    Python Tune Helper Library
    ----------------------------

    DESCRIPTION
    The Tune SDK simplifies the process of making calls using the Tune
    Management API.
    The Tune Management API is for advertisers to export data and
    manage their account programmatically.  
    See https://github.com/MobileAppTracking/tune-api-python for
    more information.

    LICENSE The Tune Python Helper Library is distributed under the MIT
    License """
)
