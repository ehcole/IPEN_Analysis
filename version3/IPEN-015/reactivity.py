import h5py
import numpy as np
f0 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015-7.h5", 'r')
expData = np.array([160.41, 117.18, 1.36, -61.51, -244.33, -343.18, -339.29])
#expData = np.array([154.91, 111.68, -4.14, -138.47, -249.83, -348.68, -344.79])
results = np.zeros(expData.shape[0])
keff0 = f0["STATE_0001/keff"][()]
for i in range(8):
    if i == 0:
        f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015.h5", 'r')
        keff1 = f["STATE_0001/keff"][()]
    else:
        try:
            f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-015/IPEN-015-" + str(i) + ".h5", 'r')
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
