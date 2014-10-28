"""
Base class for handling all Tune Management API endpoints that deal with reports.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## reports_actuals_base.py
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
#  @version   0.9.9
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from .reports_base import (
    ReportsBase
)
from tune.management.shared.service import (
    TuneManagementBase
)
from tune.management.api.export import (
    Export
)

## Base class intended for gathering from Advertiser Stats actuals.
#
class ReportsActualsBase(ReportsBase):
    """
    Base class intended for gathering from Advertiser Stats actuals.
    """

    ## The constructor.
    #
    #  @param string controller              Tune Management API endpoint name.
    #  @param string api_key                 Tune MobileAppTracking API Key.
    #  @param bool   filter_debug_mode       Remove debug mode information from results.
    #  @param bool   filter_test_profile_id  Remove test profile information from results.
    #  @param bool   validate_fields                Validate fields used by actions' parameters.
    def __init__(
        self,
        controller,
        api_key,
        filter_debug_mode,
        filter_test_profile_id,
        validate_fields=False
    ):
        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # api key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        ReportsBase.__init__(
            self,
            controller,
            api_key,
            filter_debug_mode,
            filter_test_profile_id,
            validate_fields
        )

    ## Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string   start_date        YYYY-MM-DD HH:MM:SS
    #  @param string   end_date          YYYY-MM-DD HH:MM:SS
    #  @param string   group             Group by one of more field names
    #  @param string   filter            Filter the results and apply conditions
    #                                    that must be met for records to be
    #                                    included in data.
    #  @param string   response_timezone Setting expected time for data
    def count(
        self,
        start_date=None,
        end_date=None,
        group=None,
        filter=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            TuneManagementBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            TuneManagementBase.validate_datetime('end_date', end_date)

        if group is not None:
            group = TuneManagementBase.validate_group(self, group)
        if filter is not None:
            filter = TuneManagementBase.validate_filter(self, filter)

        return ReportsBase.call(
            self,
            action="count",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'filter': filter,
                'group': group,
                'response_timezone': response_timezone
            }
        )

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string    start_date        YYYY-MM-DD HH:MM:SS
    #  @param string    end_date          YYYY-MM-DD HH:MM:SS
    #  @param string    filter            Filter the results and apply conditions that
    #                                     must be met for records to be included in data.
    #  @param string    fields            No value returns default fields, "*" returns all
    #                                     available fields, or provide specific fields.
    #  @param integer   limit             Limit number of results, default 10,
    #  @param integer   page              Pagination, default 1.
    #  @param array     sort              Sort by field name, ASC (default) or DESC
    #  @param string    timestamp         Set to breakdown stats by timestamp choices:
    #                                     hour, datehour, date, week, month.
    #  @param string    response_timezone Setting expected timezone for data.
    #                                     Default is set by account.
    #
    #  @return object
    def find(
        self,
        start_date=None,
        end_date=None,
        group=None,
        filter=None,
        fields=None,
        limit=None,
        page=None,
        sort=None,
        timestamp=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            TuneManagementBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            TuneManagementBase.validate_datetime('end_date', end_date)

        if group is not None:
            group = TuneManagementBase.validate_group(self, group)
        if filter is not None:
            filter = TuneManagementBase.validate_filter(self, filter)
        if fields is not None:
            fields = TuneManagementBase.validate_fields(self, fields)

        self.validate_timestamp(timestamp)

        return ReportsBase.call(
            self,
            action="find",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'filter': filter,
                'fields': fields,
                'limit': limit,
                'page': page,
                'sort': sort,
                'group': group,
                'timestamp': timestamp,
                'response_timezone': response_timezone
            }
        )

    ## Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param string start_date        YYYY-MM-DD HH:MM:SS
    #  @param string end_date          YYYY-MM-DD HH:MM:SS
    #  @param string filter            Filter the results and apply conditions that
    #                                  must be met for records to be included in data.
    #  @param string fields            No value returns default fields, "# " returns all
    #                                  available fields, or provide specific fields.
    #  @param string timestamp         Set to breakdown stats by timestamp choices:
    #                                  hour, datehour, date, week, month.
    #  @param string format            Export format for downloaded report: json, csv.
    #  @param string response_timezone Setting expected timezone for data.
    #                                  Default is set by account.
    #
    #  @return object
    def export(
        self,
        start_date=None,
        end_date=None,
        filter=None,
        fields=None,
        group=None,
        timestamp=None,
        format=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            TuneManagementBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            TuneManagementBase.validate_datetime('end_date', end_date)

        if group is not None:
            group = TuneManagementBase.validate_group(self, group)
        if filter is not None:
            filter = TuneManagementBase.validate_filter(self, filter)
        if fields is not None:
            fields = TuneManagementBase.validate_fields(self, fields)

        self.validate_timestamp(timestamp)

        TuneManagementBase.validate_format(format)

        return ReportsBase.call(
            self,
            action="find_export_queue",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'filter': filter,
                'fields': fields,
                'format': format,
                'group': group,
                'timestamp': timestamp,
                'response_timezone': response_timezone
            }
        )

    ## Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param string job_id    Provided Job Identifier to reference requested report on export queue.
    def status(
        self,
        job_id              # Export queue identifier
    ):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            Args:
        """

        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        export = Export(self.api_key)
        return export.download(
            job_id
            )

    ## Helper function for fetching report upon completion.
    #  Starts worker thread for polling export queue.
    #
    #  @param string mod_export_class  Requesting report class for this export.
    #  @param string job_id            Provided Job Identifier to reference
    #                                  requested report on export queue.
    #  @param bool   verbose           Debug purposes only to view progress of
    #                                  job on export queue.
    #  @param int    sleep             Polling delay between querying job
    #                                  status on export queue.
    #
    #  @return object @see report_reader_base.py
    def fetch(
        self,
        job_id,
        verbose=False,
        sleep=10
    ):
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        export = Export(self.api_key)
        return export.fetch(
            job_id,
            verbose=True,
            sleep=10
            )

    ## Helper function for parsing export status response to gather report url.
    #  @param @see Response
    #  @return str Report Url
    @staticmethod
    def parse_response_report_url(
        response
    ):
        return Export.parse_response_report_url(response)

    ## Helper function for parsing export response to gather job identifier.
    #  @param @see Response
    #  @return str Report Url
    @staticmethod
    def parse_response_report_job_id(
        response
    ):
        if not response:
            raise ValueError("Parameter 'response' is not defined.")
        if not response.data:
            raise ValueError("Parameter 'response.data' is not defined.")

        job_id = response.data

        if not job_id or len(job_id) < 1:
            raise Exception("Failed to return Job ID: {}".format(str(response)))

        return job_id

    ## Validate 'timestamp' parameter
    #  @param null|string timestamp
    @staticmethod
    def validate_timestamp(timestamp):
        timestamps = [
            "hour",
            "datehour",
            "date",
            "week",
            "month"
        ]
        if (isinstance(timestamp, str)
            and (timestamp not in timestamps)):
            raise ValueError("Parameter 'timestamp' is invalid: '{}'.".format(
                timestamp
                )
            )
