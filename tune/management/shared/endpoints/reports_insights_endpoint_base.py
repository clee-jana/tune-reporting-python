"""
Tune Mangement Insights Reports Endpoint base
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reports_insights_endpoint_base.py
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
#  @version   $Date: 2014-11-03 15:19:08 $
#  @link      https://developers.mobileapptracking.com @endlink
#

import sys

from .reports_endpoint_base import (
    ReportsEndpointBase
)
from tune.shared import (
    TuneSdkException
)
from tune.management.shared.endpoints import (
    TUNE_FIELDS_DEFAULT
)

## Base class for handling Tune Management API Insight stats reports.
#
class ReportsInsightEndpointBase(ReportsEndpointBase):
    """
    Base class for handling Tune Management API Insight stats reports.
    """

    ## The constructor.
    #
    #  @param str controller             Tune Management API endpoint name.
    #  @param str api_key                Tune MobileAppTracking API Key.
    #  @param bool   filter_debug_mode      Remove debug mode information from
    #                                       results.
    #  @param bool   filter_test_profile_id Remove test profile information
    #                                       from results.
    #  @param bool   validate_fields        Validate fields used by actions'
    #                                       parameters.
    def __init__(self,
                 controller,
                 api_key,
                 filter_debug_mode,
                 filter_test_profile_id,
                 validate_fields=False):
        """The constructor.

            :param str controller:       Tune Management API endpoint name.
            :param str api_key:          Tune MobileAppTracking API Key.
            :param bool filter_debug_mode:  Remove debug mode information
                                                    from results.
            :param bool filter_test_profile_id: Remove test profile information
                                                    from results.
            :param bool validate_fields: Validate fields used
                                        by actions' parameters.
        """
        ReportsEndpointBase.__init__(
            self,
            controller,
            api_key,
            filter_debug_mode,
            filter_test_profile_id,
            validate_fields
        )
        self.__api_key = api_key

    ## Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str cohort_type        Cohort types: click, install
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
    #  @param str filter             Apply constraints endpoint_based upon
    #                                   values associated with this endpoint's
    #                                   fields.
    #  @param str response_timezone  Setting expected timezone for results,
    #                                   default is set in account.
    #
    #  @return object @see response.py
    def count(self,
              start_date,
              end_date,
              cohort_type,
              group,
              cohort_interval=None,
              filter=None,
              response_timezone=None):
        """Counts all existing records that match filter criteria
            and returns an array of found model data.

            :param str    start_date:     YYYY-MM-DD HH:MM:SS
            :param str    end_date:       YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:    Cohort types - click, install
            :param str    group:          Group results using this endpoint's
                                            fields.
            :param str    cohort_interval:    Cohort intervals - year_day,
                                            year_week, year_month, year
            :param str    filter:         Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: TuneManagementResponse
        """
        if start_date is None or not start_date:
            raise ValueError("Parameter 'start_date' is not defined.")
        if end_date is None or not end_date:
            raise ValueError("Parameter 'end_date' is not defined.")
        if cohort_type is None or not cohort_type:
            raise ValueError("Parameter 'cohort_type' is not defined.")
        if group is None or not group:
            raise ValueError("Parameter 'group' is not defined.")

        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        self._validate_cohort_type(cohort_type)

        if cohort_interval is not None:
            self._validate_cohort_interval(cohort_interval)
        if filter is not None:
            filter = self._validate_filter(filter)

        return ReportsEndpointBase.call(
            self,
            action="count",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'cohort_type': cohort_type,
                'group': group,
                'interval': cohort_interval,
                'filter': filter,
                'response_timezone': response_timezone
            }
        )

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str start_date         YYYY-MM-DD HH:MM:SS
    #  @param str end_date           YYYY-MM-DD HH:MM:SS
    #  @param str cohort_type        Cohort types: click, install
    #  @param str aggregation_type   Aggregation types:
    #                                   cumulative, incremental
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str fields             Present results using these endpoint's
    #                                   fields.
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
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
             aggregation_type,
             group,
             fields=None,
             cohort_interval=None,
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
            :param str    cohort_interval:    Cohort intervals:
                                year_day, year_week, year_month, year
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
        if start_date is None or not start_date:
            raise ValueError("Parameter 'start_date' is not defined.")
        if end_date is None or not end_date:
            raise ValueError("Parameter 'end_date' is not defined.")
        if cohort_type is None or not cohort_type:
            raise ValueError("Parameter 'cohort_type' is not defined.")
        if aggregation_type is None or not aggregation_type:
            raise ValueError("Parameter 'aggregation_type' is not defined.")
        if group is None or not group:
            raise ValueError("Parameter 'group' is not defined.")

        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        self._validate_cohort_type(cohort_type)
        self._validate_aggregation_type(aggregation_type)

        group = self._validate_group(group)

        if cohort_interval is not None:
            self._validate_cohort_interval(cohort_interval)

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
                'cohort_type': cohort_type,
                'aggregation_type': aggregation_type,
                'group': group,
                'interval': cohort_interval,
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
    #  @param str aggregation_type   Aggregation types:
    #                                   cumulative, incremental
    #  @param str group              Group results using this endpoint's
    #                                   fields.
    #  @param str cohort_interval    Cohort intervals:
    #                                   year_day, year_week, year_month, year
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
               aggregation_type,
               group,
               fields,
               cohort_interval=None,
               filter=None,
               response_timezone=None):
        """Places a job into a queue to generate a report that will contain
        records that match provided filter criteria, and it returns a job
        identifier to be provided to action /export/download.json to download
        completed report.

            :param str    start_date:    YYYY-MM-DD HH:MM:SS
            :param str    end_date:      YYYY-MM-DD HH:MM:SS
            :param str    cohort_type:        Cohort types - click, install
            :param str    aggregation_type:   Aggregation types -
                                            cumulative, incremental
            :param str    group:          Group results using this endpoint's
                                            fields.
            :param str    fields:        No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param str    cohort_interval:    Cohort intervals -
                                        year_day, year_week, year_month, year
            :param str    filter:        Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str  response_timezone:   Setting expected timezone
                                        for data. Default is set by account.
            :return: (TuneManagementResponse)
        """
        if start_date is None or not start_date:
            raise ValueError("Parameter 'start_date' is not defined.")
        if end_date is None or not end_date:
            raise ValueError("Parameter 'end_date' is not defined.")
        if cohort_type is None or not cohort_type:
            raise ValueError("Parameter 'cohort_type' is not defined.")
        if aggregation_type is None or not aggregation_type:
            raise ValueError("Parameter 'aggregation_type' is not defined.")
        if group is None or not group:
            raise ValueError("Parameter 'group' is not defined.")
        if fields is None or not fields:
            raise ValueError("Parameter 'fields' is not defined.")
        self._validate_datetime('start_date', start_date)
        self._validate_datetime('end_date', end_date)

        self._validate_cohort_type(cohort_type)
        self._validate_aggregation_type(aggregation_type)

        group = self._validate_group(group)
        fields = self._validate_fields(fields)

        if cohort_interval is not None:
            self._validate_cohort_interval(cohort_interval)

        if filter is not None:
            filter = self._validate_filter(filter)

        return ReportsEndpointBase.call(
            self,
            action="export",
            query_string_dict={
                'start_date': start_date,
                'end_date': end_date,
                'cohort_type': cohort_type,
                'aggregation_type': aggregation_type,
                'interval': cohort_interval,
                'filter': filter,
                'fields': fields,
                'group': group,
                'response_timezone': response_timezone
            }
        )

    ## Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param str job_id             Provided Job Identifier to reference
    #                                   requested report on export queue.
    def status(self,
               job_id):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            :param str job_id: Export queue identifier
        """

        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return ReportsEndpointBase.call(
            self,
            "status",
            {
                'job_id': job_id
            }
        )

    ## Helper function for parsing export status response to gather report url.
    #  @param @see TuneManagementResponse
    #  @return str Report Url
    #  @throws TuneSdkException
    @staticmethod
    def parse_response_report_url(response):
        """Helper function for parsing export status response to
        gather report url.

            :param (object) response: TuneManagementResponse
            :return (str): Report Url
            :throws: TuneSdkException
        """
        if (not response.data or
                ("url" not in response.data)):
            raise TuneSdkException(
                "Report request failed to get export data."
            )

        url = response.data["url"]

        if sys.version_info >= (3, 0, 0):
            # for Python 3
            if isinstance(url, bytes):
                url = url.decode('ascii')  # or  s = str(s)[2:-1]
        else:
            if isinstance(url, unicode):
                url = str(url)

        return url

    ## Validate 'cohort_interval' parameter
    #  @param null|str format
    @staticmethod
    def _validate_cohort_interval(cohort_interval):
        """Validate 'cohort_interval' parameter.

            :param str cohort_interval: year_day, year_week, year_month, year
        """
        cohort_intervals = [
            "year_day",
            "year_week",
            "year_month",
            "year"
        ]

        if (not isinstance(cohort_interval, str)
                or (cohort_interval not in cohort_intervals)):
            raise TuneSdkException(
                "Parameter 'cohort_interval' is invalid: '{}'.".format(
                    cohort_interval
                )
            )

        return True

    ## Validate 'cohort_type' parameter
    #  @param null|str format
    @staticmethod
    def _validate_cohort_type(cohort_type):
        """Validate 'cohort_type' parameter.

            :param str cohort_type: click, install
        """
        cohort_types = [
            "click",
            "install"
        ]

        if (not isinstance(cohort_type, str) or
                (cohort_type not in cohort_types)):
            raise TuneSdkException(
                "Parameter 'cohort_type' is invalid: '{}'.".format(
                    cohort_type
                )
            )

        return True

    ## Validate 'aggregation_type' parameter
    #  @param null|str format
    @staticmethod
    def _validate_aggregation_type(aggregation_type):
        """Validate 'aggregation_type' parameter.

            :param str aggregation_type: incremental, cumulative
        """
        aggregation_types = [
            "incremental",
            "cumulative"
        ]

        if (not isinstance(aggregation_type, str) or
                (aggregation_type not in aggregation_types)):
            raise TuneSdkException(
                "Parameter 'aggregation_type' is invalid: '{}'.".format(
                    aggregation_type
                )
            )

        return True

    ## Helper function for parsing export response to gather job identifier.
    #  @param @see TuneManagementResponse
    #  @return str Report Job identifier
    @staticmethod
    def parse_response_report_job_id(response):
        """Helper function for parsing export response to
        gather job identifier.

            :param (object) response: TuneManagementResponse
            :return (str): Report Job identifier
        """
        if not response:
            raise ValueError(
                "Parameter 'response' is not defined."
            )
        if not response.data:
            raise ValueError(
                "Parameter 'response.data' is not defined."
            )
        if "job_id" not in response.data:
            raise ValueError(
                "Failed to return 'job_id': {}".format(str(response))
            )

        job_id = response.data['job_id']

        if not job_id or len(job_id) < 1:
            raise Exception(
                "Failed to return Job ID: {}".format(str(response))
            )

        return job_id
