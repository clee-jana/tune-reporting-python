"""
Tune Mangement API '/advertiser/stats/'
====================================================
"""
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
#  Python 2.7 and 3.0
#
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-10 17:11:05 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

from tune_reporting.base import (
    ReportsActualsEndpointBase
)


#  /advertiser/stats
#  @example example_reports_actuals.py
class AdvertiserReportActuals(ReportsActualsEndpointBase):
    """
    Tune Management API endpoint '/advertiser/stats/'
    """

    ## The constructor.
    #
    #  @param str   api_key         MobileAppTracking API Key.
    #  @param bool  validate_fields Validate fields used by actions'
    #
    def __init__(self,
                 api_key,
                 validate_fields=False):
        """The constructor.

            :param str api_key:             MobileAppTracking API Key.
            :param bool validate_fields:    Validate fields used by actions.
        """
        ReportsActualsEndpointBase.__init__(
            self,
            "advertiser/stats",
            api_key,
            True,
            True,
            validate_fields
        )

        self.fields_recommended = [
            "site_id",
            "site.name",
            "publisher_id",
            "publisher.name",
            "ad_impressions",
            "ad_impressions_unique",
            "ad_clicks",
            "ad_clicks_unique",
            "paid_installs",
            "paid_installs_assists",
            "non_installs_assists",
            "paid_events",
            "paid_events_assists",
            "non_events_assists",
            "paid_opens",
            "paid_opens_assists",
            "non_opens_assists"
        ]