import h5py
import numpy as np

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp5/IPEN-013-section4idata/IPEN-013.h5", 'r')

print("20 degrees celsius:")
keff = f['STATE_0001/keff'][()]
print((keff - 0.99791) * 10**5, "pcm")

print("80 degrees celsius:")
keff = f['STATE_0002/keff'][()]
print((keff - 0.99760) * 10**5, "pcm")



