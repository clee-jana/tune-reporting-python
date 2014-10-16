"""
Builds query string as expected for Tune Management API request.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## query_string_builder.py
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
#  @version   0.9.1
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

import urllib.parse
import re
from tune.common import (
    TuneSdkException,
    TuneServiceException
)

#
# Build Query String provide with dictionary of query parameters.
#
class QueryStringBuilder(object):
    """Build Query String provide with dictionary of query parameters."""

    __query = ""

    def __init__(self, name=None, value=None):
        """Constructor a query string builder.

            Args:
                name (str, optional): query string parameter's key.\n
                value (str, optional): query string parameter's value.\n
        """
        if name is not None and isinstance(name, str) and len(name) > 0:
            self.add(name, value)

    def add(self, name, value):
        """Add query string parameter.

            Args:
                name (str): query string parameter's key.\n
                value (str): query string parameter's value.\n
        """
        if value is None:
            return

        if not name or not isinstance(name, str):
            raise ValueError("Parameter 'name' is not defined.")

        name = name.strip()

        if len(name) < 1:
            raise ValueError("Parameter 'name' is not defined.")

        if isinstance(value, str):
            value = value.strip()
            if len(value) < 1:
                return

        try:
            if name == "fields":
                # Remove all spaces
                fields_value = re.sub(r'\s+', '', value)

                self._encode(name, fields_value)

            elif name == "sort":
                if type(value) is not dict:
                    raise ValueError("Parameter 'sort' value is not a dictionary.")

                for sort_field, sort_direction in value.items():
                    sort_direction = sort_direction.upper()
                    if sort_direction != "ASC" and sort_direction != "DESC":
                        raise ValueError("Parameter 'sort' has invalid direction: '{}'".format(
                            sort_direction
                            )
                        )
                    sort_name = "sort[{}]".format(sort_field)
                    sort_value = sort_direction
                    self._encode(sort_name, sort_value)

            elif name == "filter":
                filter_value = re.sub(r'\s+', ' ', value)

                self._encode(name, filter_value)

            elif name == "group":
                group_value = re.sub(r'\s+', '', value)

                self._encode(name, group_value)

            elif isinstance(value, bool):
                if value == False:
                    bool_value = "false"
                elif value == True:
                    bool_value = "true"

                self._encode(name, bool_value)

            else:

                self._encode(name, value)
        except Exception as ex:
            raise TuneSdkException(
                "Failed to add query string parameter ({0},{1}): {2}".format(
                    name,
                    value,
                    str(ex)
                    ),
                ex
            )

    def _encode(self, name, value):
        """URL Encode query string parameter.

            Args:
                name (str): query string parameter's key.\n
                value (str): query string parameter's value.\n
        """
        try:
            if self.__query:
                self.__query += "&"

            param = urllib.parse.urlencode({name : value})
            self.__query += param
        except Exception as ex:
            raise TuneSdkException(
                "Failed to URL encode {}:{}: ({0})".format(
                    name,
                    value,
                    str(ex)
                    ),
                ex
            )

    def __str__(self):
        """String representation of an object."""
        return self.__query
