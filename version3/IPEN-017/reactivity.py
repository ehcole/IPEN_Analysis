import h5py
import numpy as np

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-017/IPEN-017.h5", 'r')
p = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-017/IPEN-017-p.h5", 'r')
expData = np.array([97.25, 95.45, 97.01, 90.31, 94.86, 90.70, 98.61, 95.63, 93.45, 96.13, 96.01, 96.07, 94.03, 93.70, 95.91, 98.78, 101.23, 101.70, 94.23, 104.45, 109.00, 96.55, 107.34, 102.11, 103.05, 122.46, 114.64, 107.66, 99.01])
results = np.zeros(expData.shape[0])
for  i in range(1, 30):
    if i < 10:
        state = "STATE_000" + str(i)
    else:
        state = "STATE_00" + str(i)
    keff0 = f[state]["keff"][()]
    keff1 = p[state]["keff"][()]
    rho = (keff1 - keff0) * 10**5 / (keff1 * keff0)
    results[i - 1] = rho
#print(results)
resultsNoOutliers = results[:-1]
expDataNoOutliers = expData[:-1]
#print(resultsNoOutliers.mean())
diffs = resultsNoOutliers - expDataNoOutliers
#print(diffs)
absDiffs = np.absolute(diffs)
#print(absDiffs.mean())
diffsPercents = absDiffs / expDataNoOutliers
#print(results)
#print(expData)
print("MAPE:", diffsPercents.mean())
print(absDiffs.mean(), "pcm")
#print(expDataNoOutliers)
#print(diffsPercents)
