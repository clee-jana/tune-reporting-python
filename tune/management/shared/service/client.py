#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client.py
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
#  @version   0.9.10
#  @link      https://developers.mobileapptracking.com @endlink
#

import time
import json

from tune.shared import (
    TuneSdkException,
    TuneServiceException,
    python_check_version
)
from tune.version import (
    __version__,
    __python_required_version__
)
from .request import (Request)
from .response import (Response)
from .constants import (
    __tune_management_api_endpoint__,
    __tune_management_api_version__
)
from .proxy import (
    TuneProxy
)

python_check_version(__python_required_version__)


#  Tune MobileAppTracking Management API access class
#
#  @example example_client_account_users.py
#
class TuneManagementClient(object):

    #
    #  Request
    #
    __request = None

    #
    #  Response
    #
    __response = None

    #  Constructor
    #
    #  @param string      controller          Tune Management API endpoint name
    #  @param string      action              Tune Management API endpoint's
    #                                         action name
    #  @param string      api_key             Tune MobileAppTracking API Key
    #  @param null|array  query_string_dict   Action's query string parameters
    #  @param null|string api_url_endpoint    Tune Management API endpoint path
    #  @param null|string api_url_version     Tune Management API version
    #
    def __init__(
        self,
        controller,
        action,
        api_key,
        query_string_dict=None,
        api_url_endpoint=__tune_management_api_endpoint__,
        api_url_version=__tune_management_api_version__
    ):
        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # action
        if not action or len(action) < 1:
            raise ValueError("Parameter 'action' is not defined.")
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        # set up the request
        self.__request = Request(
            controller.strip(),
            action.strip(),
            api_key.strip(),
            query_string_dict,
            api_url_endpoint,
            api_url_version
        )

    @staticmethod
    def version():
        """Get SDK version."""
        return __version__

    #  Sends a request and gets a response from the Tune Management
    #  API Service.
    #
    def call(self):
        response_success = False

        if self.__request is None or not isinstance(self.__request, Request):
            raise TuneSdkException("Request was not defined.")

        try:
            proxy = TuneProxy(self.__request.url)
            if proxy.execute():
                json_string = proxy.response.read().decode('utf-8')
                # Convert from json to python data
                response_json = json.loads(json_string)
                response_http_code = proxy.response.getcode()
                response_headers = proxy.response.info()

                self.__response = Response(
                    response_json,
                    response_http_code,
                    response_headers,
                    request_url=self.__request.url
                )

                if response_http_code == 200:
                    response_success = True

        except Exception as e:
            raise TuneSdkException(
                "Failed to execute client request ({}): ({})".format(
                    str(self.__request),
                    str(e)
                ),
                e
            )

        return response_success

    @property
    def request(self):
        return self.__request

    @property
    def response(self):
        return self.__response
