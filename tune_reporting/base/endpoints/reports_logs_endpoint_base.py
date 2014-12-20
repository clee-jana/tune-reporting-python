"""
TUNE Management Logs Reports Endpoint base
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reports_logs_endpoint_base.py
#
#  Copyright (c) 2014 TUNE, Inc.
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
#  @copyright 2014 TUNE, Inc. (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-19 11:19:31 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

from .reports_endpoint_base import (
    ReportsEndpointBase
)
from tune_reporting.base.service import (
    TuneManagementClient
)
from tune_reporting.base.endpoints import (
    TUNE_FIELDS_DEFAULT
)


## Base class intended for gathering from Advertiser Stats logs.
##
class ReportsLogsEndpointBase(ReportsEndpointBase):
    """
    Base class intended for gathering from Advertiser Stats logs.
    """

    ## The constructor.
    #
    #  @param str controller                    TUNE Management API endpoint
    #                                           name.
    #  @param bool   filter_debug_mode          Remove debug mode information
    #                                           from results.
    #  @param bool   filter_test_profile_id     Remove test profile information
    #                                           from results.
    def __init__(self,
                 controller,
                 filter_debug_mode,
                 filter_test_profile_id):
        """The constructor.

            :param str controller:          TUNE Management API endpoint name.
            :param bool filter_debug_mode:  Remove debug mode information
                                                    from results.
            :param bool filter_test_profile_id: Remove test profile information
                                                    from results.
        """
        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")

        ReportsEndpointBase.__init__(
            self,
            controller,
            filter_debug_mode,
            filter_test_profile_id
        )

    ## Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str filter             Filter the results and apply
    #                                   conditions that must be met
    #                                   for records to be included in data.
    #  @param str response_timezone  Setting expected time for data
    def count(self,
              start_date,
              end_date,
              filter=None,
              response_timezone=None):
        """Counts all existing records that match filter criteria
        and returns an array of found model data.

            :param str  start_date:    YYYY-MM-DD HH:MM:SS
            :param str  end_date:      YYYY-MM-DD HH:MM:SS
            :param str  filter:        Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        if filter is not None and isinstance(filter, str):
            filter = self._validate_filter(filter)

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

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date             YYYY-MM-DD HH:MM:SS
    #  @param str end_date               YYYY-MM-DD HH:MM:SS
    #  @param str filter                 Filter the results and apply
    #                                       conditions that must be met for
    #                                       records to be included in data.
    #  @param str fields                 No value returns default fields,
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
    #  @param str response_timezone      Setting expected timezone for
    #                                       results, default is set in account.
    #  @return object
    def find(self,
             start_date,
             end_date,
             fields=None,
             filter=None,
             limit=None,
             page=None,
             sort=None,
             response_timezone=None):
        """Finds all existing records that match filter criteria
        and returns an array of found model data.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    filter:        Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str    fields:        No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param int   limit:         Limit number of results, default
                                            10.
            :param int   page:          Pagination, default 1.
            :param array     sort:          Sort by field name, ASC (default)
                                            or DESC
            :param str    timestamp:     Set to breakdown stats by
                                            timestamp choices: hour, datehour,
                                            date, week, month.
            :param str    response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        if filter is not None:
            filter = self._validate_filter(filter)

        if fields is not None:
            fields = self._validate_fields(fields)
        else:
            fields = self.fields(TUNE_FIELDS_DEFAULT)

        if sort is not None:
            sort_result = self._validate_sort(fields, sort)
            sort = sort_result["sort"]
            fields = sort_result["fields"]

        if fields is not None:
            fields = self._validate_fields(fields)

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

    ## Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param str start_date            YYYY-MM-DD HH:MM:SS
    #  @param str end_date              YYYY-MM-DD HH:MM:SS
    #  @param str filter                Filter the results and apply
    #                                   conditions that must be met for
    #                                   records to be included in data.
    #  @param str fields                Provide fields if format is 'csv'.
    #  @param str format                Export format: csv, json
    #  @param str response_timezone     Setting expected timezone for
    #                                   results, default is set in account.
    #
    #  @return object
    def export(self,
               start_date,
               end_date,
               fields=None,
               filter=None,
               format=None,
               response_timezone=None):
        """Places a job into a queue to generate a report that will contain
        records that match provided filter criteria, and it returns a job
        identifier to be provided to action /export/download.json to download
        completed report.

            :param str  start_date:   YYYY-MM-DD HH:MM:SS
            :param str  end_date:     YYYY-MM-DD HH:MM:SS
            :param str  filter:       Filter the results and apply conditions
                                        that must be met for records to be
                                        included in data.
            :param str  fields:       No value returns default fields, "# "
                                        returns all available fields, or
                                        provide specific fields.
            :param str  format:       Export format for downloaded report:
                                        choices: json, csv.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        if fields is not None:
            fields = self._validate_fields(fields)
        if filter is not None:
            filter = self._validate_filter(filter)
        if format is not None:
            self._validate_format(format)

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

    ## Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param str job_id    Provided Job Identifier to reference requested
    #                                   report on export queue.
    def status(self,
               job_id):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            :param str job_id: Export queue identifier
            :return: (TuneManagementResponse)
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

    ## Helper function for fetching report upon completion.
    #
    #  @param str    job_id            Provided Job Identifier to reference
    #                                   requested report on export queue.
    #  @param bool   verbose           Debug purposes only to view progress
    #                                   of job on export queue.
    #  @param int    sleep             Polling delay between querying job
    #                                   status on export queue.
    #
    #  @return object @see TuneManagementResponse
    def fetch(self,
              job_id,
              verbose=False,
              sleep=10):
        """Helper function for fetching report upon completion.

            :param str    job_id:   Provided Job Identifier to reference
                                    requested report on export queue.
            :param bool   verbose:  Debug purposes only to view progress
                                                of job on export queue.
            :param int    sleep:    Polling delay between querying job
                                                status on export queue.
            :return: (TuneManagementResponse)
        """
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return self._fetch(
            "export",
            "download",
            job_id,
            verbose,
            sleep
        )
