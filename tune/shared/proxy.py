"""
Proxy class associated with Tune Management API service.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## proxy.py
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
#  @package   Tune_PHP_SDK
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.8
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#
import time
import sys

if sys.version_info[0] == 3:
    import urllib.request
else:
    import urllib2

from .exceptions import (
    TuneSdkException,
    TuneServiceException
    )

#
# Service process class for connecting to Tune Management API service.
#
# package Tune_Python_SDK
#
class TuneProxy:
    """Service proxy class for connecting to Tune Management API service.

    Attributes:
        __request:     Tune Management API request object\n
        __response:    Tune Management API response object\n
    """

    __request_url = None
    __response = None

    @property
    def response(self):
        """Full response object to Tune Management API service."""
        return self.__response

    def __init__(self, request_url):
        if request_url is None or not isinstance(request_url, str):
            raise ValueError(
                "Invalid 'request_url' provided: '{}'".format(request_url)
                )

        self.__request_url = request_url

    def execute(self):
        """HTTP POST request to Tune MobileAppTracking Management API.

            Returns:
                bool: True upon success.
        """
        if self.__request_url is None:
            raise TuneSdkException('Request is not set.')

        self.__response = None
        if sys.version_info[0] == 3:
            try:
                self.__response = urllib.request.urlopen(self.__request_url)
            except TuneSdkException as ex:
                raise
            except TuneServiceException as ex:
                raise
            except urllib.error.URLError as ex:
                raise TuneServiceException(
                    "URLError: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url
                        ),
                    ex
                    )
            except urllib.error.HTTPError as ex:
                raise TuneServiceException(
                    "HTTPError: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url
                        ),
                    ex
                    )
            except Exception as ex:
                raise TuneSdkException(
                    "Failed to post request: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url
                        ),
                    ex
                )
        else:
            try:
                self.__response = urllib2.urlopen(self.__request_url)
            except TuneSdkException as ex:
                raise
            except TuneServiceException as ex:
                raise
            except urllib2.URLError as ex:
                raise TuneServiceException(
                    "URLError: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url
                        ),
                    ex
                    )
            except urllib2.HTTPError as ex:
                raise TuneServiceException(
                    "HTTPError: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url
                        ),
                    ex
                    )
            except Exception as ex:
                raise TuneSdkException(
                    "Failed to post request: (Error:{0}, Url:{1})".format(
                        str(ex),
                        self.__request_url),
                    ex
                )

        return True
