import h5py
import numpy as np
import sys
f = h5py.File(sys.argv[1], 'r')
#print(list(f.keys()))
keff = f['STATE_0001/keff'][()]
if keff > 1:
    print((keff - 1) * 10**5, "pcm supercritical")
else:
    print((keff - 1) * 10**5, "pcm subcritical")

