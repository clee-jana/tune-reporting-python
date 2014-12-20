#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2014 TUNE, Inc.
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
#  @copyright 2014 TUNE, Inc. (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-19 15:59:09 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

import sys
import unittest

from test_advertiser_report_clicks import TestAdvertiserReportClicks
from test_advertiser_report_event_items import TestAdvertiserReportEventItems
from test_advertiser_report_events import TestAdvertiserReportEvents
from test_advertiser_report_installs import TestAdvertiserReportInstalls
from test_advertiser_report_postbacks import TestAdvertiserReportPostbacks
from test_advertiser_report_actuals import TestAdvertiserReportActuals
from test_advertiser_report_cohort import TestAdvertiserReportCohort
from test_advertiser_report_retention import TestAdvertiserReportRetention


def suite():

    suite = unittest.TestSuite()

    suite.addTest(TestAdvertiserReportClicks())
    suite.addTest(TestAdvertiserReportEventItems())
    suite.addTest(TestAdvertiserReportEvents())
    suite.addTest(TestAdvertiserReportInstalls())
    suite.addTest(TestAdvertiserReportPostbacks())
    suite.addTest(TestAdvertiserReportActuals())
    suite.addTest(TestAdvertiserReportCohort())
    suite.addTest(TestAdvertiserReportRetention())

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run(test_suite)
