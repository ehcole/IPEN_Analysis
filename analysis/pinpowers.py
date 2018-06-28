from __future__ import division
import numpy as np
import h5py


#load data
expData = np.genfromtxt("../expData/IPENpinpowers.csv", delimiter=',')
h5 = h5py.File("../IPEN-004/IPEN-004.h5", 'r')
modelData4D = h5["STATE_0001/pin_powers"]
modelData = np.empty([modelData4D.shape[0], modelData4D.shape[1]])

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

#populate 2D array of model data, axially integrate pin power
#note: simple average was used here because the planar levels of the fuel cells
#were evenly distributed
for i in range(modelData.shape[0]):
    for j in range(modelData.shape[1]):
        for k in range(modelData4D.shape[2]):
            modelData[i][j] += modelData4D[i][j][k][0] / 8.0

#normalize experimental data
numNonzeros = 0
total = 0
for i in range(expData.shape[0]):
    for j in range(expData.shape[1]):
        if expData[i][j]:
            numNonzeros += 1
            total += expData[i][j]
expDataMean = total / numNonzeros
normalizedExpData = expData / expDataMean


#diffPercents is percent error ((model datapoint - exp datapoint) / exp datapoint)
diffs = np.zeros(expData.shape)
diffPercents = np.zeros(expData.shape)
numDatapoints = 0
expDataList = list()
modelDataList = list()

for i in range(normalizedExpData.shape[0]):
    for j in range(normalizedExpData.shape[1]):
        if normalizedExpData[i][j] and modelData[i][j]:
            numDatapoints += 1
            diffs[i][j] = modelData[i][j] - normalizedExpData[i][j]
            diffPercents[i][j] = diffs[i][j] / modelData[i][j] * 100
            expDataList.append(normalizedExpData[i][j])
            modelDataList.append(modelData[i][j])


expDatapoints = np.array(expDataList)
modelDatapoints = np.array(modelDataList)
absPercents = np.absolute(diffPercents)

print("mean absolute percent error:", np.mean(absPercents[np.where(absPercents != 0)]))
print("RMSE:", rmse(expDatapoints, modelDatapoints))


