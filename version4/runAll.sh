#!/bin/bash

for dir in `ls`
  do
    if [ $dir != runAll.sh ]
      then
	cd $dir
	./submitAll.sh
	cd ..
    fi
  done
