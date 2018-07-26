import h5py
import numpy as np

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/IPEN-013.h5", 'r')
oldKeff = f["STATE_0001/keff"][()]
results = np.zeros(13)
expData = np.array([-0.5692367257, -0.4353073932, -0.6530200078, -0.5022676959, -0.5022878327, -0.5859966029, -0.5859966029])
for i in range(2, 15):
    if i < 10:
        state = "STATE_000" + str(i)
    else:
        state = "STATE_00" + str(i)
    keff = f[state]["keff"][()]
    alpha = (oldKeff - keff) / (oldKeff * keff * 5)
    oldKeff = keff
    results[i - 2] = alpha
print("MPACT output:", results.mean() * 10**5)
print("Experimental result:", expData.mean())
print("Percent error:", (results.mean() * 10**5 - expData.mean()) / (results.mean() * 10**5) * 100)
keff20 = f["STATE_0003/keff"][()]
keff80 = f["STATE_0014/keff"][()]
