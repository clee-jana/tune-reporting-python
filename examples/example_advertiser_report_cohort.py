#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  example_advertiser_report_cohort.py
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
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-10 17:11:05 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#
#  Cohort Report
#
#  For insight into the value of the users you’ve acquired for your mobile app
#  (e.g. how acquired users are performing over time), you can use our Cohort Report.
#
#  The cohort report analyzes user behavior back to click date time (Cohort by Click)
#  or to install date time (Cohort by Install). Based on whether you are viewing
#  the results endpoint_based on click or install, the data in the report is vastly different.
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

try:
    from tune_reporting import (
        TuneSdkException,
        AdvertiserReportCohort,
        ReportReaderCSV,
        TUNE_FIELDS_RECOMMENDED,
        TUNE_FIELDS_DEFAULT
    )
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise


class ExampleAdvertiserReportCohort(object):
    """Example using Tune Reporting API client."""

    def __init__(self):
        pass

    # Example of running successful requests to Tune MobileAppTracking Management API.
    #
    def run(self, api_key):
        """Run Example\n"""

        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        print("")
        print("==============================================================")
        print("= Tune Reporting API Advertiser Cohort                   =")
        print("==============================================================")

        try:
            week_ago = datetime.date.fromordinal(datetime.date.today().toordinal() - 8)
            yesterday = datetime.date.fromordinal(datetime.date.today().toordinal() - 1)
            start_date = "{} 00:00:00".format(week_ago)
            end_date = "{} 23:59:59".format(yesterday)

            reports_cohort = AdvertiserReportCohort(api_key, validate_fields=True)

            print("")
            print("======================================================")
            print(" Fields of Advertiser Cohort records -- Default.  ")
            print("======================================================")

            response = reports_cohort.fields(TUNE_FIELDS_DEFAULT)
            for field in response:
                print(str(field))

            print("")
            print("======================================================")
            print(" Fields of Advertiser Cohort records -- Recommended.  ")
            print("======================================================")

            response = reports_cohort.fields(TUNE_FIELDS_RECOMMENDED)
            for field in response:
                print(str(field))

            print("")
            print("======================================================")
            print(" Count Advertiser Cohort click records.               ")
            print("======================================================")

            response = reports_cohort.count(
                start_date,
                end_date,
                cohort_type="click",
                cohort_interval="year_day",
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200 or response.errors:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response)))

            print("= TuneManagementResponse:")
            print(str(response))

            print("= Count:")
            print(str(response.data))

            print("")
            print("======================================================")
            print(" Count Advertiser Cohort install records.             ")
            print("======================================================")

            response = reports_cohort.count(
                start_date,
                end_date,
                cohort_type="install",
                cohort_interval="year_day",
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200 or response.errors:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response)))

            print("= TuneManagementResponse:")
            print(str(response))

            print("= TuneManagementResponse:")
            print(str(response))
            print("= Count:")
            print(str(response.data))

            print("")
            print("==========================================================")
            print(" Find Advertiser Cohort 'click/cumulative' records.       ")
            print("==========================================================")

            response = reports_cohort.find(
                start_date,
                end_date,
                cohort_type="click",
                cohort_interval="year_day",
                aggregation_type="cumulative",
                fields= "site_id,site.name,publisher_id,publisher.name,rpi,epi",
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                limit=5,
                page=None,
                sort=None,
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200 or response.errors:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response)))

            print("= TuneManagementResponse:")
            print(str(response))

            print("")
            print("==========================================================")
            print(" Find Advertiser Cohort 'click/cumulative' records.       ")
            print("==========================================================")

            response = reports_cohort.find(
                start_date,
                end_date,
                cohort_type="click",
                cohort_interval="year_day",
                aggregation_type="cumulative",
                fields=reports_cohort.fields(TUNE_FIELDS_RECOMMENDED),
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                limit=5,
                page=None,
                sort=None,
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200 or response.errors:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response)))

            print("= TuneManagementResponse:")
            print(str(response))

            print("")
            print("==========================================================")
            print(" Advertiser Cohort CSV report for export.                 ")
            print("==========================================================")

            response = reports_cohort.export(
                start_date,
                end_date,
                cohort_type="click",
                cohort_interval="year_day",
                aggregation_type="incremental",
                fields=reports_cohort.fields(TUNE_FIELDS_RECOMMENDED),
                group="site_id,publisher_id",
                filter="(publisher_id > 0)",
                response_timezone="America/Los_Angeles"
            )

            if response.http_code != 200 or response.errors:
                raise Exception("Failed: {}: {}".format(response.http_code, str(response)))

            print("= TuneManagementResponse:")
            print(str(response))

            job_id = AdvertiserReportCohort.parse_response_report_job_id(response)

            print("= CSV Job ID: {}".format(job_id))

            print("")
            print("========================================================")
            print(" Fetching Advertiser Cohort CSV report.                 ")
            print("========================================================")

            export_fetch_response = reports_cohort.fetch(
                job_id,
                verbose=True,
                sleep=10
            )

            print("= TuneManagementResponse:")
            print(str(export_fetch_response))

            if export_fetch_response is None:
                print("Exit")
                return

            csv_report_url = AdvertiserReportCohort.parse_response_report_url(export_fetch_response)

            print("= CSV Report URL: {}".format(csv_report_url))

            print("")
            print("========================================================")
            print(" Read Cohort CSV report and pretty print 5 lines.       ")
            print("========================================================")

            csv_report_reader = ReportReaderCSV(csv_report_url)
            csv_report_reader.read()
            csv_report_reader.pretty_print(limit=5)

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
        example = ExampleAdvertiserReportCohort()
        example.run(api_key)
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
