import h5py

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-018/IPEN-018.h5", 'r')
keff0 = f["STATE_0001/keff"][()]
keff1 = f["STATE_0003/keff"][()]

rho = (keff1 - keff0) * 10**5 / (keff1 * keff0)
print(abs(rho - 2354.4) / rho)
