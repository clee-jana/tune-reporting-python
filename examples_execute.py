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

from examples.tune.management.shared import (
    ExampleClient
    )

from examples.tune.management.api import (
    ExampleClicks,
    ExampleEventItems,
    ExampleEvents,
    ExampleInstalls,
    ExamplePostbacks,
    ExampleActuals,
    ExampleCohort,
    ExampleRetention
    )
 
if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError("Provide API Key to execute Tune Management API example {}.".format(sys.argv[0]))
        api_key = sys.argv[1]

        example = ExampleClient()
        example.run(api_key)
        
        example = ExampleClicks()
        example.run(api_key)
        
        example = ExampleEventItems()
        example.run(api_key)
        
        example = ExampleEvents()
        example.run(api_key)
        
        example = ExampleInstalls()
        example.run(api_key)
        
        example = ExamplePostbacks()
        example.run(api_key)
        
        example = ExampleActuals()
        example.run(api_key)
        
        example = ExampleCohort()
        example.run(api_key)
        
        example = ExampleRetention()
        example.run(api_key)

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise