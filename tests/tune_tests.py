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
#  @category  Tune
#  @package   Tune_API_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.13
#  @link      https://developers.mobileapptracking.com @endlink
#

import sys
import unittest

from test_client_account_users import TestClientAccountUsers
from test_items_account_users import TestItemsAccountUsers
from test_reports_clicks import TestReportsClicks
from test_reports_event_items import TestReportsEventItems
from test_reports_events import TestReportsEvents
from test_reports_installs import TestReportsInstalls
from test_reports_postbacks import TestReportsPostbacks
from test_reports_actuals import TestReportsActuals
from test_reports_cohort import TestReportsCohort
from test_reports_retention import TestReportsRetention


def suite(api_key):

    suite = unittest.TestSuite()

    suite.addTest(TestClientAccountUsers(api_key))
    suite.addTest(TestItemsAccountUsers(api_key))

    suite.addTest(TestReportsClicks(api_key))
    suite.addTest(TestReportsEventItems(api_key))
    suite.addTest(TestReportsEvents(api_key))
    suite.addTest(TestReportsInstalls(api_key))
    suite.addTest(TestReportsPostbacks(api_key))
    suite.addTest(TestReportsActuals(api_key))
    suite.addTest(TestReportsCohort(api_key))
    suite.addTest(TestReportsRetention(api_key))

    return suite

if __name__ == '__main__':

    try:
        if len(sys.argv) > 1:
            api_key = sys.argv.pop()

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise

    runner = unittest.TextTestRunner()

    test_suite = suite(api_key)

    runner.run(test_suite)
