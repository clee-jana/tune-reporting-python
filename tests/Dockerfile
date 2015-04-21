FROM tunesdk/tune-reporting-python-setup:latest

MAINTAINER Jeff Tanner jefft@tune.com

WORKDIR /data/tune-reporting-python

RUN python -V

RUN pip install -r requirements.txt && \
    python setup.py clean && \
    python setup.py build && \
    python setup.py install

ENTRYPOINT ["python"]
CMD ["./tests/tune_reporting_tests.py", "b951b30cc17b6a77dad4f1ef1471bd5d"]
