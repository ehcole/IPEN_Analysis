#!/bin/bash

for dir in `ls`
  do
    if [[ $dir != k_eff.py && $dir != submitAll.sh ]]
	then
	cd $dir
	qsub *.pbs
	cd ..
    fi
  done
