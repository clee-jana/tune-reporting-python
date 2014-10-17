"""
Tune Management API endpoint /export/
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (c) 2014 Tune, Inc
#    All rights reserved.
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction, including
#    without limitation the rights to use, copy, modify, merge, publish,
#    distribute, sublicense, and/or sell copies of the Software, and to permit
#    persons to whom the Software is furnished to do so, subject to the
#    following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
#    Python 3.0
#
# @category  Tune
# @package   Tune_PHP_SDK
# @author    Jeff Tanner <jefft@tune.com>
# @copyright 2014 Tune (http://www.tune.com)
# @license   http://opensource.org/licenses/MIT The MIT License (MIT)
# @version   0.9.2
# @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

from tune.management.shared import (
    ReportsBase
)

## /export
#
class Export(ReportsBase):
    """Tune Management API controller '/export/'."""

    ## Constructor
    #  @param str api_key  Tune MobileAppTracking API Key
    def __init__(self, api_key):
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        self.__api_key = api_key
        ReportsBase.__init__(
            self,
            controller="export",
            api_key=api_key,
            filter_debug_mode=False,
            filter_test_profile_id=False
        )

    ## Request status from export queue for report. When completed, url will be provided for downloading report.
    #  @param str job_id   Job identifier assigned for report export.
    #  @return object @see Response
    def download(
        self,
        job_id              # Export queue identifier
    ):
        """
        Action 'download' for polling export queue for status information on
        request report to be exported.
        """
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return ReportsBase.call(
            self,
            action="download",
            query_string_dict={
                'job_id': job_id
            }
        )

    #  Helper function for fetching report upon completion.
    #  Starts worker thread for polling export queue.
    #
    #  @param string job_id        Job identifier assigned for report export.
    #  @param string report_format Report export content format expectation: csv, json
    #  @param bool   verbose       For debug purposes to monitor job export completion status.
    #  @param int    sleep         Polling delay for checking job completion status.
    #
    #  @return object Document contents
    def fetch(
        self,
        job_id,
        report_format,
        verbose=False,
        sleep=60, # seconds
    ):
        if not self.__api_key or len(self.__api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return ReportsBase.fetch(
            self,
            "tune.management.api.export",
            "Export",
            "download",
            job_id,
            report_format,
            verbose,
            sleep
        )

    ## Helper function for parsing export status response to gather report url.
    #  @param @see Response
    #  @return str Report Url
    @staticmethod
    def parse_response_url(
        response
    ):
        print("parse_response_url: {}".format(response))

        if not response:
            raise ValueError("Parameter 'response' is not defined.")
        if not response.data:
            raise ValueError("Parameter 'response.data' is not defined.")
        if "data" not in response.data:
            raise ValueError("Parameter 'response.data['data'] is not defined.")
        if "url" not in response.data["data"]:
            raise ValueError("Parameter 'response.data['data']['url'] is not defined.")

        url = response.data["data"]["url"]

        return url
