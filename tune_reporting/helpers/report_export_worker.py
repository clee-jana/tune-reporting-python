"""
Tune Reports Export Status Worker
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  report_export_worker.py
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
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2014-12-10 17:11:05 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

import time

from tune_reporting.helpers import (
    TuneSdkException,
    TuneServiceException
)
from tune_reporting.base.service import (
    TuneManagementClient
)


#  Worker for handle polling of report request on export queue.
#
class ReportExportWorker(object):
    """Worker for handle polling of report request on export queue.
    """

    #
    #  @var string
    #
    __export_controller = None

    #
    #  @var string
    #
    __export_action = None

    #
    #  @var string
    #
    __api_key = None

    #
    #  @var string
    #
    __job_id = None

    #
    #  @var int
    #
    __sleep = None

    #
    #  @var boolean
    #
    __verbose = None

    #
    #  @var object @see TuneManagementResponse
    #
    __response = None

    #  The constructor
    #
    #  @param str    export_controller   Export controller.
    #  @param str    export_action       Export status action.
    #                                       status query.
    #  @param str   api_key              MobileAppTracking API Key
    #  @param str   job_id               Provided Job Identifier to
    #                                       reference requested report on
    #                                       export queue.
    #  @param bool     verbose              Debug purposes only to view
    #                                       progress of job on export queue.
    #  @param int      sleep                Polling delay between querying job
    #                                       status on export queue.
    def __init__(self,
                 export_controller,
                 export_action,
                 api_key,
                 job_id,
                 verbose=False,
                 sleep=10):
        """The constructor.

                :param str      export_controller:  Export controller.
                :param str      export_action:      Export status action.
                                                    status query.
                :param str      api_key:            MobileAppTracking API Key
                :param str      job_id:     Provided Job Identifier to
                                            reference requested report on
                                            export queue.
                :param bool     verbose:    Debug purposes only to view
                                            progress of job on export queue.
                :param int      sleep:  Polling delay between querying job
                                                    status on export queue.
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
        # api_key
        if not api_key or len(api_key) < 1:
            raise ValueError(
                "Parameter 'api_key' is not defined."
            )
        # job_id
        if not job_id or len(job_id) < 1:
            raise ValueError(
                "Parameter 'job_id' is not defined."
            )

        self.__export_controller = export_controller
        self.__export_action = export_action
        self.__api_key = api_key
        self.__job_id = job_id
        self.__sleep = sleep
        self.__verbose = verbose
        self.__response = None

    #  Poll export for download URL.
    #
    def run(self):
        """Poll status until status of "complete" or "fail" to
        gather download URL for report export.

            :return: True upon success.
            :rtype: bool
        """
        status = None
        response = None
        attempt = 0

        client = TuneManagementClient(
            self.__export_controller,
            self.__export_action,
            self.__api_key,
            query_string_dict={
                'job_id': self.__job_id
            }
        )

        try:
            while True:
                client.call()

                response = client.response

                # Failed to return response.
                if not response:
                    raise TuneSdkException(
                        "No response returned from export request."
                    )

                # Failed to get successful service response.
                if response.http_code != 200 or response.errors:
                    raise TuneServiceException(
                        "Service failed: {}: {}".format(
                            response.http_code,
                            str(response)
                        )
                    )

                # Failed to get data.
                if not response.data:
                    raise TuneSdkException(
                        "No response data returned from export,"
                        "response: {}".format(
                            str(response)
                        )
                    )

                # Failed to get status.
                if "status" not in response.data:
                    raise TuneSdkException(
                        "Export data does not contain report 'status',"
                        "response: {}".format(
                            str(response)
                        )
                    )

                # Get status.
                status = response.data["status"]
                if status == "complete" or status == "fail":
                    break

                attempt += 1
                if self.__verbose:
                    print(
                        "= attempt: {}, response: {}".format(attempt, response)
                    )

                time.sleep(self.__sleep)
        except (TuneSdkException, TuneServiceException):
            raise
        except Exception as ex:
            raise TuneSdkException(
                "Failed get export status: (Error:{0})".format(
                    str(ex)
                ),
                ex
            )

        if self.__verbose:
            print("= response: {}".format(response))

        self.__response = response

        return True

    @property
    def response(self):
        """Property that will hold completed report downloaded
        from Management API service.

            :return: Response
            :rtype: TuneManagementResponse
        """
        return self.__response
