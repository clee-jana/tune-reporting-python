"""
TUNE Management API '/advertiser/stats/ltv/'
====================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ltv.py
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
#  @version   $Date: 2014-12-21 13:25:20 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

from tune_reporting.base import (
    AdvertiserReportCohortBase
)
from tune_reporting.base.endpoints import (
    TUNE_FIELDS_DEFAULT
)


#  /advertiser/stats/ltv
#  @example example_reports_cohort.py
class AdvertiserReportValue(AdvertiserReportCohortBase):
    """TUNE Management API controller 'advertiser/stats/ltv'"""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportCohortBase.__init__(
            self,
            "advertiser/stats/ltv",
            False,
            True
        )

        self.fields_recommended = [
            "site_id",
            "site.name",
            "publisher_id",
            "publisher.name",
            "rpi",
            "epi"
        ]

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str cohort_type        Cohort types: click, install
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
    #  @param str aggregation_type   Aggregation types:
    #                                   cumulative, incremental
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str fields             Present results using these endpoint's
    #                                   fields.
    #  @param str filter             Apply constraints endpoint_based upon
    #                                   values associated with this endpoint's
    #                                   fields.
    #  @param int limit              Limit number of results, default 10,
    #                                   0 shows all
    #  @param int page               Pagination, default 1.
    #  @param str sort               Sort results using this endpoint's
    #                                   fields.
    #                                   Directions: DESC, ASC
    #  @param str format
    #  @param str response_timezone  Setting expected timezone for
    #                                   results, default is set in account.
    #
    #  @return object @see response.py
    def find(self,
             start_date,
             end_date,
             cohort_type,
             cohort_interval,
             aggregation_type,
             fields,
             group,
             filter=None,
             limit=None,
             page=None,
             sort=None,
             format=None,
             response_timezone=None):
        """Finds all existing records that match filter criteria
        and returns an array of found model data.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:        Cohort types:
                                                click, install
            :param str    cohort_interval:    Cohort intervals:
                                year_day, year_week, year_month, year
            :param str    aggregation_type:   Aggregation types:
                                                cumulative, incremental
            :param str    group:           Group results using this endpoint's
                                            fields.
            :param str    filter:         Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str    fields:         No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param int    limit:          Limit number of results, default
                                            10.
            :param int    page:           Pagination, default 1.
            :param array  sort:           Sort by field name, ASC (default)
                                            or DESC
            :param str    timestamp:      Set to breakdown stats by
                                            timestamp choices: hour, datehour,
                                            date, week, month.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        self._validate_cohort_type(cohort_type)
        self._validate_cohort_interval(cohort_interval)
        self._validate_aggregation_type(aggregation_type)

        if group is None or not group:
            raise ValueError("Parameter 'group' is not defined.")

        group = self._validate_group(group)

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

        return self.call(
            action="find",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'cohort_type': cohort_type,
                'interval': cohort_interval,
                'aggregation_type': aggregation_type,
                'group': group,
                'filter': filter,
                'fields': fields,
                'limit': limit,
                'page': page,
                'sort': sort,
                'format': format,
                'response_timezone': response_timezone
            }
        )

    ## Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str cohort_type        Cohort types: click, install
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
    #  @param str aggregation_type   Aggregation types:
    #                                   cumulative, incremental
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str filter             Apply constraints endpoint_based upon
    #                                   values associated with this endpoint's
    #                                   fields.
    #  @param str fields             Present results using these endpoint's
    #                                   fields.
    #  @param str response_timezone  Setting expected timezone for results,
    #                                   default is set in account.
    #
    #  @return object @see response.py
    #
    def export(self,
               start_date,
               end_date,
               cohort_type,
               cohort_interval,
               aggregation_type,
               fields,
               group,
               filter=None,
               response_timezone=None):
        """Places a job into a queue to generate a report that will contain
        records that match provided filter criteria, and it returns a job
        identifier to be provided to action /export/download.json to download
        completed report.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:        Cohort types - click, install
            :param str    cohort_interval:    Cohort intervals -
                                        year_day, year_week, year_month, year
            :param str    aggregation_type:   Aggregation types -
                                            cumulative, incremental
            :param str    group:          Group results using this endpoint's
                                            fields.
            :param str    fields:        No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param str    filter:        Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        self._validate_cohort_type(cohort_type)
        self._validate_cohort_interval(cohort_interval)
        self._validate_aggregation_type(aggregation_type)

        if group is None or not group:
            raise ValueError("Parameter 'group' is not defined.")
        if fields is None or not fields:
            raise ValueError("Parameter 'fields' is not defined.")

        group = self._validate_group(group)
        fields = self._validate_fields(fields)

        if filter is not None:
            filter = self._validate_filter(filter)

        return self.call(
            action="export",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'cohort_type': cohort_type,
                'interval': cohort_interval,
                'aggregation_type': aggregation_type,
                'filter': filter,
                'fields': fields,
                'group': group,
                'response_timezone': response_timezone
            }
        )

    ## Helper function for fetching report document given provided
    #   job identifier.
    #
    #  @param str job_id            Job Identifier of report on queue.
    #  @param bool   verbose           For debugging purposes only.
    #  @param int    sleep             How long thread should sleep before
    #                                 next status request.
    #
    #  @return object
    def fetch(self,
              job_id,
              verbose=False,
              sleep=10):
        """Helper function for fetching report upon completion.
        Starts worker for polling export queue.

            :param str    job_id:     Provided Job Identifier to reference
                                        requested report on export queue.
            :param bool   verbose:    Debug purposes only to view progress of
                                        job on export queue.
            :param int    sleep:      Polling delay between querying job
                                        status on export queue.
            :return: (TuneManagementResponse)
        """
        return super(AdvertiserReportValue, self)._fetch(
            self.controller,
            "status",
            job_id,
            verbose,
            sleep
        )
