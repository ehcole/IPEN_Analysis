import h5py
import numpy as np
import sys
p = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016p.h5", 'r')
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016.h5", 'r')
expData = np.array([2438.05, 2311.40, 2195.85, 1975.38, 1449.33, 222.16])
results = np.zeros(expData.shape)
boronConc = np.array([0.082, 6.067, 11.028, 21.98, 43.23, 95.742])
delta = np.zeros(len(boronConc) - 1)
for i in range(1, 7):
    state = "STATE_000" + str(i)
    keff = f[state]['keff'][()]
    keffp = p[state]['keff'][()]
    results[i - 1] = abs(keffp - keff) / (keffp * keff) * 10**5
diffs = results - expData
absDiffs = np.absolute(diffs)
diffPercents = absDiffs / results * 100
print("Individual case MAPE:", diffPercents.mean())


for i in range(1, len(boronConc)):
    delta[i - 1] = (results[i] - results[i - 1]) / (boronConc[i] - boronConc[i - 1])
print("Boron reactivity coefficient percent error:", abs((delta.mean() + 23.25) / delta.mean() * 100))

