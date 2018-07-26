import h5py

total = 0
counter = 0
for i in range(1, 7):
    if i <= 3:
        lastState = 4
    else:
        lastState = 5
    h5 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/IPEN-014t/IPEN-014-" + str(i) + ".h5", 'r')
    for j in range(1, lastState + 1):
        state = "STATE_000" + str(j)
        keff = h5[state]["keff"][()]
        #print(i, j)
        #print((keff - 1) * 10**5, "pcm")
        counter += 1
        total += abs((keff - 1) * 10**5)
print("mean absolute error:", total / counter, "pcm")
            
