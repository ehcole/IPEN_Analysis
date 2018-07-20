import h5py
import numpy as np
import sys
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-016/IPEN-016.h5", 'r')
for i in range(1, 7):
    state = "STATE_000" + str(i)
    try:
        keff = f[state]['keff'][()]
    except:
        exit(0)
    else:
        print("State", i)
        print((keff - 1) * 10**5, "pcm")


