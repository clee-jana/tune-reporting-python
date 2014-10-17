#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
## unittest_actuals.py
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
#  Python 3.0
#
#  @category  Tune
#  @package   Tune_PHP_SDK
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.2
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#


import unittest
import datetime

from tune.management.api.advertiser import (Stats)

class UnittestTuneManagementApiAdvertiserReportsActuals(unittest.TestCase):

    def __init__(self, api_key):
        self.__api_key = api_key
        unittest.TestCase.__init__(self)

    def setUp(self):
        week_ago = datetime.date.fromordinal(datetime.date.today().toordinal()-8)
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        self.__start_date  = "{} 00:00:00".format(week_ago)
        self.__end_date    = "{} 23:59:59".format(yesterday)

    def test_ApiKey(self):
        self.assertIsNotNone(self.__api_key)

    def test_Count(self):
        response = None

        try:
            stats = Stats(
                self.__api_key,
            )

            response = stats.count(
                    self.__start_date,
                    self.__end_date,
                    filter              = "(publisher_id = 0)",
                    group               = "site_id,publisher_id,campaign_id,site_event_id,match_type,advertiser_sub_publisher_id,advertiser_sub_site_id,advertiser_sub_campaign_id,agency_id,country_id",
                    response_timezone   = "America/Los_Angeles"
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
            stats = Stats(
                self.__api_key,
            )

            response = stats.find(
                    self.__start_date,
                    self.__end_date,
                    filter              = "(publisher_id = 0)",
                    fields              = "site_id,site.name,publisher_id,publisher.name,campaign_id,campaign.name,site_event_id,site_event.name,match_type,advertiser_sub_publisher_id,advertiser_sub_publisher.name,advertiser_sub_site_id,advertiser_sub_site.name,advertiser_sub_campaign_id,advertiser_sub_campaign.name,agency_id,agency.name,ad_clicks,ad_clicks_unique,installs,updates,opens,events,payouts,revenues_usd,country_id,country.name,currency_code",
                    limit               = 10,
                    page                = None,
                    sort                = {"installs": "DESC"},
                    group               = "site_id,publisher_id,campaign_id,site_event_id,match_type,advertiser_sub_publisher_id,advertiser_sub_site_id,advertiser_sub_campaign_id,agency_id,country_id",
                    timestamp           = "datehour",  # Set to breakdown stats by timestamp choices: hour, datehour, date, week, month
                    response_timezone   = "America/Los_Angeles"
                )
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)
        self.assertIsInstance(response.data, list)
        self.assertLessEqual(len(response.data), 10)

    def runTest (self):
        self.test_ApiKey()
        self.test_Count()
        self.test_Find()