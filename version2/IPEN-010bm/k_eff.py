import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010bm/IPEN-010-1.h5", 'r')
keff = (f["STATE_0001"]["keff"][()] - 1) * 10**5
print(keff, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010bm/IPEN-010-2.h5", 'r')
keff = (f["STATE_0001"]["keff"][()] - 1) * 10**5
print(keff, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-010bm/IPEN-010-3.h5", 'r')
keff = (f["STATE_0001"]["keff"][()] - 1) * 10**5
print(keff, "pcm")
