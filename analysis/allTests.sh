#!/bin/bash
echo "3D model:"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-011/IPEN-011.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-011/IPEN-011.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-008/IPEN-008.h5
echo

echo "2D model, control rods out:"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009/IPEN-009r.h5
echo

echo "2D model, control rods in:"
echo
echo "criticality"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010.h5
echo "power distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010.h5
echo "reaction rate distribution:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/reactionRates.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010/IPEN-010r.h5
