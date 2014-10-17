"""
Base class for handling all Tune Management API endpoints that deal with reports.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## reports_base.py
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
#  Python 3.0
#
#  @category  Tune
#  @package   Tune_PHP_SDK
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.2
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from tune.management.shared.service import (
    TuneManagementBase
)
from .report_reader_csv import (
    ReportReaderCSV
)
from .report_reader_json import (
    ReportReaderJSON
)
from tune.shared import (
    TuneSdkException,
    TuneServiceException
)
from .report_export_worker import (
    ReportExportWorker
)

## Base components for every Tune Management API reports.
#
class ReportsBase(TuneManagementBase):
    """
    Base components for every Tune Management API reports.
    """

    ## Remove debug mode information from results.
    #  @var bool
    __filter_debug_mode = False

    ## Remove test profile information from results.
    #  @var bool
    __filter_test_profile_id = False

    ## The constructor.
    #
    #  @param str   controller                 Tune Management API endpoint name.
    #  @param str   api_key                    MobileAppTracking API Key.
    #  @param bool  filter_debug_mode          Remove debug mode information
    #                                           from results.
    #  @param bool  filter_test_profile_id     Remove test profile information
    #                                           from results.
    #  @param bool  validate                   Validate fields used by actions'
    #                                           parameters.
    def __init__(
        self,
        controller,
        api_key,
        filter_debug_mode,
        filter_test_profile_id,
        validate=False
        ):

        if not isinstance(controller, str) or len(controller) < 1:
            raise ValueError(
                "Parameter 'controller' is not defined."
            )
        if not isinstance(api_key, str) or len(api_key) < 1:
            raise ValueError(
                "Parameter 'api_key' is not defined."
            )
        if not isinstance(filter_debug_mode, bool):
            raise ValueError(
                "Parameter 'filter_debug_mode' is not defined as bool."
            )
        if not isinstance(filter_test_profile_id, bool):
            raise ValueError(
                "Parameter 'filter_test_profile_id' is not defined as bool."
            )

        self.__api_key = api_key
        self.__filter_debug_mode = filter_debug_mode
        self.__filter_test_profile_id = filter_test_profile_id

        TuneManagementBase.__init__(
            self,
            controller,
            api_key,
            validate
            )

    ## Prepare action with provided query str parameters, then call
    #  Management API service.
    #
    #  @param str    $action Endpoint action to be called.
    #  @param dict      $query_string_dict Query str parameters for this action.
    #
    def call(
        self,
        action,
        query_string_dict
    ):
        """
        Make service request for report.

        Parameters:
            action (str) - Endpoint action name.
            query_string_dict(dict) - Query str parameters of action.
        """
        if not isinstance(action, str) or len(action) < 1:
            raise ValueError(
                "Parameter 'action' is not defined."
                )

        if query_string_dict is None and not isinstance(query_string_dict, dict):
            raise ValueError(
                "Parameter 'query_string_dict' is not defined as dict."
                )

        sdk_filter = None

        if self.__filter_debug_mode or self.__filter_test_profile_id:
            sdk_filter = None
            if self.__filter_debug_mode:
                sdk_filter = "(debug_mode=0 OR debug_mode is NULL)"

            if self.__filter_test_profile_id:
                if sdk_filter is not None:
                    sdk_filter = sdk_filter + " AND "
                sdk_filter = "(test_profile_id=0 OR test_profile_id IS NULL)"

        if sdk_filter is not None:
            if 'filter' in query_string_dict:
                if query_string_dict['filter'] is not None:
                    if isinstance(query_string_dict['filter'], str):
                        if len(query_string_dict['filter']) > 0:
                            query_string_dict['filter'] = "({}) AND {}".format(
                                query_string_dict['filter'],
                                sdk_filter
                                )
                        else:
                            query_string_dict['filter'] = sdk_filter
                    else:
                        query_string_dict['filter'] = sdk_filter
                else:
                    query_string_dict['filter'] = sdk_filter
            else:
                query_string_dict['filter'] = sdk_filter

        if 'filter' in query_string_dict:
            if query_string_dict['filter'] is not None:
                if isinstance(query_string_dict['filter'], str):
                    if len(query_string_dict['filter']) > 0:
                        query_string_dict['filter'] = "({})".format(
                            query_string_dict['filter']
                        )

        return TuneManagementBase.call(
            self,
            action,
            query_string_dict
        )

    ## Helper function for fetching report document given provided job identifier.
    #
    #  Requesting for report url is not the same for all report endpoints.
    #
    #  @param str    mod_export_class        Report class.
    #  @param str    mod_export_function     Report function performing status request.
    #  @param str    job_id                  Job Identifier of report on queue.
    #  @param str    report_format           Requested document format: csv, json
    #  @param bool   verbose                 For debugging purposes only.
    #  @param int    sleep                   How long thread should sleep before
    #                                           next status request.
    #
    #  @return object Report reader
    #  @throws ValueError
    #  @throws TuneServiceException
    #
    def fetch(
        self,
        mod_export_namespace,
        mod_export_class,
        mod_export_function,
        job_id,
        report_format,
        verbose=False,
        sleep=60 # seconds
    ):
        """
        Helper function for fetching report document given provided job identifier.
        """

        # api_key
        if not self.__api_key or len(self.__api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")
        if not mod_export_namespace or len(mod_export_namespace) < 1:
            raise ValueError("Parameter 'mod_export_namespace' is not defined.")
        if not mod_export_class or len(mod_export_class) < 1:
            raise ValueError("Parameter 'mod_export_function' is not defined.")
        if not mod_export_function or len(mod_export_function) < 1:
            raise ValueError("Parameter 'mod_export_function' is not defined.")
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")
        if not report_format or len(report_format) < 1:
            raise ValueError("Parameter 'report_format' is not defined.")

        export_worker = ReportExportWorker(
            mod_export_namespace,
            mod_export_class,
            mod_export_function,
            self.__api_key,
            job_id,
            verbose,
            sleep
        )
        thread_killed = False
        try:
            if verbose:
                print("Starting...")
            export_worker.start()
            if verbose:
                print("Waiting...")
            export_worker.join()
            if verbose:
                print("Completed...")
                print(export_worker.response)
        except (KeyboardInterrupt, SystemExit):
            print("\n! Received keyboard interrupt, quitting threads.\n")
            thread_killed = True
            export_worker.stop()
        except TuneSdkException as ex:
            raise
        except Exception as ex:
            raise TuneSdkException(
                "Failed to post request: (Error:{0})".format(
                    str(ex)
                    ),
                ex
                )

        if thread_killed:
            return None

        if (not export_worker.response
            or export_worker.response.http_code != 200
            or export_worker.response.data["status"] == "fail"
        ):
            raise TuneServiceException(
                "Report request failed: {}".format(str(export_worker.response))
                )

        loaded_mod = __import__(mod_export_namespace, fromlist=[mod_export_namespace])

        # Load it from imported module
        loaded_class = getattr(loaded_mod, mod_export_class)

        report_url = loaded_class.parse_response_url(export_worker.response)

        if not report_url or len(report_url) < 1:
            raise TuneSdkException("Failed to get report url from response.")

        return self.parse_report_data(report_url, report_format)

    ## Helper function for fetching report document given provided job identifier.
    #
    #  Response is not the same for all report endpoints.
    #
    #  @param str report_url     Report url provided upon
    #                               completing of export processing.
    #  @param str report_format  Expected format of exported report.
    #
    @staticmethod
    def parse_report_data(
       report_url,
       report_format
    ):
        """
        Helper function for fetching report document given provided job identifier.
        """

        report_reader = None
        try:
            if report_format == "csv":
                report_reader = ReportReaderCSV(
                    report_url
                )
            elif report_format == "json":
                report_reader = ReportReaderJSON(
                    report_url
                )
        except Exception as ex:
            raise TuneSdkException(
                "Failed to create reader provided by report url {}: {}".format(
                    report_url,
                    str(ex)
                )
            )

        return report_reader

