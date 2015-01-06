"""
TUNE Management Reports Endpoint base
============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_base.py
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
#  @version   $Date: 2015-01-05 19:38:53 $
#  @link      https://developers.mobileapptracking.com @endlink
#

from tune_reporting.base.endpoints import (
    EndpointBase
)


## Base components for every TUNE Management API reports.
#
class AdvertiserReportBase(EndpointBase):
    """Base components for every TUNE Management API reports.
    """

    #  Remove debug mode information from results.
    #  @var bool
    __filter_debug_mode = False

    #  Remove test profile information from results.
    #  @var bool
    __filter_test_profile_id = False

    ## The constructor.
    #
    #  @param str   controller               TUNE Management API endpoint name.
    #  @param bool  filter_debug_mode        Remove debug mode information
    #                                        from results.
    #  @param bool  filter_test_profile_id   Remove test profile information
    #                                        from results.
    #
    def __init__(self,
                 controller,
                 filter_debug_mode,
                 filter_test_profile_id):
        """The constructor.

            :param controller (string): TUNE Management API endpoint name.
            :param bool filter_debug_mode:  Remove debug mode information
                                                    from results.
            :param bool filter_test_profile_id: Remove test profile
                                                information from results.
        """

        if not isinstance(controller, str) or len(controller) < 1:
            raise ValueError(
                "Parameter 'controller' is not defined: '{}'".format(controller)
            )
        if not isinstance(filter_debug_mode, bool):
            raise ValueError(
                "Parameter 'filter_debug_mode' is not defined as bool."
            )
        if not isinstance(filter_test_profile_id, bool):
            raise ValueError(
                "Parameter 'filter_test_profile_id' is not defined as bool."
            )

        self.__filter_debug_mode = filter_debug_mode
        self.__filter_test_profile_id = filter_test_profile_id

        EndpointBase.__init__(
            self,
            controller,
            True
        )

    #  Prepare action with provided query str parameters, then call
    #  Management API service.
    #
    #  @param str   action Endpoint action to be called.
    #  @param dict  query_string_dict Query str parameters for this action.
    #
    def call(self, action, query_string_dict):
        """
        Make service request for report.

            :param action (str): Endpoint action name.
            :param query_string_dict (dict): Query str parameters of action.
            :returns (object): TuneManagementResponse
        """
        if not isinstance(action, str) or len(action) < 1:
            raise ValueError(
                "Parameter 'action' is not defined."
            )

        if query_string_dict is None or \
           not isinstance(query_string_dict, dict):
            raise ValueError(
                "Parameter 'query_string_dict' is not defined as dict."
            )

        sdk_filter = ""

        if self.__filter_debug_mode:
            sdk_filter = "(debug_mode=0 OR debug_mode is NULL)"

        if self.__filter_test_profile_id:
            if len(sdk_filter) > 0:
                sdk_filter = sdk_filter + " AND "
            sdk_filter = sdk_filter + \
                "(test_profile_id=0 OR test_profile_id IS NULL)"

        if len(sdk_filter) > 0:
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

        return EndpointBase.call(
            self,
            action,
            query_string_dict
        )
