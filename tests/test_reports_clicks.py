#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_reports_clicks.py
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
#  @version   0.9.13
#  @link      https://developers.mobileapptracking.com @endlink
#

import unittest
import datetime
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")
try:
    from tune import (
        Clicks,
        TuneSdkException,
        TUNE_FIELDS_RECOMMENDED
        )
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise


class TestReportsClicks(unittest.TestCase):

    def __init__(self, api_key):
        self.__api_key = api_key
        unittest.TestCase.__init__(self)

    def setUp(self):
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal() - 1)
        self.__start_date = "{} 00:00:00".format(yesterday)
        self.__end_date = "{} 23:59:59".format(yesterday)

    def test_ApiKey(self):
        self.assertIsNotNone(self.__api_key)

    def test_Fields(self):
        response = None

        clicks = Clicks(
            self.__api_key,
            validate_fields=True
        )

        response = clicks.fields(TUNE_FIELDS_RECOMMENDED)

        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)

    def test_Count(self):
        response = None

        clicks = Clicks(
            self.__api_key,
            validate_fields=True
        )

        response = clicks.count(
            self.__start_date,
            self.__end_date,
            filter=None,
            response_timezone="America/Los_Angeles"
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)
        self.assertIsInstance(response.data, int)
        self.assertGreaterEqual(response.data, 0)

    def test_Find(self):
        response = None

        clicks = Clicks(
            self.__api_key,
            validate_fields=True
        )

        response = clicks.find(
            self.__start_date,
            self.__end_date,
            filter=None,
            fields=clicks.fields(TUNE_FIELDS_RECOMMENDED),
            limit=5,
            page=None,
            sort={"created": "DESC"},
            response_timezone="America/Los_Angeles"
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.http_code, 200)
        self.assertIsNone(response.errors)
        self.assertIsInstance(response.data, list)
        self.assertLessEqual(len(response.data), 10)

    def test_FindInvalidFields(self):
        try:
            clicks = Clicks(
                self.__api_key,
                validate_fields=True
            )

            clicks.find(
                self.__start_date,
                self.__end_date,
                filter=None,
                fields="foo",
                limit=5,
                page=None,
                sort={"created": "DESC"},
                response_timezone="America/Los_Angeles"
            )
        except TuneSdkException:
            pass
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

    def test_FindInvalidFilter(self):
        try:
            clicks = Clicks(
                self.__api_key,
                validate_fields=True
            )

            clicks.find(
                self.__start_date,
                self.__end_date,
                filter="(foo > 0)",
                fields=clicks.fields(TUNE_FIELDS_RECOMMENDED),
                limit=5,
                page=None,
                sort={"created": "DESC"},
                response_timezone="America/Los_Angeles"
            )
        except TuneSdkException:
            pass
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

    def test_Export(self):
        response = None

        try:
            clicks = Clicks(
                self.__api_key,
                validate_fields=True
            )

            response = clicks.export(
                self.__start_date,
                self.__end_date,
                filter=None,
                fields=clicks.fields(TUNE_FIELDS_RECOMMENDED),
                format="csv",
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
        self.test_FindInvalidFields()
        self.test_FindInvalidFilter()
        self.test_Export()
