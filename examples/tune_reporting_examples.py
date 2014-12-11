#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2014 Tune, Inc
#  All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#  Python 2.7
#
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-10 17:11:05 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

import sys

from example_advertiser_report_actuals import ExampleAdvertiserReportActuals
from example_advertiser_report_cohort import ExampleAdvertiserReportCohort
from example_advertiser_report_retention import ExampleAdvertiserReportRetention

from example_advertiser_report_clicks import ExampleAdvertiserReportClicks
from example_advertiser_report_event_items import ExampleAdvertiserReportEventItems
from example_advertiser_report_events import ExampleAdvertiserReportEvents
from example_advertiser_report_installs import ExampleAdvertiserReportInstalls
from example_advertiser_report_postbacks import ExampleAdvertiserReportPostbacks

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                "Provide API Key to execute Tune Reporting API example {}.".format(sys.argv[0])
                )

        api_key = sys.argv[1]

        example = ExampleAdvertiserReportActuals()
        example.run(api_key)

        example = ExampleAdvertiserReportCohort()
        example.run(api_key)

        example = ExampleAdvertiserReportRetention()
        example.run(api_key)

        example = ExampleAdvertiserReportClicks()
        example.run(api_key)

        example = ExampleAdvertiserReportEventItems()
        example.run(api_key)

        example = ExampleAdvertiserReportEvents()
        example.run(api_key)

        example = ExampleAdvertiserReportInstalls()
        example.run(api_key)

        example = ExampleAdvertiserReportPostbacks()
        example.run(api_key)

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
