#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

import time
import string
import re
from datetime import datetime

from tune.version import (
    __version__
)
from tune.management.shared.service import (
    TuneManagementClient
)
from tune.shared import (
    TuneSdkException,
    TuneServiceException,
    is_parentheses_balanced
)
from tune.shared.report_export_worker import (
    ReportExportWorker
)

TUNE_FIELDS_ALL = 0
TUNE_FIELDS_DEFAULT = 1
TUNE_FIELDS_RELATED = 2
TUNE_FIELDS_MINIMAL = 4
TUNE_FIELDS_RECOMMENDED = 8


#  Base components for every Tune Management API request.
#
class EndpointBase(object):

    """
    Base components for every Tune Management API request.
    """

    #  Tune Management API Endpoint
    #  @var str
    __controller = None

    #  MobileAppTracking API Key
    #  @var str
    __api_key = None

    #  Tune Management API Endpoint's fields
    #  @var list
    __fields = None

    #  Validate action's parameters against this endpoint' fields.
    #  @var bool
    __validate_fields = False

    #  Endpoint's model name
    #  @var str
    __model_name = None

    #  Parameter 'sort' directions.
    #  @var list
    __sort_directions = [
        "DESC",
        "ASC"
    ]

    #  Parameter 'filter' expression operations.
    #  @var list
    __filter_operations = [
        "=",
        "!=",
        "<",
        "<=",
        ">",
        ">=",
        "IS",
        "NOT",
        "NULL",
        "IN",
        "LIKE",
        "RLIKE",
        "REGEXP",
        "BETWEEN"
    ]

    #  Parameter 'filter' conjunction operations.
    #  @var list
    __filter_conjunctions = [
        "AND",
        "OR"
    ]

    #  Recommended fields for report exports
    #  @var list
    __fields_recommended = None

    #  Constructor
    #
    #  @param string controller         Tune Management API Endpoint
    #  @param string api_key            MobileAppTracking API Key
    #  @param bool   validate_fields    Validate fields used by actions'
    #                                   parameters.
    #
    def __init__(
        self,
        controller,
        api_key,
        validate_fields
    ):
        """Constructor a new request object.

            Args:
                controller (str): Controller portion of Tune Service request.\n
                api_key (str): User's Tune API Key.\n

        """
        # -----------------------------------------------------------------
        # validate_fields inputs
        # -----------------------------------------------------------------

        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        self.__controller = controller
        self.__api_key = api_key
        self.__validate_fields = validate_fields

    #  Get controller
    #  @return string
    @property
    def controller(self):
        """Tune Management API controller."""
        return self.__controller

    #  Get API Key
    #  @return string
    @property
    def api_key(self):
        """Tune Management API KEY."""
        return self.__api_key

    #  Call Tune Management API service for this controller.
    # @param string action              Tune Management API endpoint's
    #                                   action name.
    # @param array  query_string_dict   Action's query string parameters
    # @return object @see Response
    def call(
        self,
        action,
        query_string_dict=None
    ):
        """Call Tune Management API service requesting response
        endpoint_base upon provided controller/action?query_string.
        """
        client = TuneManagementClient(
            self.controller,
            action,
            self.api_key,
            query_string_dict
        )

        client.call()

        return client.response

    #  Provide complete definition for this endpoint.
    #  @return object @see Response
    def define(self):
        return self.call(
            action="define"
        )

    #  Get all fields for assigned endpoint.
    #  @return list endpoint fields
    #  @throws TuneServiceException
    def fields(self, enum_fields_selection=TUNE_FIELDS_ALL):

        if (self.__validate_fields or
           not (enum_fields_selection & TUNE_FIELDS_RECOMMENDED)) and \
           self.__fields is None:
            self.__endpoint_fields()

        if enum_fields_selection & TUNE_FIELDS_RECOMMENDED:
            if self.fields_recommended is None:
                raise TuneSdkException(
                    "Property 'fields_recommended' not defined."
                )
            return self.fields_recommended

        if not (enum_fields_selection & TUNE_FIELDS_DEFAULT) \
           and (enum_fields_selection & TUNE_FIELDS_RELATED):
            fields = self.__fields.keys()
            fields.sort()
            return fields

        fields_filtered = {}

        for field_name, field_info in self.__fields.items():
            if not (enum_fields_selection & TUNE_FIELDS_RELATED) \
               and not (enum_fields_selection & TUNE_FIELDS_MINIMAL) \
               and field_info["related"]:
                continue

            if not (enum_fields_selection & TUNE_FIELDS_DEFAULT) \
               and not field_info["related"]:
                fields_filtered[field_name] = field_info
                continue

            if (enum_fields_selection & TUNE_FIELDS_DEFAULT) \
               and field_info["default"]:
                if (enum_fields_selection & TUNE_FIELDS_MINIMAL) \
                   and field_info["related"]:

                    for related_field in [".name", ".ref"]:
                        if field_name.endswith(related_field):
                            fields_filtered[field_name] = field_info

                    continue

                fields_filtered[field_name] = field_info
                continue

            if (enum_fields_selection & TUNE_FIELDS_RELATED) \
               and field_info["related"]:
                fields_filtered[field_name] = field_info
                continue

        fields = fields_filtered.keys()
        fields.sort()
        return fields

    #  Fetch all fields from model and related models of this endpoint.
    #  @return list endpoint fields
    #  @throws TuneServiceException
    def __endpoint_fields(self):
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
                "Failed to get fields for "
                "endpoint: '{}'".format(self.__controller)
            )

        fields = client.response.data[0]["fields"]
        self.__model_name = client.response.data[0]["modelName"]

        fields_found = {}
        related_fields = {}
        for field in fields:
            if field["related"] == 1:
                if field["type"] == "property":
                    related_property = field["name"]
                    if related_property not in related_fields:
                        related_fields[related_property] = []
                    continue

                field_related = field["name"].split(".")
                related_property = field_related[0]
                related_field_name = field_related[1]

                if related_property not in related_fields:
                    related_fields[related_property] = []

                related_fields[related_property].append(related_field_name)
                continue

            field_name = field["name"]
            fields_found[field_name] = {
                "default": field["fieldDefault"],
                "related": False
            }

        fields_found_merged = {}

        for field_name, field_info in fields_found.items():
            fields_found_merged[field_name] = field_info
            if (field_name != "_id") and field_name.endswith("_id"):
                related_property = field_name[:-3]

                if (related_property in related_fields) \
                   and (len(related_fields[related_property]) > 0):

                    for related_field_name in related_fields[related_property]:

                        # Not including duplicate data.
                        if related_field_name == "id":
                            continue

                        related_property_field_name = "{}.{}".format(
                            related_property,
                            related_field_name
                        )
                        fields_found_merged[related_property_field_name] = {
                            "default": field["fieldDefault"],
                            "related": True
                        }
                else:
                    related_property_field_name = "{}.{}".format(
                        related_property,
                        "name"
                    )
                    fields_found_merged[related_property_field_name] = {
                        "default": field["fieldDefault"],
                        "related": True
                    }

        self.__fields = fields_found_merged

        return self.__fields

    #  Get model name for this endpoint.
    #  @return string model name
    def model_name(self):
        if self.__fields is None:
            self.fields()

        return self.__model_name

    #  Validate query string parameter 'fields' having valid
    #  endpoint's fields
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

        if self.__validate_fields:
            if self.__fields is None:
                self.fields()

            for field in fields_list:
                if field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'fields' contains "
                        "an invalid field: '{}'.".format(
                            field
                        )
                    )

        return ",".join(fields_list)

    #  Validate query string parameter 'group' having valid endpoint's fields
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
            raise TuneSdkException(
                "Invalid parameter 'group' provided: '{}'".format(group)
            )

        if self.__validate_fields:
            if self.__fields is None:
                self.fields()

            for group_field in group_list:
                if group_field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'group' contains "
                        "an invalid field: '{}'.".format(
                            group_field
                        )
                    )

        return ",".join(group_list)

    #  Validate query string parameter 'sort' having valid endpoint's fields
    #  @param dict sort
    #  @return dict
    #  @throws TuneSdkException
    def validate_sort(self, sort):
        if not isinstance(sort, dict):
            raise TuneSdkException("Invalid parameter 'sort' provided.")

        if self.__validate_fields:
            if self.__fields is None:
                self.fields()

        sort_build = {}
        for sort_field, sort_direction in sort.items():
            if self.__validate_fields:
                if sort_field not in self.__fields:
                    raise TuneSdkException(
                        "Parameter 'sort' contains "
                        "an invalid field: '{}'.".format(
                            sort_field
                        )
                    )
            sort_direction = sort_direction.upper()
            if sort_direction not in self.__sort_directions:
                raise TuneSdkException(
                    "Parameter 'sort' contains "
                    "an invalid direction: '{}'.".format(
                        sort_direction
                    )
                )

            sort_build[sort_field] = sort_direction

        return sort_build

    #  Validate filter parameter
    #
    def validate_filter(self, filter):

        if not isinstance(filter, str) or not filter:
            raise TuneSdkException(
                "Parameter 'filter' is invalid: '{}'.".format(
                    filter
                )
            )

        if self.__validate_fields:
            if self.__fields is None:
                self.fields()

        filter = re.sub(' +', ' ', filter)

        if not is_parentheses_balanced(filter):
            raise TuneSdkException("Invalid parameter 'filter' provided.")

        filter_no_parentheses = re.sub('[()]', ' ', filter)
        filter_no_parentheses = re.sub(' +', ' ', filter_no_parentheses)
        filter_no_parentheses = filter_no_parentheses.strip()

        filter_parts = filter_no_parentheses.split(' ')

        for filter_part in filter_parts:
            filter_part = filter_part.strip()

            if isinstance(filter_part, str) and not filter_part:
                continue

            m = re.match(r"\B'\w+'\B", filter_part)
            if (m is not None and (m.group(0) == filter_part)):
                continue

            if filter_part.isdigit():
                continue

            if filter_part in self.__filter_operations:
                continue

            if filter_part in self.__filter_conjunctions:
                continue

            m = re.match(r"[a-z0-9\.\_]+", filter_part)
            if (m is not None and (m.group(0) == filter_part)):

                if self.__validate_fields:
                    if filter_part in self.__fields:
                        continue

                else:
                    continue

            raise TuneSdkException(
                "Parameter 'filter' is invalid: '{}'.".format(
                    filter
                )
            )

        return "({})".format(filter)

    #  Validate 'format' parameter
    #  @param null|str format
    @staticmethod
    def validate_format(format):
        report_export_formats = [
            "csv",
            "json"
        ]
        if format is None:
            return format

        if (isinstance(format, str) and (format not in report_export_formats)):
            raise TuneSdkException(
                "Parameter 'format' is invalid: '{}'.".format(format)
            )

        return True

    #  Validate parameters of type datetime.
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

    #  Get SDK version
    #  @return string
    @staticmethod
    def version():
        """Get SDK version."""
        return __version__

    #  To string
    #  @return string
    def __str__(self):
        """For debug purposes, provide string representation of this object."""
        return "{}, {}".format(self.__controller, self.__api_key)

    @property
    def fields_recommended(self):
        return self.__fields_recommended

    @fields_recommended.setter
    def fields_recommended(self, value):
        """Provide data value."""
        self.__fields_recommended = value

    #  Helper function for fetching report document given provided
    #  job identifier.
    #
    #  Requesting for report url is not the same for all report endpoints.
    #
    #  @param string    export_controller   Export controller.
    #  @param string    export_action       Export status action.
    #  @param str       job_id              Job Identifier of report on queue.
    #  @param bool      verbose             For debugging purposes only.
    #  @param int       sleep               How long should sleep before next
    #                                       status request.
    #
    #  @return object @see Response
    #  @throws ValueError
    #  @throws TuneServiceException
    #
    def fetch(
        self,
        export_controller,
        export_action,
        job_id,
        verbose=False,
        sleep=10
    ):
        """
        Helper function for fetching report document given provided
        job identifier.
        """

        # export_controller
        if not export_controller or len(export_controller) < 1:
            raise ValueError(
                "Parameter 'export_controller' is not defined."
            )
        # export_action
        if not export_action or len(export_action) < 1:
            raise ValueError(
                "Parameter 'export_action' is not defined."
            )
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError(
                "Parameter 'job_id' is not defined."
            )

        export_worker = ReportExportWorker(
            export_controller,
            export_action,
            self.api_key,
            job_id,
            verbose,
            sleep
        )

        try:
            if verbose:
                print("Starting...")
            if export_worker.run():
                if verbose:
                    print("Completed...")
                    print(export_worker.response)
        except (KeyboardInterrupt, SystemExit):
            print("\n! Received keyboard interrupt, quitting.\n")
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

        if not export_worker.response \
           or export_worker.response.http_code != 200 \
           or export_worker.response.data["status"] == "fail":
            raise TuneServiceException(
                "Report request failed: {}".format(
                    str(export_worker.response)
                )
            )

        if not export_worker.response:
            raise TuneSdkException("Failed to get export status.")

        return export_worker.response

    #  Helper function for parsing export status response to
    #  gather report url.
    #  @param @see Response
    #  @return str Report Url
    @staticmethod
    def parse_response_report_url(
        response
    ):
        if not response:
            raise ValueError(
                "Parameter 'response' is not defined."
            )
        if not response.data:
            raise ValueError(
                "Parameter 'response.data' is not defined."
            )
        if "data" not in response.data:
            raise ValueError(
                "Parameter 'response.data['data'] is not defined."
            )
        if "url" not in response.data["data"]:
            raise ValueError(
                "Parameter 'response.data['data']['url'] is not defined."
            )

        url = response.data["data"]["url"]

        if isinstance(url, unicode):
            url = str(url)

        return url

    #  Helper function for parsing export response to gather job identifier.
    #  @param @see Response
    #  @return str Report Url
    @staticmethod
    def parse_response_report_job_id(
        response
    ):
        if not response:
            raise ValueError(
                "Parameter 'response' is not defined."
            )
        if not response.data:
            raise ValueError(
                "Parameter 'response.data' is not defined."
            )

        job_id = response.data

        if not job_id or len(job_id) < 1:
            raise Exception(
                "Failed to return Job ID: {}".format(str(response))
            )

        return job_id
