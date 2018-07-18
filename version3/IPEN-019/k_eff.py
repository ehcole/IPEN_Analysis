import h5py

for i in range(8):
    if i == 0:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/IPEN-019.h5", 'r')
    else:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/IPEN-019-" + str(i) + ".h5", 'r')
    keff = f["STATE_0001/keff"][()]
    numPlates = 32 - i * 5
    if numPlates < 0:
        numPlates = 0
    print(numPlates, "Plates")
    print((keff - 1) * 10**5, "pcm")

