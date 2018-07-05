import h5py
import numpy as np
import sys
f = h5py.File(sys.argv[1], 'r')
keff = f['STATE_0001/keff'][()]
print((keff - 1) * 10**5, "pcm")


