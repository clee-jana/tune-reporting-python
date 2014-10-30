#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (c) 2014 Tune, Inc
#    All rights reserved.
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#    THE SOFTWARE.
#
#    Python 2.7
#
#    category    Tune
#    package     SDK
#    version     2014-10-28
#    copyright   Copyright (c) 2014, Tune (http://www.tune.com)
#

import sys

from example_client_account_users import ExampleClientAccountUsers
from example_reports_clicks import ExampleReportsClicks
from example_reports_event_items import ExampleReportsEventItems
from example_reports_events import ExampleReportsEvents
from example_reports_installs import ExampleReportsInstalls
from example_reports_postbacks import ExampleReportsPostbacks
from example_reports_actuals import ExampleReportsActuals
from example_reports_cohort import ExampleReportsCohort
from example_reports_retention import ExampleReportsRetention

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                "Provide API Key to execute Tune Management API example {}.".format(sys.argv[0])
                )

        api_key = sys.argv[1]

        example = ExampleClientAccountUsers()
        example.run(api_key)

        example = ExampleReportsClicks()
        example.run(api_key)

        example = ExampleReportsEventItems()
        example.run(api_key)

        example = ExampleReportsEvents()
        example.run(api_key)

        example = ExampleReportsInstalls()
        example.run(api_key)

        example = ExampleReportsPostbacks()
        example.run(api_key)

        example = ExampleReportsActuals()
        example.run(api_key)

        example = ExampleReportsCohort()
        example.run(api_key)

        example = ExampleReportsRetention()
        example.run(api_key)

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
