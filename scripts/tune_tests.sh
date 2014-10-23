#!/bin/bash

if [ $# -ne 1 ]; then
    echo usage: $0 api_key
    exit 1
fi

api_key=$1

python ./tests/tune_tests.py $api_key