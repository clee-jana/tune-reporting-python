#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_advertiser_report_cohort_value.py
#
#  Copyright (c) 2014 TUNE, Inc.
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
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 TUNE, Inc. (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-31 17:01:21 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

import datetime
import os.path
import sys
import unittest

try:
    from tune_reporting import (
        AdvertiserReportCohortValue,
        SdkConfig,
        TUNE_FIELDS_RECOMMENDED
        )
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise


class TestAdvertiserReportCohortValue(unittest.TestCase):

    def __init__(self, api_key):
        # Setup SDK Configuration with TUNE MobileAppTracking API Key.
        dirname = os.path.split(__file__)[0]
        dirname = os.path.dirname(dirname)
        filepath = os.path.join(dirname, SdkConfig.SDK_CONFIG_FILENAME)

        abspath = os.path.abspath(filepath)

        sdk_config = SdkConfig(filepath=abspath)
        sdk_config.api_key = api_key
        unittest.TestCase.__init__(self)

    def setUp(self):
        week_ago = datetime.date.fromordinal(datetime.date.today().toordinal() - 8)
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal() - 1)
        self.__start_date = "{} 00:00:00".format(week_ago)
        self.__end_date = "{} 23:59:59".format(yesterday)

    def test_ApiKey(self):
        sdk_config = SdkConfig()
        api_key = sdk_config.api_key

        self.assertIsNotNone(api_key)
        self.assertGreater(len(api_key), 0)
        self.assertNotEqual("API_KEY", api_key)

    def test_Fields(self):
        response = None

        advertiser_report = AdvertiserReportCohortValue()

        response = advertiser_report.fields(TUNE_FIELDS_RECOMMENDED)
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)

    def test_Count(self):
        response = None

        try:
            advertiser_report = AdvertiserReportCohortValue()

            response = advertiser_report.count(
                self.__start_date,
                self.__end_date,
                cohort_type="click",
                cohort_interval="year_day",
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                response_timezone="America/Los_Angeles"
                )
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)
        self.assertIsInstance(response.data, int)
        self.assertGreaterEqual(response.data, 0)

    def test_Find(self):
        response = None

        try:
            advertiser_report = AdvertiserReportCohortValue()

            response = advertiser_report.find(
                self.__start_date,
                self.__end_date,
                cohort_type="click",
                cohort_interval="year_day",
                aggregation_type="cumulative",
                fields=advertiser_report.fields(TUNE_FIELDS_RECOMMENDED),
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                limit=10,
                page=None,
                sort=None,
                response_timezone="America/Los_Angeles"
            )
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)
        self.assertIsInstance(response.data, list)
        self.assertLessEqual(len(response.data), 10)

    def test_Export(self):
        response = None

        try:
            advertiser_report = AdvertiserReportCohortValue()

            response = advertiser_report.export(
                self.__start_date,
                self.__end_date,
                cohort_type="click",
                cohort_interval="year_day",
                aggregation_type="cumulative",
                fields=advertiser_report.fields(TUNE_FIELDS_RECOMMENDED),
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                response_timezone="America/Los_Angeles"
            )
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)

    def runTest(self):
        self.test_ApiKey()
        self.test_Fields()
        self.test_Count()
        self.test_Find()
        self.test_Export()
