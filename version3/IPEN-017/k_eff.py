import h5py

total = 0
counter = 0
for i in range(1, 7):
    lastState = 6
    h5 = h5py.File("IPEN-017-" + str(i) + ".h5", 'r')
    for j in range(1, lastState + 1):
        state = "STATE_000" + str(j)
        keff = h5[state]["keff"][()]
        print(i, j)
        print((keff - 1) * 10**5, "pcm")
        counter += 1
        total += abs((keff - 1) * 10**5)
h5 = h5py.File("IPEN-017-7.h5", 'r')
print("7, 1")
keff = h5["STATE_0001/keff"][()]
print((keff -1) * 10**5, "pcm")
counter += 1
total += abs((keff - 1) * 10**5)
print(total / counter, "pcm")
            
