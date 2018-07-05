#!/bin/bash
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-011/IPEN-011.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-011/IPEN-011.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-008/IPEN-008.h5
