"""
Tune SDK shared helper functions.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## helpers.py
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

import sys
from datetime import datetime

## Check Python Version
#
def python_check_version(required_version):
    """Check Python Version"""
    current_version = sys.version_info
    if (current_version[0] == required_version[0]
        and current_version[1] >= required_version[1]):
        pass
    else:
        sys.stderr.write(
            "[%s] - Error: Your Python interpreter must be "
            "%d.%d or greater (within major version %d)\n"
            % (
            sys.argv[0],
                required_version[0],
                required_version[1],
                required_version[0]
            )
        )
        sys.exit(-1)
    return 0

##
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

##
def validate_datetime(date_time_text):
    try:
        datetime.strptime(date_time_text, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False
