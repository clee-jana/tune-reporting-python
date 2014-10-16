"""
Tune SDK
"""
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
#    Python 3.0
#
# @category  Tune
# @package   Tune_PHP_SDK
# @author    Jeff Tanner <jefft@tune.com>
# @copyright 2014 Tune (http://www.tune.com)
# @license   http://opensource.org/licenses/MIT The MIT License (MIT)
# @version   0.9.1
# @link      https://developers.mobileapptracking.com Tune Developer Community @endlink
#

__title__ = 'tune'
__build__ = 0x000090
__author__ = 'Tune, Inc.'
__license__ = 'LICENSE.md'
__copyright__ = 'Copyright 2014 Tune, Inc'

import sys

if sys.version_info < (3, 0):
    sys.stderr.write("[%s] - Error: Your Python interpreter must be %d.%d "
                    "or greater (within major version %d)\n"
                    % (sys.argv[0], 3, 0, 3))
    sys.exit(-1)

try:
    from . import common
    from . import management
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise
