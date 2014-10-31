#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#
#  Copyright (c) 2014 Tune, Inc
#  All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining
#  a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to permit
#  persons to whom the Software is furnished to do so, subject to the
#  following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#
#  Python 2.7
#
#  @category  Tune
#  @package   Tune_API_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.11
#  @link      https://developers.mobileapptracking.com @endlink
#

from tune.management.shared import (
    ItemsEndpointBase
)
from .stats import (
    Stats,          # Actuals
    Clicks,         # Logs
    EventItems,     # Logs
    Events,         # Logs
    Installs,       # Logs
    Postbacks,      # Logs
    Retention,      # Retention
    LTV             # Cohort
)


#  Endpoint '/advertisers'
#
class Advertiser(ItemsEndpointBase):
    """
    Tune Management API endpoint '/advertiser/'
    """

    #  The constructor.
    #
    #  @param str   api_key     MobileAppTracking API Key.
    #  @param bool  validate_fields    Validate fields used by actions.
    #
    def __init__(
        self,
        api_key,
        validate_fields=False
    ):
        ItemsEndpointBase.__init__(
            self,
            "advertisers",
            api_key,
            validate_fields
        )
