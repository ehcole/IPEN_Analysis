#!/bin/bash
echo
echo "3D model:"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-008/IPEN-008.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-011/IPEN-011.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-008/IPEN-008.h5
echo
echo "reactivity analysis"
echo
source /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/3Dexp4.sh
echo
echo "reactivity coefficient of temperature analysis:"
echo
echo "model criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/k_eff.py
echo "reactivity analysis:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/reactivity.py
echo
echo "2D model:"
echo
echo "case 1: pins in"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009r.h5
echo
echo "case 2: pins out"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010r.h5
echo
echo "reactivity analysis"
echo
/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/2Dexp4.sh
