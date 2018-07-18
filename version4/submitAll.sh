#!/bin/bash

for dir in `ls`
  do
    if [ $dir != submitAll.sh ]
      then
	cd $dir
	./submitAll.sh
	cd ..
    fi
  done
