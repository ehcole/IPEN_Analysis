import h5py
import numpy as np
import sys
import pandas as pd
import math

h5 = h5py.File(sys.argv[1], 'r')
modelData4D = h5["STATE_0001/pin_powers"]
modelData = np.zeros([modelData4D.shape[0], modelData4D.shape[1]])

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def posToIndex(position):
    #map position corresponds to column 0
    if 'ab' in position:
        xIndex = 0
    #if map position was entered as lowercase letter, shift left such that a is mapped to 1
    elif ord(position[0]) >= 97:
        xIndex = ord(position[0]) - 96
    #else, letter is capital. Shifts left such that A is mapped to 1
    else:
        xIndex = ord(position[0]) - 64

    yIndex = int(position[-2:])
    return [xIndex, yIndex]
#populate 2D array of model data, axially integrate pin power
#note: simple average was used here because the planar levels of the fuel cells
#were evenly distributed
for i in range(modelData.shape[0]):
    for j in range(modelData.shape[1]):
        for k in range(modelData4D.shape[2]):
            modelData[i][j] += modelData4D[i][j][k][0] / modelData4D.shape[2]


expDataDF = pd.read_csv("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/expData/reactionRates.csv")
expData = dict()
for col in expDataDF.columns[1:]:
    sum = 0
    count = 0
    for i in expDataDF[col]:
        count += 1
        sum += i 
    expData[col] = sum
total = 0
count = 0
expData.pop("Y06")
expData.pop("Q11")
expData.pop("T15")
for key in expData:
    count += 1
    total += expData[key]

mean = total / count

predictionsList = list()
targetsList = list()
for key in expData:
    arrayIndices = posToIndex(key)
    if modelData[arrayIndices[0]][arrayIndices[1]] != 0:
        targetsList.append(expData[key] / mean)
        predictionsList.append(modelData[arrayIndices[0]][arrayIndices[1]])


predictions = np.array(predictionsList)
targets = np.array(targetsList)
#print(predictions)
#print(targets)
diffs = abs(targets - predictions)
#print(diffs)
diffPercents = diffs / targets * 100
print("MAPE:", diffPercents.mean())
print("rmse:", rmse(predictions, targets))


