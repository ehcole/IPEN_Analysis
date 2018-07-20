import h5py

total = 0
for i in range(8):
    if i == 0:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015.h5", 'r')
        keff = f["STATE_0001/keff"][()]
        print("32 Plates")
        print((keff - 1) * 10**5, "pcm")
        total += abs((keff - 1) * 10**5)
    else:
        try:
            f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015-" + str(i) + ".h5", 'r')
        except:
            exit(0)
        else:
            try:
                keff = f["STATE_0001/keff"][()]
            except:
                exit(0)
            else:
                numPlates = 32 - i * 5
                if numPlates < 0:
                    numPlates = 0
                print(numPlates, "Plates")
                print((keff - 1) * 10**5, "pcm")
                total += abs((keff - 1) * 10**5)
                if i == 7:
                    print("Mean absolute error", total / 8)
