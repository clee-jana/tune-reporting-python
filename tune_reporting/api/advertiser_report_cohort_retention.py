"""
TUNE Reporting API '/advertiser/stats/retention/'
====================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  retention.py
#
#  Copyright (c) 2015 TUNE, Inc.
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
#  @copyright 2015 TUNE, Inc. (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2015-04-10 11:10:41 $
#  @link      https://developers.mobileapptracking.com @endlink
#

from tune_reporting.base import (
    AdvertiserReportCohortBase
)
from tune_reporting.base.endpoints import (
    TUNE_FIELDS_DEFAULT
)


#  /advertiser/stats/retention
#  @example example_reports_retention.py
class AdvertiserReportCohortRetention(AdvertiserReportCohortBase):
    """
    TUNE Reporting API controller 'advertiser/stats/retention'
    """

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportCohortBase.__init__(
            self,
            "advertiser/stats/retention",
            False,
            True
        )

        self.fields_recommended = [
            "site_id",
            "site.name",
            "install_publisher_id",
            "install_publisher.name",
            "installs",
            "opens"
        ]

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str cohort_type        Cohort types: click, install
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
    #  @param str fields             Present results using these endpoint's
    #                                   fields.
    #  @param str group              Group results using this endpoint's
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
             map_params):
        """Finds all existing records that match filter criteria
        and returns an array of found model data.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:        Cohort types:
                                                click, install
            :param str    cohort_interval:    Cohort intervals:
                                year_day, year_week, year_month, year
            :param str    fields:         No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param str    group:           Group results using this endpoint's
                                            fields.
            :param str    filter:         Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
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
            :return: (TuneServiceResponse)
        """
        map_query_string = {}
        map_query_string = self._validate_datetime(map_params, "start_date", map_query_string)
        map_query_string = self._validate_datetime(map_params, "end_date", map_query_string)

        map_query_string = self._validate_cohort_type(map_params, map_query_string)
        map_query_string = self._validate_cohort_interval(map_params, map_query_string)

        map_query_string = self._validate_group(map_params, map_query_string)

        if "filter" in map_params and map_params["filter"] is not None:
            map_query_string = self._validate_filter(map_params, map_query_string)

        if "fields" not in map_params or map_params["fields"] is None:
          map_params["fields"] = self.fields(TUNE_FIELDS_DEFAULT)
        if "fields" in map_params and map_params["fields"] is not None:
            map_query_string = self._validate_fields(map_params, map_query_string)

        if "limit" in map_params and map_params["limit"] is not None:
            map_query_string = self._validate_limit(map_params, map_query_string)
        if "page" in map_params and map_params["page"] is not None:
            map_query_string = self._validate_page(map_params, map_query_string)

        if "sort" in map_params and map_params["sort"] is not None:
            map_query_string = self._validate_sort(map_params, map_query_string)

        if "response_timezone" in map_params and map_params["response_timezone"] is not None:
            map_query_string["response_timezone"] = map_params["response_timezone"]

        return self.call(
            "find",
            map_query_string
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
    #  @param str fields             Present results using these endpoint's
    #                                   fields.
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str filter             Apply constraints endpoint_based upon
    #                                   values associated with this endpoint's
    #                                   fields.
    #  @param str response_timezone  Setting expected timezone for results,
    #                                   default is set in account.
    #
    #  @return object @see response.py
    #
    def export(self,
               map_params):
        """Places a job into a queue to generate a report that will contain
        records that match provided filter criteria, and it returns a job
        identifier to be provided to action /export/download.json to download
        completed report.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:        Cohort types - click, install
            :param str    cohort_interval:    Cohort intervals -
                                        year_day, year_week, year_month, year
            :param str    fields:        No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param str    group:          Group results using this endpoint's
                                            fields.
            :param str    filter:        Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneServiceResponse)
        """
        map_query_string = {}
        map_query_string = self._validate_datetime(map_params, "start_date", map_query_string)
        map_query_string = self._validate_datetime(map_params, "end_date", map_query_string)

        map_query_string = self._validate_cohort_type(map_params, map_query_string)
        map_query_string = self._validate_cohort_interval(map_params, map_query_string)

        map_query_string = self._validate_group(map_params, map_query_string)

        if "fields" not in map_params or map_params["fields"] is None:
          map_params["fields"] = self.fields(TUNE_FIELDS_DEFAULT)
        if "fields" in map_params and map_params["fields"] is not None:
            map_query_string = self._validate_fields(map_params, map_query_string)

        if "format" in map_params and map_params["format"] is not None:
            map_query_string = self._validate_format(map_params, map_query_string)
        else:
            map_query_string["format"] = 'csv'

        if "filter" in map_params and map_params["filter"] is not None:
            map_query_string = self._validate_filter(map_params, map_query_string)

        if "response_timezone" in map_params and map_params["response_timezone"] is not None:
            map_query_string["response_timezone"] = map_params["response_timezone"]

        return self.call(
            "export",
            map_query_string
        )

    ## Helper function for fetching report document given provided job
    #  identifier.
    #
    #  @param str   job_id      Job Identifier of report on queue.
    #
    #  @return object
    def fetch(self,
              job_id):
        """Helper function for fetching report upon completion.
        Starts worker for polling export queue.

            :param str  job_id:     Provided Job Identifier to reference
                                    requested report on export queue.
            :return: (TuneServiceResponse)
        """
        return super(AdvertiserReportCohortRetention, self)._fetch(
            self.controller,
            "status",
            job_id
        )
