"""
Tune Mangement Items Endpoint base
==================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  items_endpoint_base.py
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

from .endpoint_base import (
    EndpointBase
)
from tune.management.shared.service import (
    TuneManagementClient
)


## Base class intended for gathering from Advertiser Stats logs.
##
class ItemsEndpointBase(EndpointBase):
    """
    Base class intended for gathering from Advertiser Stats logs.
    """

    ## The constructor.
    #
    #  @param str controller         Tune Management API endpoint name.
    #  @param str api_key            Tune MobileAppTracking API Key.
    #  @param bool   validate_fields    Validate fields used by actions'
    #                                   parameters.
    def __init__(self,
                 controller,
                 api_key,
                 validate_fields=False):
        """The constructor.

            :param str controller:       Tune Management API endpoint name.
            :param str api_key:          Tune MobileAppTracking API Key.
            :param bool validate_fields: Validate fields used by actions'
                                            parameters.
        """
        # controller
        if not controller or len(controller) < 1:
            raise ValueError("Parameter 'controller' is not defined.")
        # api key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        EndpointBase.__init__(
            self,
            controller,
            api_key,
            validate_fields
        )

    ## Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str filter     Filter the results and apply conditions
    #                               that must be met for records to
    #                               be included in data.
    def count(self,
              filter=None):
        """Counts all existing records that match filter criteria
        and returns an array of found model data.

            :param str    filter:         Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :return: (TuneManagementResponse)
        """
        if filter is not None and isinstance(filter, str):
            filter = self._validate_filter(filter)

        return EndpointBase.call(
            self,
            action="count",
            query_string_dict={
                'filter': filter
            }
        )

    ## Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param str filter             Filter the results and apply conditions
    #                                   that must be met for records to be
    #                                   included in data.
    #  @param str fields             No value returns default fields, "*"
    #                                   returns all available fields,
    #                                   or provide specific fields.
    #  @param int    limit              Limit number of results, default 10,
    #                                   0 shows all.
    #  @param int    page               Pagination, default 1.
    #  @param dict   sort               Expression defining sorting found
    #                                   records in result set endpoint_base
    #                                   upon provided fields and its modifier
    #                                   (ASC or DESC).
    #  @return object
    def find(self,
             filter=None,
             fields=None,
             limit=None,
             page=None,
             sort=None):
        """Finds all existing records that match filter criteria
        and returns an array of found model data.

            :param str    filter:         Filter the results and apply
                                            conditions that must be met for
                                            records to be included in data.
            :param str    fields:         No value returns default fields,
                                            "*" returns all available fields,
                                            or provide specific fields.
            :param int    limit:           Limit number of results, default
                                            10.
            :param int    page:           Pagination, default 1.
            :param array  sort:           Sort by field name, ASC (default)
                                            or DESC.
            :return: (TuneManagementResponse)
        """
        if fields is not None:
            fields = self._validate_fields(fields)
        if filter is not None:
            filter = self._validate_filter(filter)
        if sort is not None:
            sort = self._validate_sort(sort)

        return EndpointBase.call(
            self,
            action="find",
            query_string_dict={
                'filter': filter,
                'fields': fields,
                'limit': limit,
                'page': page,
                'sort': sort
            }
        )

    ## Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param str filter             Filter the results and apply conditions
    #                                   that must be met for records to be
    #                                   included in data.
    #  @param str fields             Provide fields if format is 'csv'.
    #  @param str format             Export format: csv, json
    #
    #  @return object
    def export(self,
               filter=None,
               fields=None,
               format=None):
        """Places a job into a queue to generate a report that will contain
        records that match provided filter criteria, and it returns a job
        identifier to be provided to action /export/download.json to download
        completed report.

            :param str    filter:     Filter the results and apply
                                        conditions that must be met for
                                        records to be included in data.
            :param str    fields:     No value returns default fields,
                                        "*" returns all available fields,
                                        or provide specific fields.
            :param str    format:     Export format for downloaded report:
                                        choices: json, csv.
            :return: (TuneManagementResponse)
        """
        if fields is not None:
            fields = self._validate_fields(fields)
        if filter is not None:
            filter = self._validate_filter(filter)
        if format is not None:
            self._validate_format(format)

        return EndpointBase.call(
            self,
            action="find_export_queue",
            query_string_dict={
                'filter': filter,
                'fields': fields,
                'format': format
            }
        )

    ## Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param str job_id    Provided Job Identifier to reference
    #                          requested report on export queue.
    def status(self,
               job_id):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            :param str    job_id:     Provided Job Identifier to reference.
            :return: (TuneManagementResponse)
        """

        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        client = TuneManagementClient(
            controller="export",
            action="download",
            api_key=self.api_key,
            query_string_dict={
                'job_id': job_id
            }
        )

        return client.call()

    ## Helper function for fetching report upon completion.
    #
    #  @param str job_id           Provided Job Identifier to reference
    #                                 requested report on export queue.
    #  @param bool   verbose          Debug purposes only to view progress of
    #                                 job on export queue.
    #  @param int    sleep            Polling delay between querying job
    #                                 status on export queue.
    #
    #  @return object @see TuneManagementResponse
    def fetch(self,
              job_id,
              verbose=False,
              sleep=10):
        """Helper function for fetching report upon completion.

            :param str    job_id:     Provided Job Identifier to reference
                                        requested report on export queue.
            :param bool   verbose:    Debug purposes only to view progress of
                                        job on export queue.
            :param int    sleep:      Polling delay between querying job
                                        status on export queue.
            :return: (TuneManagementResponse)
        """
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return self._fetch(
            "export",
            "download",
            job_id,
            verbose,
            sleep
        )
