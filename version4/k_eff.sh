#!/bin/bash
for dir in `ls`
  do
    if [[ $dir != "k_eff.sh" && $dir != "submitAll.sh" ]]
	then
	  echo $dir
	  cd $dir
	  python k_eff.py
	  cd ..
    fi
  done
