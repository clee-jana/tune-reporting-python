"""
Tune Management API endpoint /advertiser/stats/ltv
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## ltv.py
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
#  @package   Tune_PHP_SDK
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.8
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from tune.management.shared import (
    ReportsInsightBase
)

## /advertiser/stats/ltv
#  @example example_cohort.py
class LTV(ReportsInsightBase):
    """Tune Management API controller 'advertiser/stats/ltv'"""

    ## The constructor.
    #
    #  @param str   api_key     MobileAppTracking API Key.
    #  @param bool  validate_fields    Validate fields used by actions.
    #
    def __init__(
        self,
        api_key,
        validate_fields=False
        ):
        ReportsInsightBase.__init__(
            self,
            "advertiser/stats/ltv",
            api_key,
            False,
            True,
            validate_fields
        )

        self.fields_recommended = [
             "site_id"
            ,"site.name"
            ,"publisher_id"
            ,"publisher.name"
            ,"rpi"
            ,"epi"
        ]

    ## Helper function for fetching report document given provided job identifier.
    #
    #  @param string job_id            Job Identifier of report on queue.
    #  @param bool   verbose           For debugging purposes only.
    #  @param int    sleep             How long thread should sleep before
    #                                   next status request.
    #
    #  @return object
    def fetch(
        self,
        job_id,
        verbose=False,
        sleep=10             #
    ):
        return ReportsInsightBase.fetch(
            self,
            "tune.management.api.advertiser.stats.ltv",
            self.__class__.__name__,
            job_id,
            verbose,
            sleep # seconds
        )
