"""
Tune Management module containing what is required to service a
request and response from Tune Management API.
"""
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
#    Python 3.0
#
# @category  Tune
# @package   Tune_PHP_SDK
# @author    Jeff Tanner <jefft@tune.com>
# @copyright 2014 Tune (http://www.tune.com)
# @license   http://opensource.org/licenses/MIT The MIT License (MIT)
# @version   0.9.2
# @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from tune.version import __python_required_version__
from tune.shared import python_check_version

python_check_version(__python_required_version__)

from .api import (
    Account,
    Users,
    Advertiser,
    Stats,          # Actuals
    Clicks,         # Logs
    EventItems,     # Logs
    Events,         # Logs
    Installs,       # Logs
    Postbacks,      # Logs
    Updates,        # Logs
    Retention,      # Retention
    LTV,            # Cohort
    Export
)

from .shared import (TuneManagementClient, TuneManagementBase)
