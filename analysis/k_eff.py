import h5py
import numpy as np
import sys
import os



#each argument must be either an h5 file or a directory containing its own k_eff.py
for i in range(1, len(sys.argv)):
    if not "h5" in sys.argv[i]: 
        os.system("python " + sys.argv[i] + "/k_eff.py")
    else:
        f = h5py.File(sys.argv[i], 'r')
        index = 1
        while 1:
            if index < 10:
                state = "STATE_000" + str(index)
            else:
                state = "STATE_00" + str(index)
            index += 1
            try:
                keff = f[state]["keff"][()]
                print((keff - 1) * 10**5, "pcm")
            except:
                sys.exit(0)
            

