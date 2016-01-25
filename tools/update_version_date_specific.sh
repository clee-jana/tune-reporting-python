#!/bin/bash

export TZ=America/Los_Angeles

files=`find $1 -type f -name '*.py'`

today=`date +%F' '%T' '%Z`

echo $files

echo $today

for f in $files
do
    if [ -f $f ]; then
        printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"
        sed -r -i "$sed_repl" $f
    fi
done