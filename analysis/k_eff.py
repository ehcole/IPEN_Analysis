import h5py
import numpy as np
f = h5py.File("../IPEN-004/IPEN-004.h5", 'r')
#print(list(f.keys()))
print(f['STATE_0001/keff'][()])
