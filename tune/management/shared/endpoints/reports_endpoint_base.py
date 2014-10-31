#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reports_endpoint_base.py
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

from tune.management.shared.endpoints import (
    EndpointBase
)
from tune.shared import (
    TuneSdkException,
    TuneServiceException
)


#  Base components for every Tune Management API reports.
#
class ReportsEndpointBase(EndpointBase):
    """
    Base components for every Tune Management API reports.
    """

    #  Remove debug mode information from results.
    #  @var bool
    __filter_debug_mode = False

    #  Remove test profile information from results.
    #  @var bool
    __filter_test_profile_id = False

    #  The constructor.
    #
    #  @param str   controller               Tune Management API endpoint name.
    #  @param str   api_key                  MobileAppTracking API Key.
    #  @param bool  filter_debug_mode        Remove debug mode information
    #                                      from results.
    #  @param bool  filter_test_profile_id   Remove test profile information
    #                                      from results.
    #  @param bool  validate_fields          Validate fields used by actions'
    #                                      parameters.
    def __init__(
        self,
        controller,
        api_key,
        filter_debug_mode,
        filter_test_profile_id,
        validate_fields=False
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

        EndpointBase.__init__(
            self,
            controller,
            api_key,
            validate_fields
        )

    #  Prepare action with provided query str parameters, then call
    #  Management API service.
    #
    #  @param str   action Endpoint action to be called.
    #  @param dict  query_string_dict Query str parameters for this action.
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
