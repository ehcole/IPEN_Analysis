import h5py

f0 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015-7.h5", 'r')
keff0 = f0["STATE_0001/keff"][()]
for i in range(7):
    if i == 0:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015.h5", 'r')
        keff1 = f["STATE_0001/keff"][()]
        print("32 Plates")
        print((keff1 - keff0) * 10**5 / (keff1 * keff0), "pcm")
    else:
        try:
            f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015-" + str(i) + ".h5", 'r')
        except:
            exit(0)
        else:
            try:
                keff1 = f["STATE_0001/keff"][()]
            except:
                exit(0)
            else:
                numPlates = 32 - i * 5
                if numPlates < 0:
                    numPlates = 0
                print(numPlates, "Plates")
                print((keff1 - keff0) * 10**5 / (keff1 * keff0), "pcm")
