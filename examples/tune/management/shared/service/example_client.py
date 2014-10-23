#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
## example_client.py
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
#  @version   0.9.5
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

import sys
import traceback

from tune.shared import (TuneSdkException, TuneServiceException)
from tune.management.shared import (TuneManagementClient)

class ExampleClient(object):
    """Example using Tune Management API client."""

    def __init__(self):
        pass

    #
    # Example of running successful requests to Tune MobileAppTracking Management API.
    #
    def run(self, api_key):
        """Run Example\n"""

        print(  "======================================")
        print(  "= Tune Management API Client Example =")
        print(  "======================================")
        print(  "    Tune SDK version: {0}".format(
                                TuneManagementClient.version()
                                ))
        print("")

        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        try:
            controller = "account/users"
            action = "find.json"

            query_string_dict = {
                'limit': 5,
                'fields': 'first_name,last_name,email,title'
            }

            client = TuneManagementClient(
                controller,
                action,
                api_key,
                query_string_dict
                )

            if client.call():
                print(client.response)
            else:
                raise RuntimeError("Unexpected failure: {}.".format(client.response))

        except TuneSdkException as exc:
            print("TuneSdkException ({})".format(exc))
            print(self.format_exception(exc.errors))
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("*** print_tb:")
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print("*** print_exception:")
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2, file=sys.stdout)
            print("*** print_exc:")
            traceback.print_exc()

        print(  "======================================")
        print(  "= End Example                        =")
        print(  "======================================")

    @staticmethod
    def format_exception(e):
        "Provide traceback of provided exception."
        exception_list = traceback.format_stack()
        exception_list = exception_list[:-2]
        exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
        exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

        exception_str = "Traceback (most recent call last):\n"
        exception_str += "".join(exception_list)
        # Removing the last \n
        exception_str = exception_str[:-1]

        return exception_str

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError("Provide API Key to examples_execute Tune Management API example {}.".format(sys.argv[0]))
        api_key = sys.argv[1]
        example = ExampleClient()
        example.run(api_key)
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise