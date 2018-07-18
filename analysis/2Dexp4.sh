#!/bin/bash
for dir in `ls /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4`
 do 
    if [[ $dir != "k_eff.sh" && $dir != "runAll.sh" ]]
	then
	    echo $dir
	    python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/$dir/k_eff.py
    fi
 done

