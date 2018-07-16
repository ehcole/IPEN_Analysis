import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/ss/IPEN-021/IPEN-021.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/ss/IPEN-022/IPEN-022.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")
