import h5py
import numpy as np
import sys
import os



#each argument must be either an h5 file or a directory containing its own k_eff.py
error = 0
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/IPEN-013.h5")
for i in range(1, 16):
    if i < 10:
        state = "STATE_000" + str(i)
    else:
        state = "STATE_00" + str(i)
    temp = f[state]["tinlet"][()]
    keff = f[state]["keff"][()]
    error += abs(keff - 1) * 10**5
    print(temp, "C:", (keff - 1) * 10**5, "pcm")
print("Mean error:", error / 15, "pcm")

