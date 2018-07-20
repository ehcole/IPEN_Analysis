import h5py

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/IPEN-013.h5", 'r')
keff20 = (f["STATE_0001/keff"][()] - 1) * 10**5
keff80 = (f["STATE_0002/keff"][()] - 1) * 10**5
alpha = (keff20 - keff80) / (keff20 * keff80 * 60)
print(alpha)
