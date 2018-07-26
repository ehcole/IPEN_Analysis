import h5py

total = 0
counter = 0
for i in range(1, 7):
    if i <= 3:
        lastState = 4
    else:
        lastState = 5
    try:
        h5 = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/exp4-1/IPEN-014p/IPEN-014-" + str(i) + ".h5", 'r')
    except:
        exit(0)
    else:
        for j in range(1, lastState + 1):
            state = "STATE_000" + str(j)
            try:
                keff = h5[state]["keff"][()]
            except:
                exit(0)
            else:
                #print(i, j)
                bank_pos = h5[state]["bank_pos"]
                print(bank_pos[0])
                print(bank_pos[1])
                print(keff)
                #print((keff - 1) * 10**5, "pcm")
                counter += 1
                total += abs((keff - 1) * 10**5)
#print("mean absolute error:", total / counter, "pcm")
            
