import h5py
import numpy as np

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version3/IPEN-013/IPEN-013.h5", 'r')
results = np.zeros(23)
keff = f['STATE_0001/keff'][()]
print((keff - 0.99791) * 10**5, "pcm")
results[0] = (keff - 0.99791) * 10**5
keff = f['STATE_0002/keff'][()]
print((keff - 0.99760) * 10**5, "pcm")
results[1] = (keff - 0.99760) * 10**5
for i in range(3, 24):
    if i < 10:
        state = "STATE_000" + str(i)
    else:
        state = "STATE_00" + str(i)
    keff = f[state]['keff'][()]
    print((keff - 1) * 10**5, "pcm")
    results[i - 1] = (keff - 1) * 10**5
print(results.mean())
