#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
## example_retention.py
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
#  Retention Report
#
#  The Retention Report shows you how many of your installed users open or engage
#  with your app over time (how users continue to get value from the app).
#  Retention Reports are particularly good for evaluating the quality of users as
#  opposed to the quantity of users (as in the case of user acquisition campaigns).
#  For more information about retention reports, please visit Running Retention
#  Reports.
#
#  Aggregate "cumulative" shows the data compounds or grows over time.
#
#  Aggregate "incremental" shows the rate of change over time.
#
#  Aggregate "cumulative" shows user growth over time by taking into account
#  all of the revenue from the cohort date time to the specified time interval.
#  Because the data is cumulative (values added on top of each other), the graph
#  shows an upward trend as shown in the following screenshot.
#
#  Aggregate "incremental" option only includes the data measured during the specified
#  interval (such as Day, Week, Month, Year, or All Time). Viewing the data
#  incrementally does not appear as impressive as viewing cumulative or aggregated
#  data because it only shows incremental changes (and there is typically a
#  downward trend because of decreases in retention).
#
#  Cohort "clicks" refers to the number of clicks through to the app store to
#  download an app.
#
#  Cohort "installs" refers to the number of downloads of an app
#

import sys
import traceback
import datetime

from tune.management.api.advertiser.stats import Retention
from tune.common import (TuneSdkException, TuneServiceException)

class ExampleRetention(object):
    """Example using Tune Management API client."""

    def __init__(self):
        pass

    ## Example of running successful requests to Tune MobileAppTracking Management API.
    #
    def run(self, api_key):
        """Run Example\n"""

        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        print(  "====================================================")
        print(  "= Tune Management API Advertiser Reports Retention =")
        print(  "====================================================")

        try:
            week_ago = datetime.date.fromordinal(datetime.date.today().toordinal()-8)
            yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
            start_date  = "{} 00:00:00".format(week_ago)
            end_date    = "{} 23:59:59".format(yesterday)

            retention = Retention(api_key, validate = True)
            
            response = retention.fields()
            print("= advertiser/stats/retention fields: {}".format(response))

            print(  "= advertiser/stats/retention/count.json request =")
            response = retention.count(
                    start_date,
                    end_date,
                    cohort_type         = "click",
                    cohort_interval     = "year_day",
                    group               = "ad_network_id",
                    filter              = None,
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/retention/count.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print("Count: {}\n".format(response.data))

            print(  "= advertiser/stats/retention/find.json request =")
            response = retention.find(
                    start_date,
                    end_date,
                    cohort_type         = "install",
                    aggregation_type    = "cumulative",
                    cohort_interval     = "year_day",
                    group               = "ad_network_id,install_publisher_id,country_id",
                    filter              = None,
                    fields              = "installs,opens,ad_network.name" \
                        ",install_publisher.name,country.name" \
                        ",ad_network_id,install_publisher_id,country_id",
                    limit               = 10,
                    page                = None,
                    sort                = {"year_day": "ASC", "install_publisher_id": "ASC"},
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/retention/find.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print(  "= advertiser/stats/retention/export.json request =")
            response = retention.export(
                    start_date,
                    end_date,
                    cohort_type         = "install",
                    aggregation_type    = "cumulative",
                    cohort_interval     = "year_day",
                    group               = "ad_network_id,install_publisher_id,country_id",
                    filter              = None,
                    fields              = "installs,opens,ad_network.name" \
                        ",install_publisher.name,country.name" \
                        ",ad_network_id,install_publisher_id,country_id",
                    response_timezone   = "America/Los_Angeles"
                )
            print("= advertiser/stats/retention/export.json response: {}".format(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = response.data["job_id"]
            print("Job ID: {}".format(job_id))

            print(  "= advertiser stats retention status in CSV data format =")

            csv_report_reader = retention.fetch(job_id, report_format="csv", verbose = True)
            csv_report_reader.read()
            csv_report_reader.pretty_print(limit=5)

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
        example = ExampleRetention()
        example.run(api_key)
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise