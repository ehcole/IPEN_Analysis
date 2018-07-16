import h5py
import numpy as np
import sys
p = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016p.h5", 'r')
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016.h5", 'r')
expData = np.array([2359.49, 2212.83, 2100.67, 1851.91, 1484.37, 218.966])
results = np.zeros(expData.shape)
for i in range(1, 7):
    state = "STATE_000" + str(i)
    keff = f[state]['keff'][()]
    keffp = p[state]['keff'][()]
    results[i - 1] = abs(keffp - keff) / (keffp * keff) * 10**5
diffs = results - expData
absDiffs = np.absolute(diffs)
diffPercents = absDiffs / results * 100
print("MAPE:", diffPercents.mean())

