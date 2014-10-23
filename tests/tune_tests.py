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

from test_client import TestClient
from test_clicks import TestClicks
from test_event_items import TestEventItems
from test_events import TestEvents
from test_installs import TestInstalls
from test_postbacks import TestPostbacks
from test_actuals import TestActuals
from test_cohort import TestCohort
from test_retention import TestRetention

def suite(api_key):

    suite = unittest.TestSuite()

    suite.addTest (TestClient(api_key))
    suite.addTest (TestClicks(api_key))
    suite.addTest (TestEventItems(api_key))
    suite.addTest (TestEvents(api_key))
    suite.addTest (TestInstalls(api_key))
    suite.addTest (TestPostbacks(api_key))
    suite.addTest (TestActuals(api_key))
    suite.addTest (TestCohort(api_key))
    suite.addTest (TestRetention(api_key))

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