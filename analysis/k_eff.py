import h5py
import numpy as np
import sys

for i in range(1, len(sys.argv)):
    try:
        f = h5py.File(sys.argv[i], 'r')
    except:
        path = sys.argv[i][:-3]
        path += "/" + sys.argv[i]
        try:
            f = h5py.File(path, 'r')
        except:
            print("invalid filename")
            exit
    else:
        keff = f['STATE_0001/keff'][()]
        print((keff - 1) * 10**5, "pcm")


