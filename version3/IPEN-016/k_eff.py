import h5py
import numpy as np
import sys
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016.h5", 'r')
for i in range(1, 7):
    print("State", i)
    state = "STATE_000" + str(i)
    keff = f[state]['keff'][()]
    print((keff - 1) * 10**5, "pcm")


