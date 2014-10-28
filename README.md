<h1>tune-api-python</h1>
<h2>Tune API Python SDK for Python 2.7 and 3.0</h2>
<h3>Incorporate Tune API services.</h3>
<h4>Update:  2014-10-27</h4>
<h4>Version: 0.9.7</h4>
===

## Overview

The utility focus of the SDKs is upon the Advertiser Reporting endpoints. Even though the the breadth of the Management API goes beyond just reports, it is these endpoints that our customers primarily access. The second goal of the SDKs is to assure that our customers’ developers are using best practices in gathering reports in the most optimal way.

## Documentation

Please see documentation here:

[Tune API SDKs](https://developers.mobileapptracking.com/tune-api-sdks/)

<a name="sdk_requirements"></a>
## SDK Requirements

<a name="sdk_prerequisites"></a>
#### Prerequisites

    * Python 2.7 or Python 3.0

<a name="generate_api_key"></a>
#### Generate API Key

To use SDK, it requires you to [Generate API Key](http://developers.mobileapptracking.com/generate-api-key/)

<a name="sdk_installation"></a>
## Installation

You can install **tune-api-python** via PyPi or by installing from source.

<a name="sdk_installation_pip"></a>
#### Via PyPi using pip:

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

```bash
    $ pip install tune
```

Don't have pip installed? Try installing it, by running this from the command
line:

```bash
    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

<a name="sdk_installation_zip"></a>
#### Via ZIP file:

You can [download the source code
(ZIP)](https://github.com/MobileAppTracking/tune-api-python/zipball/master "tune-api-python
source code") for `tune-api-python`, and then run:

```bash
    python setup.py install
```

You may need to run the above commands with `sudo`.

<a name="sdk_examples"></a>
## Code Samples

```bash
    $ ./scripts/tune_examples.sh [API_KEY]
```

<a name="license"></a>
## License

[MIT License](http://opensource.org/licenses/MIT)

<a name="sdk_reporting_issues"></a>
## Reporting Issues

We would love to hear your feedback.

Report issues using the [Github Issue Tracker](https://github.com/MobileAppTracking/tune-api-python/issues) or Email [sdk@tune.com](mailto:sdk@tune.com).
