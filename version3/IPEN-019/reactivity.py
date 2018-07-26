import h5py
import numpy as np
f0 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/IPEN-019-7.h5", 'r')
expData = np.array([154.91, 111.68, -4.14, -67.01, -249.83, -348.68, -344.79])
#expData = np.array([12.52, -21.92, -89.89, -135.23, -266.62, -344.76, -332.39])
results = np.zeros(expData.shape[0])
keff0 = f0["STATE_0001/keff"][()]
for i in range(8):
    if i == 0:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/IPEN-019.h5", 'r')
        keff1 = f["STATE_0001/keff"][()]
    else:
        try:
            f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-019/IPEN-019-" + str(i) + ".h5", 'r')
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
    if i != 7:
        results[i] = (keff1 - keff0) * 10**5 / (keff1 * keff0)
print(results)
print(expData)
diffs = results - expData
absDiffs = np.absolute(diffs)
print(absDiffs.mean())
diffsPercents = absDiffs / results
absDiffsPercents = np.absolute(diffsPercents)
print(absDiffsPercents.mean())
