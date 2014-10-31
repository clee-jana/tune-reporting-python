****************************************
tune-api-python
Tune API SDK for Python 2.7 and 3.0
Incorporate Tune API services.
Update:  2014-10-31
Version: 0.9.11
****************************************

=============
Overview
=============

The utility focus of the SDKs is upon the Advertiser Reporting endpoints. Even though the the breadth of the Management API goes beyond just reports, it is these endpoints that our customers primarily access. The second goal of the SDKs is to assure that our customers’ developers are using best practices in gathering reports in the most optimal way.

=============
Documentation
=============

Please see documentation here:

.. Tune API SDKs: https://developers.mobileapptracking.com/tune-api-sdks/

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
.. Generate API Key: http://developers.mobileapptracking.com/generate-api-key/

=============
Installation
=============

You can install `tune-api-python` via PyPi or by installing from source.

-------------
Via PyPi using pip:
-------------

Install from PyPi using `pip`, a package manager for Python.
.. pip: http://www.pip-installer.org/en/latest/

.. code-block:: bash
    $ pip install tune


Don't have pip installed? Try installing it, by running this from the command
line:

.. code-block:: bash
    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

-------------
Via ZIP file:
-------------

you can download the source code ZIP
.. ZIP: https://github.com/MobileAppTracking/tune-api-python/zipball/master

.. code-block:: bash
    $ python setup.py install

You may need to run the above commands with `sudo`.

=============
Code Samples
=============
-------------
SDK Examples
-------------

Run the following script to view execution of all examples:
.. code-block:: bash
    $ make installs
    $ make api_key=[API_KEY] examples
    
-------------
SDK Unittests
-------------

Run the following script to view execution of all unittests:
.. code-block:: bash
    $ make tests-installs
    $ make api_key=[API_KEY] tests
    
-------------
SDK Document
-------------

Run the following script to generate Doxygen-based documentation:
.. code-block:: bash
    $ make docs
    
Requires installation of Doxygen: 
.. Doxygen: http://www.stack.nl/~dimitri/doxygen/index.html

=============
License
=============

.. MIT License: http://opensource.org/licenses/MIT

=============
Reporting Issues
=============

We would love to hear your feedback.

Report issues using the Github Issue Tracker:
.. Github Issue Tracker: https://github.com/MobileAppTracking/tune-api-python/issues

or Email:
.. sdk@tune.com: mailto:sdk@tune.com