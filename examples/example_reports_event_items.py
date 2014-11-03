#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  example_event_items.py
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
#  Python 2.7 and 3.0
#
#  @category  Tune
#  @package   Tune_API_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.13
#  @link      https://developers.mobileapptracking.com @endlink
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
# https://platform.mobileapptracking.com/#!/Advertiser/Reports/logs?type=eventItems
#
# Event Items API call: stats/event/items
#

import sys
import traceback
import datetime

try:
    from tune import (
        TuneSdkException,
        EventItems,
        ReportReaderCSV,
        ReportReaderJSON,
        TUNE_FIELDS_RECOMMENDED
    )
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise


class ExampleReportsEventItems(object):
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

        print("")
        print("==============================================================")
        print("= Tune Management API Advertiser Reports Logs Event Items    =")
        print("==============================================================")

        try:
            yesterday = datetime.date.fromordinal(datetime.date.today().toordinal() - 1)
            start_date = "{} 00:00:00".format(yesterday)
            end_date = "{} 23:59:59".format(yesterday)

            event_items = EventItems(api_key, validate_fields=True)

            print("")
            print("======================================================")
            print(" Fields of Advertiser Logs Event Items records.       ")
            print("======================================================")

            response = event_items.fields(TUNE_FIELDS_RECOMMENDED)
            for field in response:
                print(str(field))

            print("")
            print("======================================================")
            print(" Count Advertiser Logs Event Items records.           ")
            print("======================================================")

            response = event_items.count(
                start_date,
                end_date,
                filter=None,
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print("= TuneManagementResponse:")
            print(str(response))
            print("= Count:")
            print(str(response.data))

            print("")
            print("======================================================")
            print(" Find Advertiser Logs Event Items records.            ")
            print("======================================================")

            response = event_items.find(
                start_date,
                end_date,
                filter=None,
                fields=event_items.fields(TUNE_FIELDS_RECOMMENDED),
                limit=5,
                page=None,
                sort={"created": "DESC"},
                response_timezone="America/Los_Angeles"
            )

            print("= TuneManagementResponse:")
            print(str(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print("")
            print("==========================================================")
            print(" Advertiser Logs Event Items CSV report for export.       ")
            print("==========================================================")

            response = event_items.export(
                start_date,
                end_date,
                filter=None,
                fields=event_items.fields(TUNE_FIELDS_RECOMMENDED),
                format="csv",
                response_timezone="America/Los_Angeles"
            )

            print("= TuneManagementResponse:")
            print(str(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = EventItems.parse_response_report_job_id(response)

            print("= CSV Job ID: {}".format(job_id))

            print("")
            print("=================================================================")
            print(" Fetching Advertiser Logs Event Items CSV report                 ")
            print("=================================================================")

            export_fetch_response = event_items.fetch(
                job_id,
                verbose=True,
                sleep=10
            )

            csv_report_url = EventItems.parse_response_report_url(export_fetch_response)

            print("= CVS Report URL: {}".format(csv_report_url))

            print("")
            print("========================================================")
            print(" Read Event Items CSV report and pretty print 5 lines.  ")
            print("========================================================")

            csv_report_reader = ReportReaderCSV(csv_report_url)
            csv_report_reader.read()
            csv_report_reader.pretty_print(limit=5)

            print("")
            print("===========================================================")
            print(" Advertiser Logs Event Items JSON report for export.       ")
            print("===========================================================")

            response = event_items.export(
                start_date,
                end_date,
                filter=None,
                fields=event_items.fields(TUNE_FIELDS_RECOMMENDED),
                format="json",
                response_timezone="America/Los_Angeles"
            )

            print("= TuneManagementResponse:")
            print(str(response))

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = EventItems.parse_response_report_job_id(response)

            print("= JSON Job ID: {}".format(job_id))

            print("")
            print("========================================================")
            print(" Fetching Advertiser Logs Event Items JSON report.      ")
            print("========================================================")

            export_fetch_response = event_items.fetch(
                job_id,
                verbose=True,
                sleep=10
            )

            print("= TuneManagementResponse:")
            print(str(export_fetch_response))

            if export_fetch_response is None:
                print("Exit")
                return

            json_report_url = EventItems.parse_response_report_url(export_fetch_response)

            print("= JSON Report URL: {}".format(json_report_url))

            print("")
            print("========================================================")
            print(" Read Event Items JSON report and pretty print 5 lines. ")
            print("========================================================")

            json_report_reader = ReportReaderJSON(json_report_url)
            json_report_reader.read()
            json_report_reader.pretty_print(limit=5)

        except TuneSdkException as exc:
            print("TuneSdkException ({})".format(exc))
            print(self.provide_traceback())
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

        print("")
        print("======================================")
        print("= End Example                        =")
        print("======================================")

    @staticmethod
    def provide_traceback():
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
            raise ValueError("{} [api_key].".format(sys.argv[0]))
        api_key = sys.argv[1]
        example = ExampleReportsEventItems()
        example.run(api_key)
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
