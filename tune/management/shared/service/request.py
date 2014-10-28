"""
Container of complete request Tune Management API request.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## request.py
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
#  @version   0.9.9
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from .query_string_builder import (
    QueryStringBuilder
)
from tune.shared import (
    TuneSdkException
)

class Request(object):
    """Base components for every Tune Management API request.

    Attributes:
        __controller        Tune Management API controller
        __action            Tune Management API action
        __api_key           Tune Management API key of user
        __query_string_dict Query String parameters
        __api_url_base      Tune Management API base URL
        __api_url_version   Tune Management API version
    """

    __controller = None
    __action = None
    __api_key = None
    __query_string_dict = None
    __api_url_base = None
    __api_url_version = None

    def __init__(
        self,
        controller,
        action,
        api_key,
        query_string_dict,
        api_url_base,
        api_url_version
        ):
        """Constructor a new request object.

            Args:
                controller (str): Controller portion of Tune Service request.\n
                action (str): Action portion of Tune Service request.\n
                api_key (str): User's Tune API Key.\n
                query_string_dict (dictionary, optional): Other attributes
                to be included in the request's query string.\n

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

        if not api_url_base or len(api_url_base) < 1:
            raise ValueError("Parameter 'api_url_base' is not defined.")
        if not api_url_version or len(api_url_version) < 1:
            raise ValueError("Parameter 'api_url_version' is not defined.")

        self.__controller = controller
        self.__action = action
        self.__api_key = api_key
        self.__query_string_dict = query_string_dict
        self.__api_url_base = api_url_base
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
    def base(self):
        """Tune Management API base URL"""
        return self.__api_url_base

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
        """Tune Management API query string dictionary used to build Query String."""
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
                self.__api_url_base,
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

            Returns:
                string
        """
        pretty = "\napi_url_base:\t " + str(self.__api_url_base)
        pretty += "\napi_url_version:\t " + str(self.__api_url_version)
        pretty += "\ncontroller:\t " + str(self.__controller)
        pretty += "\naction:\t " + str(self.__action)
        pretty += "\napi_key:\t " + str(self.__api_key)
        pretty += "\nurl:\t " + str(self.url)
        return pretty
