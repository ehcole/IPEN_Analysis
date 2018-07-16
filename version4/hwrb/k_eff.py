import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/hwrb/IPEN-023/IPEN-023.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/hwrb/IPEN-024/IPEN-024.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")
