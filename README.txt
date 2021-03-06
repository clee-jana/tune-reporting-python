****************************************
tune-reporting-python
TUNE SDK for Python 2.7 and 3.0
Incorporate TUNE services.
Update:  $Date: 2015-12-11 20:56:46 $
Version: 1.0.9
****************************************

=============
Overview
=============

Python helper library for TUNE services.

The utility focus of this SDK is upon the Advertiser Reporting endpoints.

The second goal of the SDKs is to assure that our customers’ developers are
using best practices in gathering reports in the most optimal way.

=============
Documentation
=============

Please see documentation here:

https://developers.mobileapptracking.com/tune-api-sdks/

=============
Requirements
=============

-------------
Prerequisites
-------------

    * Python 2.7 or Python 3.0

-------------
Generate API Key
-------------

To use SDK, it requires you to generate API Key:
http://developers.mobileapptracking.com/generate-api-key/

=============
Installation
=============

You can install **tune-reporting-python** via PyPi or by installing from source.

-------------
Via PyPi using pip:
-------------

'tune_reporting' module is in PyPi: https://pypi.python.org/pypi/tune_reporting

Install from PyPi using pip: http://www.pip-installer.org/en/latest/, a
package manager for Python.

    pip install --upgrade tune-reporting

You may need to run the above commands with `sudo`.

Don't have pip installed? Try installing it, by running this from the command
line:

    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

-------------
Via ZIP file:
-------------

You can download the source code ZIP
https://github.com/MobileAppTracking/tune-reporting-python/zipball/master:

    python setup.py install

You may need to run the above commands with `sudo`.

-------------
SDK Examples
-------------

Run the following script to view execution of all examples:
```
    make installs
    make API_KEY=[API_KEY] examples
```

-------------
SDK Unittests
-------------

Run the following script to view execution of all unittests:
```
    make tests-installs
    make API_KEY=[API_KEY] tests
```

---------------------------
SDK Documentation -- Sphinx
---------------------------

The following will generate Sphinx documentation, see http://en.wikipedia.org/wiki/Sphinx_(documentation_generator), from Python codebase:

```
    make tests-installs
    make docs-sphinx
```

----------------------------
SDK Documentation -- Doxygen
----------------------------

The following will generate Doxygen documentation, see http://en.wikipedia.org/wiki/Doxygen, from Python codebase:

```
    make tests-installs
    make docs-doxygen
```

Requires installation of Doxygen: http://www.stack.nl/~dimitri/doxygen/index.html.

=============
License
=============

MIT License: http://opensource.org/licenses/MIT

=============
Reporting Issues
=============

We would love to hear your feedback.

Report issues using the Github Issue Tracker:
https://github.com/MobileAppTracking/tune-reporting-python/issues

or Email:
sdk@tune.com