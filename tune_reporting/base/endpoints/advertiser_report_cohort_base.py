"""
TUNE Service Insights Reports Endpoint base
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_cohort_base.py
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

import sys

from .advertiser_report_base import (
    AdvertiserReportBase
)
from tune_reporting.helpers import (
    TuneSdkException
)


## Base class for handling TUNE Reporting API Insight stats reports.
#
class AdvertiserReportCohortBase(AdvertiserReportBase):
    """
    Base class for handling TUNE Reporting API Insight stats reports.
    """

    ## The constructor.
    #
    #  @param str controller                TUNE Reporting API endpoint name.
    #  @param bool   filter_debug_mode      Remove debug mode information from
    #                                       results.
    #  @param bool   filter_test_profile_id Remove test profile information
    #                                       from results.
    def __init__(self,
                 controller,
                 filter_debug_mode,
                 filter_test_profile_id):
        """The constructor.

            :param str controller:       TUNE Reporting API endpoint name.
            :param bool filter_debug_mode:  Remove debug mode information
                                                    from results.
            :param bool filter_test_profile_id: Remove test profile information
                                                    from results.
        """
        AdvertiserReportBase.__init__(
            self,
            controller,
            filter_debug_mode,
            filter_test_profile_id
        )

    ## Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    # @param dict map_params    Mapping of: <p><dl>
    # <dt>start_date</dt><dd>YYYY-MM-DD HH:MM:SS</dd>
    # <dt>end_date</dt><dd>YYYY-MM-DD HH:MM:SS</dd>
    # <dt>cohort_type</dt><dd>Cohort types: click, install</dd>
    # <dt>cohort_interval</dt><dd>Cohort intervals: year_day, year_week, year_month, year</dd>
    # <dt>group</dt><dd>Group results using this endpoint's fields.</dd>
    # <dt>filter</dt><dd>Apply constraints based upon values associated with
    #                    this endpoint's fields.</dd>
    # <dt>response_timezone</dt><dd>Setting expected timezone for results,
    #                          default is set in account.</dd>
    # </dl><p>
    #
    #  @return object TuneServiceResponse
    #
    def count(self,
              map_params):
        """Counts all existing records that match filter criteria
            and returns an array of found model data.

            :param (dict) map_params:\n
                start_date: YYYY-MM-DD HH:MM:SS\n
                end_date: YYYY-MM-DD HH:MM:SS\n
                cohort_type: Cohort types: click, install.\n
                cohort_interval: Cohort intervals:
                    year_day, year_week, year_month, year.\n
                group: Group results using this endpoint's fields.\n
                filter: Apply constraints based upon values
                    associated with this endpoint's fields.\n
                response_timezone: Setting expected timezone for results,
                    default is set in account.\n

            :return: TuneServiceResponse
        """
        map_query_string = {}
        map_query_string = self._validate_datetime(map_params, "start_date", map_query_string)
        map_query_string = self._validate_datetime(map_params, "end_date", map_query_string)

        map_query_string = self._validate_cohort_type(map_params, map_query_string)
        map_query_string = self._validate_cohort_interval(map_params, map_query_string)

        map_query_string = self._validate_group(map_params, map_query_string)

        if "filter" in map_params and map_params["filter"] is not None:
            map_query_string = self._validate_filter(map_params, map_query_string)

        if "response_timezone" in map_params and map_params["response_timezone"] is not None:
            map_query_string["response_timezone"] = map_params["response_timezone"]

        return AdvertiserReportBase.call(
            self,
            "count",
            map_query_string
        )

    ## Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param str job_id             Provided Job Identifier to reference
    #                                   requested report on export queue.
    #
    #  @return object TuneServiceResponse
    #
    def status(self,
               job_id):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            :param str job_id: Export queue identifier
            :return: (TuneServiceResponse)
        """

        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return AdvertiserReportBase.call(
            self,
            "status",
            {
                'job_id': job_id
            }
        )

    ## Helper function for parsing export status response to gather report url.
    #  @param @see TuneServiceResponse
    #  @return str Report Url
    #  @throws TuneSdkException
    @staticmethod
    def parse_response_report_url(response):
        """Helper function for parsing export status response to
        gather report url.

            :param (object) response: TuneServiceResponse
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

    ## Validate query string parameter 'cohort_interval'.
    #  @param dict map_params
    #  @param dict map_query_string
    #  @return dict map_query_string
    #  @throws ValueError
    @staticmethod
    def _validate_cohort_interval(map_params, map_query_string):
        """Validate 'cohort_interval' parameter.

            :param (dict) map_params
            :param (dict) map_query_string

            :return (dict): map_query_string
            :throws: ValueError
        """

        if 'cohort_interval' not in map_params:
            raise ValueError("Parameter 'cohort_interval' is not defined.")

        cohort_interval = map_params['cohort_interval']

        cohort_intervals = [
            "year_day",
            "year_week",
            "year_month",
            "year"
        ]
        if cohort_interval is None or not cohort_interval:
            raise ValueError("Parameter 'cohort_interval' is not defined.")
        if (not isinstance(cohort_interval, str)
                or (cohort_interval not in cohort_intervals)):
            raise TuneSdkException(
                "Parameter 'cohort_interval' is invalid: '{}'.".format(
                    cohort_interval
                )
            )

        map_query_string['interval'] = cohort_interval
        return map_query_string

    ## Validate query string parameter 'cohort_type'.
    #  @param dict map_params
    #  @param dict map_query_string
    #  @return dict map_query_string
    #  @throws ValueError
    @staticmethod
    def _validate_cohort_type(map_params, map_query_string):
        """Validate 'cohort_type' parameter.

            :param (dict) map_params
            :param (dict) map_query_string

            :return (dict): map_query_string
            :throws: ValueError
        """

        if 'cohort_type' not in map_params:
            raise ValueError("Parameter 'cohort_type' is not defined.")

        cohort_type = map_params['cohort_type']

        cohort_types = [
            "click",
            "install"
        ]
        if cohort_type is None or not cohort_type:
            raise ValueError("Parameter 'cohort_type' is not defined.")
        if (not isinstance(cohort_type, str) or
                (cohort_type not in cohort_types)):
            raise TuneSdkException(
                "Parameter 'cohort_type' is invalid: '{}'.".format(
                    cohort_type
                )
            )

        map_query_string['cohort_type'] = cohort_type
        return map_query_string

    ## Validate query string parameter 'aggregation_type'.
    #  @param dict map_params
    #  @param dict map_query_string
    #  @return dict map_query_string
    #  @throws ValueError
    @staticmethod
    def _validate_aggregation_type(map_params, map_query_string):
        """Validate 'aggregation_type' parameter.

            :param (dict) map_params
            :param (dict) map_query_string

            :return (dict): map_query_string
            :throws: ValueError
        """

        if 'aggregation_type' not in map_params:
            raise ValueError("Parameter 'aggregation_type' is not defined.")

        aggregation_type = map_params['aggregation_type']

        aggregation_types = [
            "incremental",
            "cumulative"
        ]

        if aggregation_type is None or not aggregation_type:
            raise ValueError("Parameter 'aggregation_type' is not defined.")
        if (not isinstance(aggregation_type, str) or
                (aggregation_type not in aggregation_types)):
            raise TuneSdkException(
                "Parameter 'aggregation_type' is invalid: '{}'.".format(
                    aggregation_type
                )
            )

        map_query_string['aggregation_type'] = aggregation_type
        return map_query_string

    ## Helper function for parsing export response to gather job identifier.
    #  @param @see TuneServiceResponse
    #  @return str Report Job identifier
    @staticmethod
    def parse_response_report_job_id(response):
        """Helper function for parsing export response to
        gather job identifier.

            :param (object) response: TuneServiceResponse
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
