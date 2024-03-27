#!/bin/bash

FROM=$(pwd)/storage
TO=$(pwd)/public/storage

if [[ $1 == "remove" ]]; then
    rm $TO -v
elif [[ -e $TO ]]; then
    echo $TO "already exists"
else
    ln -s $FROM $TO -v
fi
