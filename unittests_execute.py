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
#    Python 3.3
#
#    category    Tune
#    package     SDK
#    version     2014-10-05
#    copyright   Copyright (c) 2014, Tune (http://www.tune.com)
#

import sys
import unittest

from unittests.tune import (
    UnittestTuneManagementClient,
    UnittestReportsLogsClicks,
    UnittestReportsLogsEventItems,
    UnittestReportsLogsEvents,
    UnittestReportsLogsInstalls,
    UnittestReportsLogsPostbacks,
    UnittestReportsActuals,
    UnittestReportsCohort,
    UnittestReportsRetention
)

def suite(api_key):

    suite = unittest.TestSuite()

    suite.addTest (UnittestTuneManagementClient(api_key))
    suite.addTest (UnittestReportsLogsClicks(api_key))
    suite.addTest (UnittestReportsLogsEventItems(api_key))
    suite.addTest (UnittestReportsLogsEvents(api_key))
    suite.addTest (UnittestReportsLogsInstalls(api_key))
    suite.addTest (UnittestReportsLogsPostbacks(api_key))
    suite.addTest (UnittestReportsActuals(api_key))
    suite.addTest (UnittestReportsCohort(api_key))
    suite.addTest (UnittestReportsRetention(api_key))

    return suite


if __name__ == '__main__':
    
    try:
        if len(sys.argv) > 1:
            api_key = sys.argv.pop()

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
    
    runner = unittest.TextTestRunner()
    
    test_suite = suite(api_key)
    
    runner.run (test_suite)