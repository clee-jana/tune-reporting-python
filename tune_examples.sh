#!/bin/bash

if [ $# -ne 1 ]; then
    echo usage: $0 api_key
    exit 1
fi

api_key=$1

python3 ./examples_execute.py $api_key