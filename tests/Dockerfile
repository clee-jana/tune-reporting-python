FROM tunesdk/tune-reporting-python-setup:latest

MAINTAINER Jeff Tanner jefft@tune.com

WORKDIR /data/tune-reporting-python

RUN python -V && \
    echo $API_KEY && \
    pip install -r requirements.txt && \
    python setup.py clean && \
    python setup.py build && \
    python setup.py install

CMD ["python ./tests/tune_reporting_tests.py $API_KEY"]
