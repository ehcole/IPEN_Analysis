import h5py
import numpy as np

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-017/IPEN-017.h5", 'r')
total = 0
for  i in range(1, 30):
    if i < 10:
        state = "STATE_000" + str(i)
    else:
        state = "STATE_00" + str(i)
    keff = (f[state]["keff"][()] - 1) * 10**5
    print(keff)
    total += keff
print("Mean Error:", total / 29, "pcm")
