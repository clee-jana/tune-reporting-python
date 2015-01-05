"""
TUNE SDK Configuration Class
=============================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sdk_config.py
#
#  Copyright (c) 2014 TUNE, Inc.
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
#  @copyright 2014 TUNE (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @version   $Date: 2015-01-03 08:41:07 $
#  @link      https://developers.mobileapptracking.com/tune-reporting-sdks @endlink
#

import sys
import os.path

try:
    import configparser
    import collections
except ImportError as exc:
    sys.stderr.write("Error: failed to import module ({})".format(exc))
    raise

class SdkConfig(object):
    """Singleton class for reading SDK configuration file.
    """

    SDK_CONFIG_FILENAME = 'tune_reporting_sdk.config'
    class __SdkConfig:
        """SDK Configuration Singleton instance class."""

        __filepath = None
        __config = None
        __sections_dict = None

        def __init__(self, filepath):
            self.__filepath = filepath
            self.__config = configparser.ConfigParser()
            self.__config.read(self.whereConfig)
            self.__sections_dict = self.__as_dict()

        @property
        def filepath(self):
            """Get property filepath."""
            return self.__filepath

        def __as_dict(self):
            """Generate dictionary of the contents SDK Configuration File."""
            if self.__config is None:
                raise ValueError("Configuration not defined.")
            sections_dict = collections.defaultdict(dict)
            for section_items in self.__config.sections():
                sections_dict[section_items] = dict(**self.__config[section_items])
            return sections_dict

        @property
        def sections_dict(self):
            """Get property dictionary of sections."""
            return self.__sections_dict

        @property
        def config(self):
            """Get property of parsed SDK configuration file."""
            return self.__config

        @property
        def whereConfig(self):
            """Get property location of SDK configuration file."""
            if not os.path.exists(self.__filepath):
                raise ValueError("SDK Configuration filepath invalid: '{0}'".format(self.__filepath))

            return self.__filepath

        @property
        def filepath(self):
            """Get property filepath."""
            return self.__filepath

        @property
        def config(self):
            """Get property of section TUNE_REPORTING within a dictionary."""
            return self.sections_dict["TUNE_REPORTING"]

        def __str__(self):
            """pretty print contents of SDK Configuration file into a string."""
            str_builder = ""
            str_builder += "filepath: {}".format(self.__filepath)
            str_builder += "\n"
            for key_section in self.sections_dict:
                str_builder += "{\n"
                for key_item in self.sections_dict[key_section]:
                    value_item = self.sections_dict[key_section][key_item]
                    str_builder += "\t[%s] '%s': '%s'\n" % (key_section, key_item, value_item)
                str_builder += "}"
            return str_builder

        @property
        def api_key(self):
            """Get TUNE MobileAppTracking API Key from SDK Configuration File."""
            if "tune_reporting_api_key_string" not in self.sections_dict["TUNE_REPORTING"]:
                return None
            api_key = self.sections_dict["TUNE_REPORTING"]["tune_reporting_api_key_string"]
            if isinstance(api_key, unicode):
                api_key = str(api_key)
            return api_key

        @api_key.setter
        def api_key(self, value):
            """Set TUNE MobileAppTracking API Key from SDK Configuration File."""
            if "tune_reporting_api_key_string" not in self.sections_dict["TUNE_REPORTING"]:
                return None
            self.sections_dict["TUNE_REPORTING"]["tune_reporting_api_key_string"] = value

        @property
        def validate_fields(self):
            """Get boolean flag to validate fields from SDK Configuration File."""
            if "tune_reporting_validate_fields_boolean" not in self.sections_dict["TUNE_REPORTING"]:
                return False
            verify_fields = self.sections_dict["TUNE_REPORTING"]["tune_reporting_validate_fields_boolean"]
            if isinstance(verify_fields, unicode):
                verify_fields = str(verify_fields)
            return verify_fields == "true"

        @property
        def status_sleep(self):
            """Get number of seconds to sleep between status requests from SDK Configuration File."""
            if "tune_reporting_export_status_sleep_seconds" not in self.sections_dict["TUNE_REPORTING"]:
                return 0
            status_sleep = self.sections_dict["TUNE_REPORTING"]["tune_reporting_export_status_sleep_seconds"]
            if isinstance(status_sleep, unicode):
                status_sleep = str(status_sleep)
            return int(status_sleep)

        @property
        def status_timeout(self):
            """Get number of seconds to timeout status requests from SDK Configuration File."""
            if "tune_reporting_export_status_timeout_seconds" not in self.sections_dict["TUNE_REPORTING"]:
                return 0
            status_timeout = self.sections_dict["TUNE_REPORTING"]["tune_reporting_export_status_timeout_seconds"]
            if isinstance(status_timeout, unicode):
                status_timeout = str(status_timeout)
            return int(status_timeout)

    instance = None

    def __new__(cls, *args, **kwargs): # __new__ always a classmethod
        #print cls
        #print "args is", args
        #print "kwargs is", kwargs

        if not SdkConfig.instance:
            SdkConfig.instance = SdkConfig.__SdkConfig(kwargs.pop('filepath'))
        return SdkConfig.instance

if __name__ == '__main__':
    dirname = os.path.split(__file__)[0]
    dirname = os.path.dirname(dirname)
    dirname = os.path.dirname(dirname)
    filepath = os.path.join(dirname, "config", SdkConfig.SDK_CONFIG_FILENAME)
    filepath = os.path.abspath(filepath)

    s1=SdkConfig(filepath=filepath)
    s2=SdkConfig()

    s1.filepath = filepath

    if(id(s1)==id(s2)):
        print "Same identifier"
    else:
        print "Different identifier"

    if(s1.filepath==s2.filepath):
        print "Same filepath"
    else:
        print "Different filepath"

    if(s1.config["tune_reporting_api_key_string"]==s2.config["tune_reporting_api_key_string"]):
        print "Same config"
    else:
        print "Different config"

    print s2
