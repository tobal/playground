#!/usr/bin/env bash

for i in {1..100};
do
    ./overflow $i | ./a.out
done
