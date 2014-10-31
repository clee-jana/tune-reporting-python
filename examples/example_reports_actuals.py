#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  example_actuals.py
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
#  @version   0.9.11
#  @link      https://developers.mobileapptracking.com @endlink
#
#  The Actuals report gives you quick insight into the performance of your apps
#  and advertising partners (publishers). Use this report for reconciliation,
#  testing, debugging, and ensuring that all measurement and attribution continues
#  to operate smoothly. MAT generates this report by aggregating all the logs of
#  each request (MAT updates the report every 5 minutes).
#
#  API call(s) stats/
#

import sys
import traceback
import datetime

try:
    from tune import (
        TuneSdkException,
        Stats,
        Export,
        ReportReaderCSV,
        ReportReaderJSON,
        TUNE_FIELDS_RECOMMENDED
        )
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise


class ExampleReportsActuals(object):
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

        print "========================================================="
        print "= Tune Management API Advertiser Reports Actuals        ="
        print "========================================================="

        try:
            week_ago = datetime.date.fromordinal(datetime.date.today().toordinal() - 8)
            yesterday = datetime.date.fromordinal(datetime.date.today().toordinal() - 1)
            start_date = "{} 00:00:00".format(week_ago)
            end_date = "{} 23:59:59".format(yesterday)

            stats = Stats(api_key, validate_fields=True)

            print ""
            print "======================================================"
            print " Fields of Advertiser Actuals records.                "
            print "======================================================"

            response = stats.fields(TUNE_FIELDS_RECOMMENDED)
            for field in response:
                print str(field)

            print ""
            print "======================================================"
            print " Count Advertiser Actuals records.                    "
            print "======================================================"

            response = stats.count(
                start_date,
                end_date,
                filter="(publisher_id > 0)",
                group="site_id,publisher_id",
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print "= Response:"
            print str(response)
            print "= Count:"
            print str(response.data)

            print ""
            print "======================================================"
            print " Find Advertiser Actuals records.                     "
            print "======================================================"

            response = stats.find(
                start_date,
                end_date,
                filter="(publisher_id > 0)",
                fields=stats.fields(TUNE_FIELDS_RECOMMENDED),
                limit=5,
                page=None,
                sort={"installs": "DESC"},
                group="site_id,publisher_id",
                timestamp="datehour",
                response_timezone="America/Los_Angeles"
            )

            print "= Response:"
            print str(response)

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            print ""
            print "=========================================================="
            print " Request Advertiser Actuals CSV report for export.        "
            print "=========================================================="

            response = stats.export(
                start_date,
                end_date,
                filter="(publisher_id > 0)",
                fields=stats.fields(TUNE_FIELDS_RECOMMENDED),
                format="csv",
                group="site_id,publisher_id",
                timestamp="datehour",
                response_timezone="America/Los_Angeles"
            )

            print "= Response:"
            print str(response)

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = Stats.parse_response_report_job_id(response)

            print "= CSV Job ID: {}".format(job_id)

            print ""
            print "================================================================="
            print " Fetching Advertiser Actuals CSV report                          "
            print "================================================================="

            export = Export(api_key)
            export_fetch_response = export.fetch(
                job_id,
                verbose=True,
                sleep=10
                )

            csv_report_url = Stats.parse_response_report_url(export_fetch_response)
            print "= CVS Report URL: {}".format(csv_report_url)

            print ""
            print "========================================================"
            print " Read Actuals CSV report and pretty print 5 lines.      "
            print "========================================================"

            csv_report_reader = ReportReaderCSV(csv_report_url)
            csv_report_reader.read()
            csv_report_reader.pretty_print(limit=5)

            print ""
            print "==========================================================="
            print " Request Advertiser Actuals JSON report for export.        "
            print "==========================================================="

            response = stats.export(
                start_date,
                end_date,
                filter="(publisher_id > 0)",
                fields=stats.fields(TUNE_FIELDS_RECOMMENDED),
                format="json",
                group="site_id,publisher_id",
                timestamp="datehour",
                response_timezone="America/Los_Angeles"
            )

            print "= Response:"
            print str(response)

            if response.http_code != 200:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response.errors)))

            job_id = Stats.parse_response_report_job_id(response)

            print "= JSON Job ID: {}".format(job_id)

            print "========================================================"
            print " Fetching Advertiser Actuals JSON report                "
            print "========================================================"

            export = Export(api_key)

            export_fetch_response = export.fetch(
                job_id,
                verbose=True,
                sleep=10
                )

            print "= Response:"
            print str(export_fetch_response)

            if export_fetch_response is None:
                print "Exit"
                return

            json_report_url = Stats.parse_response_report_url(export_fetch_response)
            print "= JSON Report URL: {}".format(json_report_url)

            print "========================================================"
            print " Read Actuals JSON report and pretty print 5 lines.     "
            print "========================================================"

            json_report_reader = ReportReaderJSON(json_report_url)
            json_report_reader.read()
            json_report_reader.pretty_print(limit=5)

        except TuneSdkException as exc:
            print "TuneSdkException ({})".format(exc)
            print self.provide_traceback()
            raise
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print "*** print_tb:"
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print "*** print_exception:"
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2, file=sys.stdout)
            print "*** print_exc:"
            traceback.print_exc()
            raise

        print "======================================"
        print "= End Example                        ="
        print "======================================"

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
        example = ExampleReportsActuals()
        example.run(api_key)
    except Exception as exc:
        print "Exception: {0}".format(exc)
        raise
