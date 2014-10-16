"""
Worker thread for polling download status of requested report.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## report_export_worker.py
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

import time
import subprocess

from tune.common import (
    TuneSdkException,
    TuneServiceException
)
from threading import (
    Thread,
    current_thread
)

class ReportExportWorker(Thread):
    """
    Threaded worker for handle polling of report request on export queue.
    """

    ## The constructor
    #
    #  @param string   mod_export_class    Reference class name for worker to
    #                                      perform download status query.
    #  @param string   mod_export_function Reference class function name for worker
    #                                      to perform download status query.
    #  @param string   api_key             MobileAppTracking API Key
    #  @param string   job_id              Provided Job Identifier to reference
    #                                      requested report on export queue.
    #  @param bool     verbose             Debug purposes only to view progress
    #                                      of job on export queue.
    #  @param int      sleep               Polling delay between querying job
    #                                      status on export queue.
    def __init__(
             self,
             mod_export_namespace,
             mod_export_class,
             mod_export_function,
             api_key,
             job_id,
             verbose=False,
             sleep=60 # seconds
         ):
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError("Parameter 'api_key' is not defined.")

        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        loaded_mod = __import__(mod_export_namespace, fromlist=[mod_export_namespace])

        # Load it from imported module
        loaded_class = getattr(loaded_mod, mod_export_class)

        # Create an instance of it
        instance = loaded_class(api_key)

        Thread.__init__(self)
        self.__api_key = api_key
        self.__job_id = job_id
        self.__sleep = sleep
        self.__report = None
        self.__verbose = verbose
        self.__class_export = instance
        self.__process = None
        self.__mod_export_name = mod_export_namespace
        self.__mod_export_class = mod_export_class
        self.__mod_export_function = mod_export_function
        self.__response = None

    ## Poll export for download URL. Method representing
    #   the thread's activity.
    #
    def run(self):
        cmd = ["bash", 'process.sh']
        self.__process = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
        status = "running"
        response = None
        attempt = 0

        while True:
            response = getattr(self.__class_export, self.__mod_export_function)(
                    self.__job_id
                )

            if not response:
                raise TuneSdkException(
                    "No response returned from export request."
                )

            if not response.data:
                raise TuneSdkException(
                    "No response data returned from export. Request URL: {}".format(
                        response.request_url
                    )
                )

            if response.http_code != 200:
                raise TuneServiceException(
                    "Request failed: HTTP Error Code: {}: {}".format(
                        response.http_code,
                        response.request_url
                    )
                )

            status = response.data["status"]
            if status == "complete" or status == "fail":
                break

            attempt += 1
            if self.__verbose:
                print("= thread id {}: attempt: {}, response: {}".format(
                        current_thread().ident,
                        attempt,
                        response
                    )
                )

            time.sleep(self.__sleep)

        if self.__verbose:
            print("= thread id {}: response: {}".format(
                    current_thread().ident,
                    response
                )
            )

        self.__response = response

    def stop(self):
        """Terminate thread."""
        if self.__verbose:
            print("= {}: Trying to stop".format(current_thread()))
        if self.__process is not None:
            self.__process.terminate()
            self.__process = None

    @property
    def response(self):
        """
        Property that will hold completed report downloaded
        from Management API service.
        """
        return self.__response
