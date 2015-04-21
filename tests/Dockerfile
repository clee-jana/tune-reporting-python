FROM tunesdk/tune-reporting-python-setup:latest

MAINTAINER Jeff Tanner jefft@tune.com

WORKDIR /data/tune-reporting-python

RUN python -V

RUN echo API_KEY

RUN pip install -r requirements.txt && \
    python setup.py clean && \
    python setup.py build && \
    python setup.py install

ENTRYPOINT ["python"]
CMD ["./tests/tune_reporting_tests.py", API_KEY]
