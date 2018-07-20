import h5py
import numpy as np

total = 0
counter = 0
expData = np.array([94.93, 108.34, 94.24, 113.89, 102.78, 97.83, 101.82, 95.10, 93.76, 95.55, 96.54, 97.26, 96.85, 90.13, 98.93, 93.43, 99.63, 84.76, 79.50, 85.50, 96.39, 91.90, 95.52, 90.79, 85.44, 64.30, 608.86])
rho = np.zeros(expData.shape[0])
for i in range(1, 7):
    if i <= 3:
        lastState = 4
    else:
        lastState = 5
    h5 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/IPEN-014/IPEN-014-" + str(i) + ".h5", 'r')
    h5p = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/IPEN-014p/IPEN-014-" + str(i) + ".h5", 'r')
    for j in range(1, lastState + 1):
        state = "STATE_000" + str(j)
        keff = h5[state]["keff"][()]
        keffp = h5p[state]["keff"][()]
        rho[counter] = (keffp - keff) * 10**5 / (keffp * keff)
        counter += 1
diffs = rho - expData
absDiffs = np.absolute(diffs)
diffsPercents = absDiffs / rho
expDataNoOutlier = np.zeros(expData.shape[0] - 1)
diffsPercentsNoOutlier = np.zeros(expData.shape[0] - 1)
counter = 0
total = 0
for i in range(expData.shape[0]):
    if diffsPercents[i] < 1 and diffsPercents[i] > 0:
        counter += 1
        total += diffsPercents[i]
    if i < 24:
        expDataNoOutlier[i] = expData[i]
        diffsPercentsNoOutlier[i] = diffsPercents[i]
    elif i > 24:
        expDataNoOutlier[i - 1] = expData[i]
        diffsPercentsNoOutlier[i - 1] = diffsPercents[i]
print(diffsPercentsNoOutlier.mean())
print(total / counter)
            
