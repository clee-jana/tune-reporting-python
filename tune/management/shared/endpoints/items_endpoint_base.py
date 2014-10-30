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

from .endpoint_base import (
    EndpointBase
)
from tune.shared import (
    TuneSdkException,
    TuneServiceException
)
from tune.management.shared.service import (
    TuneManagementClient
)


#  Base class intended for gathering from Advertiser Stats logs.
##
class ItemsEndpointBase(EndpointBase):
    """
    Base class intended for gathering from Advertiser Stats logs.
    """

    #  The constructor.
    #
    #  @param string controller         Tune Management API endpoint name.
    #  @param string api_key            Tune MobileAppTracking API Key.
    #  @param bool   validate_fields    Validate fields used by actions'
    #                                   parameters.
    def __init__(
        self,
        controller,
        api_key,
        validate_fields=False
    ):
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

    #  Counts all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string filter     Filter the results and apply conditions
    #                               that must be met for records to
    #                               be included in data.
    def count(
        self,
        filter=None
    ):
        if filter is not None and isinstance(filter, str):
            filter = EndpointBase.validate_filter(self, filter)

        return EndpointBase.call(
            self,
            action="count",
            query_string_dict={
                'filter': filter
            }
        )

    #  Finds all existing records that match filter criteria
    #  and returns an array of found model data.
    #
    #  @param string filter             Filter the results and apply conditions
    #                                   that must be met for records to be
    #                                   included in data.
    #  @param string fields             No value returns default fields, "*"
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
    def find(
        self,
        filter=None,
        fields=None,
        limit=None,
        page=None,
        sort=None
    ):
        if fields is not None:
            fields = EndpointBase.validate_fields(self, fields)
        if filter is not None:
            filter = EndpointBase.validate_filter(self, filter)
        if sort is not None:
            sort = EndpointBase.validate_sort(self, sort)

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

    #  Places a job into a queue to generate a report that will contain
    #  records that match provided filter criteria, and it returns a job
    #  identifier to be provided to action /export/download.json to download
    #  completed report.
    #
    #  @param string filter             Filter the results and apply conditions
    #                                   that must be met for records to be
    #                                   included in data.
    #  @param string fields             Provide fields if format is 'csv'.
    #  @param string format             Export format: csv, json
    #
    #  @return object
    def export(
        self,
        filter=None,
        fields=None,
        format=None
    ):
        if fields is not None:
            fields = EndpointBase.validate_fields(self, fields)
        if filter is not None:
            filter = EndpointBase.validate_filter(self, filter)
        if format is not None:
            EndpointBase.validate_format(format)

        return EndpointBase.call(
            self,
            action="find_export_queue",
            query_string_dict={
                'filter': filter,
                'fields': fields,
                'format': format
            }
        )

    #  Query status of insight reports. Upon completion will
    #  return url to download requested report.
    #
    #  @param string job_id    Provided Job Identifier to reference
    #                          requested report on export queue.
    def status(
        self,
        job_id              # Export queue identifier
    ):
        """Query status of insight reports. Upon completion will return url to
        download requested report.

            Args:
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

    #  Helper function for fetching report upon completion.
    #  Starts worker thread for polling export queue.
    #
    #  @param string mod_export_class Requesting report class for this export.
    #  @param string job_id           Provided Job Identifier to reference
    #                                 requested report on export queue.
    #  @param bool   verbose          Debug purposes only to view progress of
    #                                 job on export queue.
    #  @param int    sleep            Polling delay between querying job
    #                                 status on export queue.
    #
    #  @return object @see Response
    def fetch(
        self,
        job_id,
        verbose=False,
        sleep=10
    ):
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return EndpointBase.fetch(
            self,
            "tune.management.api.export",
            "Export",
            "download",
            job_id,
            verbose,
            sleep
        )
