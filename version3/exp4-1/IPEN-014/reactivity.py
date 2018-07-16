import h5py
import numpy as np
total = 0
counter = 0
expData = np.array([94.93, 108.34, 94.24, 113.89, 102.78, 97.83, 101.82, 95.10, 93.76, 95.55, 96.54, 97.26, 96.85, 90.13, 98.93, 93.43, 99.63, 84.76, 79.50, 85.50, 86.39, 91.90, 95.52, 90.79, 85.44, 64.30, 608.87])
results = np.zeros(expData.shape)
for i in range(1, 7):
    if i <= 3:
        lastState = 4
    else:
        lastState = 5
    h5 = h5py.File("IPEN-014-" + str(i) + ".h5", 'r')
    h5p = h5py.File("../IPEN-014p/IPEN-014-" + str(i) + ".h5", 'r')
    for j in range(1, lastState + 1):
        state = "STATE_000" + str(j)
        keff = h5[state]["keff"][()]
        keffp = h5p[state]["keff"][()]
        #print(i, j)
        #print((keffp - keff) / (keffp * keff) * 10**5, "pcm")        
        results[counter] = abs((keffp - keff)) / (keffp * keff) * 10**5
        counter += 1
diffs = results - expData
absDiffs = np.absolute(diffs)
diffsPercents = absDiffs / results
#rint(diffsPercents)
#print(diffsPercents.mean())            
diffsPercentsNoOutlier = diffsPercents[:-1]
print(diffsPercentsNoOutlier.mean())
