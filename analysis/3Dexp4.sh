#!/bin/bash

echo "control rod calibration experiment"
echo "criticality"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/k_eff.py
echo "reactivity"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/reactivity.py
echo
echo "boron experiment"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/k_eff.py
echo "reactivity:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/reactivity.py
echo
echo "stainless steel reflector experiment"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/k_eff.py
echo "reactivity (difference from zero plate case):"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/reactivity.py
echo
echo "carbon steel reflector experiment"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/k_eff.py
echo "reactivity (difference from zero plate case):"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/reactivity.py
echo
echo "heavy water reflector box experiment"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-017/IPEN-017.h5
echo "reactivity:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-017/reactivity.py
echo
echo "light water reflector box experiment"
echo
echo "criticality:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-018/IPEN-018.h5
echo "reactivity:"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-018/reactivity.py

