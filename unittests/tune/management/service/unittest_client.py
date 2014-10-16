#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
## example_postback_urls.py
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
#  @version   0.9.1
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#
#
#  PyUnit test for accessing Tune MobileAppTracking Management API's v2/Request() action.
#

import sys
import unittest

from tune.management import (TuneManagementClient)

class UnittestTuneManagementClient(unittest.TestCase):

    __api_key = None

    def __init__(self, api_key):
        self.__api_key = api_key
        unittest.TestCase.__init__(self)

    def test_ApiKey(self):
        self.assertIsNotNone(self.__api_key)


    def test_Count(self):
        """Test account/users/count"""

        response_success = None

        try:
            controller = "account/users"
            action = "count.json"

            client = TuneManagementClient(
                controller,
                action,
                self.__api_key
            )

            response_success = client.call()
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertTrue(response_success)
        self.assertIsNotNone(client.response)
        self.assertTrue(200, client.response.http_code)
        self.assertIsNotNone(client.response.data)
        self.assertGreater(client.response.data, 5)

    def test_Find(self):
        """Test account/users/find"""

        response_success = None

        try:
            controller = "account/users"
            action = "find.json"

            query_data_map = { 'limit': 5, 'fields': 'first_name,last_name,email,title' }

            client = TuneManagementClient(
                controller,
                action,
                self.__api_key,
                query_data_map
            )

            response_success = client.call()
        except Exception as exc:
            self.fail("Exception: {0}".format(exc))

        self.assertTrue(response_success)
        self.assertIsNotNone(client.response)
        self.assertTrue(200, client.response.http_code)
        self.assertIsNotNone(client.response.data)
        self.assertEqual(len(client.response.data), 5)


    def runTest (self):
        self.test_ApiKey()
        self.test_Count()
        self.test_Find()


if __name__ == '__main__':

    try:
        if len(sys.argv) > 1:
            api_key = sys.argv.pop()
            UnittestTuneManagementClient.API_KEY = api_key

        unittest.main()
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
