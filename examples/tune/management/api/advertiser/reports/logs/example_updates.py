#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
## example_updates.py
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
#
# You can use the Logs report in the same way as the Actuals reports, but
# instead of being aggregated by request type, the Logs report contains the
# logs of each individual request (including the logs for Clicks, Installs,
# Updates, Events, Event Items, and Postback URLs). The log data is available
# in real-time, so you can use it for testing, debugging, and ensuring that
# all measurement and attribution continues to operate smoothly. MAT updates
# the Logs report every 1 minute.
#
# https://platform.mobileapptracking.com/#!/Advertiser/Reports/logs?type=updates
#
# Installs API call: stats/updates
#

import sys
import traceback
import datetime

from tune.management.api.advertiser.stats import (Updates)
from tune.management.api import (Export)
from tune.shared import (TuneSdkException, TuneServiceException)

class ExampleUpdates(object):
    """Example using Tune Management API client."""

    def __init__(self):
        pass

    #
    # Example of running successful requests to Tune MobileAppTracking Management API.
    #
    def run(self, api_key):
        """Run Example\n"""

        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        print(  "=============================================================")
        print(  "= Tune Management API Advertiser Reports Logs Updates       =")
        print(  "=============================================================")

        try:
            yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
            start_date  = "{} 00:00:00".format(yesterday)
            end_date    = "{} 23:59:59".format(yesterday)

            updates = Updates(api_key, validate = False)
            
            #response = updates.fields()
            #print("= advertiser/stats/updates fields: {}".format(response))

            print(  "= advertiser/stats/updates/count.json request =")
            response = updates.count(
                    start_date,
                    end_date,
                    filter              = "(status = 'approved')",
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/updates/count.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print("Count: {}\n".format(response.data))

            print(  "= advertiser/stats/updates/find.json request =")
            response = updates.find(
                    start_date,
                    end_date,
                    filter              = "(status = 'approved')",
                    fields              = "created,site.name,status,install_publisher_id,sdk" \
                    ",sdk_version,package_name,app_name" \
                    ",app_version,country.name,region.name" \
                    ",agency.name,site_id,country_id,region_id,agency_id",
                    limit               = 5,
                    page                = None,
                    sort                = {"created": "DESC"},
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/updates/find.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print(  "= advertiser/stats/updates/find_export_queue.json request =")
            response = updates.export(
                    start_date,
                    end_date,
                    filter              = "(status = 'approved')",
                    fields              = "created,site.name,status,install_publisher_id,sdk" \
                    ",sdk_version,package_name,app_name" \
                    ",app_version,country.name,region.name" \
                    ",agency.name,site_id,country_id,region_id,agency_id",
                    format              = "csv",
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/updates/export.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = response.data
            print("Job ID: {}".format(job_id))

            export = Export(api_key)

            print(  "\n= advertiser stats updates status in CSV data format =\n")

            csv_report_reader = export.fetch(job_id, report_format="csv", verbose = True)
            csv_report_reader.read()
            csv_report_reader.pretty_print(limit=5)

            print(  "= advertiser/stats/updates/find_export_queue.json request =")
            response = updates.export(
                    start_date,
                    end_date,
                    filter              = "(status = 'approved')",
                    fields              = "created,site.name,status,install_publisher_id,sdk" \
                    ",sdk_version,package_name,app_name" \
                    ",app_version,country.name,region.name" \
                    ",agency.name,site_id,country_id,region_id,agency_id",
                    format              = "json",
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/updates/export.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = response.data
            print("Job ID: {}".format(job_id))

            export = Export(api_key)

            json_report_reader = export.fetch(job_id, report_format="json", verbose = True)
            json_report_reader.read()
            json_report_reader.pretty_print(limit=5)

        except TuneSdkException as exc:
            print("TuneSdkException ({})".format(exc))
            print(self.format_exception(exc.errors))
            raise
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("*** print_tb:")
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print("*** print_exception:")
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2, file=sys.stdout)
            print("*** print_exc:")
            traceback.print_exc()
            raise

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
            raise ValueError("Provide API Key to execute Tune Management API example {}.".format(sys.argv[0]))
        api_key = sys.argv[1]
        example = ExampleUpdates()
        example.run(api_key)
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
