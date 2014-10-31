#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reports_logs_endpoint_base.py
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

from .reports_endpoint_base import (
    ReportsEndpointBase
)
from tune.management.shared.endpoints import (
    EndpointBase
)
from tune.management.shared.service import (
    TuneManagementClient
)


#  Base class intended for gathering from Advertiser Stats logs.
##
class ReportsLogsEndpointBase(ReportsEndpointBase):
    """
    Base class intended for gathering from Advertiser Stats logs.
    """

    #  The constructor.
    #
    #  @param string controller                 Tune Management API endpoint
    #                                           name.
    #  @param string api_key                    Tune MobileAppTracking API Key.
    #  @param bool   filter_debug_mode          Remove debug mode information
    #                                           from results.
    #  @param bool   filter_test_profile_id     Remove test profile information
    #                                           from results.
    #  @param bool   validate_fields            Validate fields used by
    #                                           actions' parameters.
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

        ReportsEndpointBase.__init__(
            self,
            controller,
            api_key,
            filter_debug_mode,
            filter_test_profile_id,
            validate_fields
        )

    #  Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string start_date         YYYY-MM-DD HH:MM:SS
    #  @param string end_date           YYYY-MM-DD HH:MM:SS
    #  @param string filter             Filter the results and apply
    #                                   conditions that must be met
    #                                   for records to be included in data.
    #  @param string response_timezone  Setting expected time for data
    def count(
        self,
        start_date=None,
        end_date=None,
        filter=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            EndpointBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            EndpointBase.validate_datetime('end_date', end_date)

        if filter is not None and isinstance(filter, str):
            filter = EndpointBase.validate_filter(self, filter)

        return ReportsEndpointBase.call(
            self,
            action="count",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'filter': filter,
                'response_timezone': response_timezone
            }
        )

    #  Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string start_date             YYYY-MM-DD HH:MM:SS
    #  @param string end_date               YYYY-MM-DD HH:MM:SS
    #  @param string filter                 Filter the results and apply
    #                                       conditions that must be met for
    #                                       records to be included in data.
    #  @param string fields                 No value returns default fields,
    #                                       "*" returns all available fields,
    #                                       or provide specific fields.
    #  @param int    limit                  Limit number of results, default
    #                                       10, 0 shows all.
    #  @param int    page                   Pagination, default 1.
    #  @param dict   sort                   Expression defining sorting found
    #                                       records in result set endpoint_base
    #                                       upon provided fields and its
    #                                       order modifier:
    #                                       (ASC or DESC).
    #  @param string response_timezone      Setting expected timezone for
    #                                       results, default is set in account.
    #  @return object
    def find(
        self,
        start_date=None,
        end_date=None,
        filter=None,
        fields=None,
        limit=None,
        page=None,
        sort=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            EndpointBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            EndpointBase.validate_datetime('end_date', end_date)

        if fields is not None:
            fields = EndpointBase.validate_fields(self, fields)
        if filter is not None:
            filter = EndpointBase.validate_filter(self, filter)
        if sort is not None:
            sort = EndpointBase.validate_sort(self, sort)

        return ReportsEndpointBase.call(
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
                'response_timezone': response_timezone
            }
        )

    #  Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param string start_date            YYYY-MM-DD HH:MM:SS
    #  @param string end_date              YYYY-MM-DD HH:MM:SS
    #  @param string filter                Filter the results and apply
    #                                   conditions that must be met for
    #                                   records to be included in data.
    #  @param string fields                Provide fields if format is 'csv'.
    #  @param string format                Export format: csv, json
    #  @param string response_timezone     Setting expected timezone for
    #                                   results, default is set in account.
    #
    #  @return object
    def export(
        self,
        start_date=None,
        end_date=None,
        filter=None,
        fields=None,
        format=None,
        response_timezone=None
    ):
        if start_date is not None and isinstance(start_date, str):
            EndpointBase.validate_datetime('start_date', start_date)
        if end_date is not None and isinstance(end_date, str):
            EndpointBase.validate_datetime('end_date', end_date)
        if fields is not None:
            fields = EndpointBase.validate_fields(self, fields)
        if filter is not None:
            filter = EndpointBase.validate_filter(self, filter)
        if format is not None:
            EndpointBase.validate_format(format)

        return ReportsEndpointBase.call(
            self,
            action="find_export_queue",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'filter': filter,
                'fields': fields,
                'format': format,
                'response_timezone': response_timezone
            }
        )

    #  Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param string job_id    Provided Job Identifier to reference requested
    #                                   report on export queue.
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

        client = TuneManagementClient(
            controller="export",
            action="download",
            api_key=self.api_key,
            query_string_dict={
                'job_id': job_id
            }
        )

        return client.call()

    #  Helper function for fetching report upon completion.
    #  Starts worker thread for polling export queue.
    #
    #  @param string mod_export_class  Requesting report class for this
    #                                   export.
    #  @param string job_id            Provided Job Identifier to reference
    #                                   requested report on export queue.
    #  @param bool   verbose           Debug purposes only to view progress
    #                                   of job on export queue.
    #  @param int    sleep             Polling delay between querying job
    #                                   status on export queue.
    #
    #  @return object @see Response
    def fetch(
        self,
        job_id,
        verbose=False,
        sleep=10
    ):
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return EndpointBase.fetch(
            self,
            "export",
            "download",
            job_id,
            verbose,
            sleep
        )
