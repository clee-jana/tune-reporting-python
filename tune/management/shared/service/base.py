"""
Base class to be used by all Tune Management API endpoints.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
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
#  @version   0.9.3
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

import time
import string
from datetime import datetime

from tune.version import (
    __version__
)
from .client import (
    TuneManagementClient
)

from tune.shared import (
    TuneSdkException,
    TuneServiceException
)

## Base components for every Tune Management API request.
#
class TuneManagementBase(object):
    """
    Base components for every Tune Management API request.
    """

    ## Tune Management API Endpoint
    #  @var str
    __controller = None

    ## MobileAppTracking API Key
    #  @var str
    __api_key = None

    ## Tune Management API Endpoint's fields
    #  @var list
    __fields = None

    ## Validate action's parameters against this endpoint' fields.
    #  @var bool
    __validate = False

    ## Endpoint's model name
    #  @var str
    __model_name = None

    ## Parameter 'sort' directions.
    #  @var list
    __sort_directions = [
        "DESC",
        "ASC"
        ]

    ## Parameter 'filter' expression operations.
    #  @var list
    __filter_operations = [
        "=",
        "!=",
        "<",
        "<=",
        ">",
        ">=",
        "IS NULL",
        "IS NOT NULL",
        "IN",
        "NOT IN",
        "LIKE",
        "NOT LIKE",
        "RLIKE",
        "NOT RLIKE",
        "REGEXP",
        "NOT REGEXP",
        "BETWEEN",
        "NOT BETWEEN"
        ]

    ## Parameter 'sort' directions.
    #  @var list
    __filter_conjunctions = [
        "AND",
        "OR"
        ]

     ## Constructor
     #
     #  @param string controller    Tune Management API Endpoint
     #  @param string api_key       MobileAppTracking API Key
     #  @param bool   validate      Validate fields used by actions' parameters.
     #
    def __init__(
        self,
        controller,
        api_key,
        validate
        ):
        """Constructor a new request object.

            Args:
                controller (str): Controller portion of Tune Service request.\n
                api_key (str): User's Tune API Key.\n

        """
        # -----------------------------------------------------------------
        # validate inputs
        # -----------------------------------------------------------------

        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        self.__controller = controller
        self.__api_key = api_key
        self.__validate = validate

    ## Get controller
    #  @return string
    @property
    def controller(self):
        """Tune Management API controller."""
        return self.__controller

    ## Get API Key
    #  @return string
    @property
    def api_key(self):
        """Tune Management API KEY."""
        return self.__api_key

    ## Call Tune Management API service for this controller.
    # @param string action               Tune Management API endpoint's action name
    # @param array  query_string_dict    Action's query string parameters
    # @return object @see Response
    def call(
        self,
        action,
        query_string_dict=None
    ):
        """Call Tune Management API service requesting response
        base upon provided controller/action?query_string.

        """
        client = TuneManagementClient(
            self.__controller,
            action,
            self.__api_key,
            query_string_dict
            )

        client.call()

        return client.response

    ## Provide complete definition for this endpoint.
    #  @return object @see Response
    def define(self):
        return self.call(
            action="define"
        )

    ## Get all fields for assigned endpoint.
    #  @return list endpoint fields
    #  @throws TuneServiceException
    def fields(self):
        query_string_dict = {
                'controllers': self.__controller,
                'details': 'modelName,fields'
            }

        client = TuneManagementClient(
            "apidoc",
            "get_controllers",
            self.__api_key,
            query_string_dict
            )

        client.call()

        if client.response.http_code != 200:
            raise TuneServiceException(
                    "Connection failure '{}': {}".format(
                        client.response.request_url,
                        client.response.http_code
                    )
                )

        if ((client.response.data is None)
            or (isinstance(client.response.data, list)
                and (len(client.response.data) == 0))):
            raise TuneServiceException(
                    "Failed to get fields for endpoint: '{}'".format(
                       self.__controller
                    )
                )

        fields = client.response.data[0]["fields"]
        self.__model_name = client.response.data[0]["modelName"]

        field_names = []
        related_fields = {}
        for field in fields:

            if field["related"] == 1:
                if field["type"] == "property":
                    related_property = field["name"]
                    if related_property not in related_fields:
                        related_fields[related_property] = []
                    continue

                field_related = field["name"].split(".")
                related_property = field_related[0];
                related_field_name = field_related[1];

                if related_property not in related_fields:
                    related_fields[related_property] = []

                related_fields[related_property].append(related_field_name)
                continue

            field_name = field["name"]
            field_names.append(field_name)

        field_names_merged = []

        field_names.sort()

        for field_name in field_names:
            field_names_merged.append(field_name)
            if ((field_name != "_id") and field_name.endswith("_id")):
                related_property = field_name[:-3]

                if ((related_property in related_fields)
                    and (len(related_fields[related_property]) > 0)):
                    for related_field_name in related_fields[related_property]:
                        field_names_merged.append("{}.{}".format(
                            related_property,
                            related_field_name
                            )
                        )
                else:
                    field_names_merged.append("{}.name".format(
                        related_property
                        )
                    )

        self.__fields = field_names_merged

        return self.__fields

    ## Get model name for this endpoint.
    #  @return string model name
    def model_name(self):
        if self.__fields is None:
            self.fields()

        return self.__model_name

    ## Validate query string parameter 'fields' having valid endpoint's fields
    #  @param array|string fields
    #  @return string
    #  @throws TuneSdkException
    def validate_fields(self, fields):
        if not isinstance(fields, str) and not isinstance(fields, list):
            raise TuneSdkException(
                "Invalid parameter 'fields' provided: '{}'".format(fields))

        fields_list = None
        if isinstance(fields, str):
            fields_list = []
            for item in fields.split(","):
                fields_list.append(item.strip())
        else:
            fields_list = fields

        if len(fields_list) == 0:
            raise TuneSdkException(
                "Invalid parameter 'fields' provided: '{}'".format(fields))

        if self.__validate:
            if self.__fields is None:
                self.fields()

            for field in fields_list:
                if field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'fields' contains an invalid field: '{}'.".format(
                            field
                            )
                        )

        return ",".join(fields_list)

    ## Validate query string parameter 'group' having valid endpoint's fields
    #  @param array|string group
    #  @return string
    #  @throws TuneSdkException
    def validate_group(self, group):
        if not isinstance(group, str) and not isinstance(group, list):
            raise TuneSdkException(
                "Invalid parameter 'group' provided: '{}'".format(group))

        group_list = None
        if isinstance(group, str):
            group_list = []
            for item in group.split(","):
                group_list.append(item.strip())
        else:
            group_list = group

        if len(group_list) == 0:
            raise TuneSdkException("Invalid parameter 'group' provided: '{}'".format(group))

        if self.__validate:
            if self.__fields is None:
                self.fields()

            for group_field in group_list:
                if group_field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'group' contains an invalid field: '{}'.".format(
                            group_field
                            )
                        )

        return ",".join(group_list)

    ## Validate query string parameter 'sort' having valid endpoint's fields
    #  @param dict sort
    #  @return dict
    #  @throws TuneSdkException
    def validate_sort(self, sort):
        if not isinstance(sort, dict):
            raise TuneSdkException("Invalid parameter 'sort' provided.")

        if self.__validate:
            if self.__fields is None:
                self.fields()

            for sort_field, sort_direction in sort.items():
                if sort_field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'sort' contains an invalid field: '{}'.".format(
                            sort_field
                            )
                        )
                if sort_direction not in self.__sort_directions:
                    raise TuneSdkException(
                        "Parameter 'sort' contains an invalid direction: '{}'.".format(
                            sort_direction
                            )
                        )
        return sort

    ## Validate filter parameter
    #
    def validate_filter(self, filter):
        if filter is None:
            return filter

        if not isinstance(filter, str) and not isinstance(filter, list):
            raise TuneSdkException("Invalid parameter 'filter' provided.")

        return filter

    ## Validate 'format' parameter
    #  @param null|str format
    @staticmethod
    def validate_format(format):
        report_export_formats = [
            "csv",
            "json"
            ]
        if format is None:
            return format

        if (isinstance(format, str)
            and (format not in report_export_formats)):
            raise TuneSdkException(
                "Parameter 'format' is invalid: '{}'.".format(format))

        return True


    ## Validate parameters of type datetime.
    #  @param str param_name
    #  @param str datetime
    @staticmethod
    def validate_datetime(param_name, date_time):

        try:
            datetime.strptime(date_time, '%Y-%m-%d')
            return True
        except ValueError:
            pass

        try:
            datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            pass

        raise ValueError(
            "Parameter '{}' is invalid: '{}'.".format(param_name, date_time))

    ## Get SDK version
    #  @return string
    @staticmethod
    def version():
        """Get SDK version."""
        return __version__

    ## To string
    #  @return string
    def __str__(self):
        """For debug purposes, provide string representation of this object."""
        return "{}, {}".format(self.__controller, self.__api_key)