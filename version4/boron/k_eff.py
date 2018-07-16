import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/boron/IPEN-019/IPEN-019.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/boron/IPEN-020/IPEN-020.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")
