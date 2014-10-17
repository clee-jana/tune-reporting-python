"""
Downloads remote JSON file from Amazon S3 repository and creates a reader.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## report_reader_json.py
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
#  @package   Tune_PHP_SDK
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2014 Tune (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   0.9.3
#  @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

import json
import sys

if sys.version_info[0] == 3:
    import urllib.request
else:
    import urllib2

from .report_reader_base import (
    ReportReaderBase
)
from tune.shared import (
    TuneSdkException,
    TuneServiceException,
    TuneProxy
)

class ReportReaderJSON(ReportReaderBase):
    """Helper class for reading reading remote JSON file"""

    ## The constructor
    #  @param string report_url Download report URL
    #                           of requested report to be exported.
    def __init__(self, report_url):
        ReportReaderBase.__init__(self, report_url)

    ## Using provided report download URL, extract JSON contents.
    #
    def read(self):
        """Read JSON data provided remote path report_url."""
        self.data = None

        proxy = TuneProxy(self.report_url)
        proxy.execute()
        report_content = proxy.response.read()
        report_utf8_str = report_content.decode("utf8")
        self.data = json.loads(report_utf8_str)

