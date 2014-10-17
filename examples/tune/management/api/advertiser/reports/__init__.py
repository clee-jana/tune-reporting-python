#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
## __init__.py
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
#  You can use the Logs report in the same way as the Actuals reports, but
#  instead of being aggregated by request type, the Logs report contains the
#  logs of each individual request (including the logs for Clicks, Installs,
#  Updates, Events, Event Items, and Postback URLs). The log data is available
#  in real-time, so you can use it for testing, debugging, and ensuring that
#  all measurement and attribution continues to operate smoothly. MAT updates
#  the Logs report every 1 minute.
#
#  @link https://platform.mobileapptracking.com/#!/Advertiser/Reports/logs?type=eventItems @endlink
#
#  Event Items API call: stats/event/items
#

from .logs import (
    ExampleClicks,
    ExampleEventItems,
    ExampleEvents,
    ExampleInstalls,
    ExamplePostbackUrls,
    ExampleUpdates
)
from .example_actuals import (ExampleActuals)
from .example_cohort import (ExampleCohort)
from .example_retention import (ExampleRetention)