import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/lwrb/IPEN-025/IPEN-025.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/lwrb/IPEN-026/IPEN-026.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")
