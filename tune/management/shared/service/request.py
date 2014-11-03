"""
Tune Mangement API Request
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  request.py
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
#  @version   0.9.13
#  @link      https://developers.mobileapptracking.com @endlink
#

from tune.shared import (
    TuneSdkException
)
from .query_string_builder import (
    QueryStringBuilder
)


class TuneManagementRequest(object):
    """Base components for every Tune Management API request.
    """

    __controller = None
    __action = None
    __api_key = None
    __query_string_dict = None
    __api_url_endpoint = None
    __api_url_version = None

    def __init__(self,
                 controller,
                 action,
                 api_key,
                 query_string_dict,
                 api_url_endpoint,
                 api_url_version):
        """The constructor.

            :param str      controller: Tune Management API endpoint name
            :param str      action:     Tune Management API endpoint's
                                        action name
            :param str      api_key:    Tune MobileAppTracking API Key
            :param array    query_string_dict:  Action's query string
                                                parameters
            :param str      api_url_endpoint:   Tune Management API
                                                endpoint path
            :param str      api_url_version:    Tune Management API version
        """
        # -----------------------------------------------------------------
        # validate_fields inputs
        # -----------------------------------------------------------------

        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # action
        if not action or len(action) < 1:
            raise ValueError("Parameter 'action' is not defined.")
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        if not api_url_endpoint or len(api_url_endpoint) < 1:
            raise ValueError("Parameter 'api_url_endpoint' is not defined.")
        if not api_url_version or len(api_url_version) < 1:
            raise ValueError("Parameter 'api_url_version' is not defined.")

        self.__controller = controller
        self.__action = action
        self.__api_key = api_key
        self.__query_string_dict = query_string_dict
        self.__api_url_endpoint = api_url_endpoint
        self.__api_url_version = api_url_version

    @property
    def controller(self):
        """Tune Management API controller."""
        return self.__controller

    @property
    def action(self):
        """Tune Management API action."""
        return self.__action

    @property
    def endpoint_base(self):
        """Tune Management API endpoint_base URL"""
        return self.__api_url_endpoint

    @property
    def version(self):
        """Tune Management API version"""
        return self.__api_url_version

    @property
    def api_key(self):
        """Tune Management API KEY."""
        return self.__api_key

    @property
    def query_string_dict(self):
        """
        Tune Management API query string dictionary used to build Query String.
        """
        return self.__query_string_dict

    @property
    def query_string(self):
        """Tune Management API query string."""
        qsb = QueryStringBuilder()

        # Every request should contain an API Key
        if not self.__api_key or len(self.__api_key) < 1:
            raise TuneSdkException("Parameter 'api_key' is not defined.")

        qsb.add("api_key", self.__api_key)

        # Build query string with provided contents in dictionary
        if self.__query_string_dict is not None:
            for name, value in self.__query_string_dict.items():
                qsb.add(name, value)

        return str(qsb)

    @property
    def path(self):
        """Tune Management API service path"""
        request_path = "{0}/{1}/{2}/{3}".format(
            self.__api_url_endpoint,
            self.__api_url_version,
            self.__controller,
            self.__action
        )

        return request_path

    @property
    def url(self):
        """Tune Management API full service request."""
        request_url = "{0}?{1}".format(
            self.path,
            self.query_string
        )

        return request_url

    def __str__(self):
        """Pretty print.

            :rtype: str
        """
        pretty = "\napi_url_endpoint_base:\t " + str(self.__api_url_endpoint)
        pretty += "\napi_url_version:\t " + str(self.__api_url_version)
        pretty += "\ncontroller:\t " + str(self.__controller)
        pretty += "\naction:\t " + str(self.__action)
        pretty += "\napi_key:\t " + str(self.__api_key)
        pretty += "\nurl:\t " + str(self.url)
        return pretty
