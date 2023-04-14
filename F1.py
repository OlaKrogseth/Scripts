import matplotlib.pyplot as plt
import numpy as np

r1 = 0.9
r2 = 0.2


f1 = np.arange(0, 1, 0.01).tolist()

for i in range(len(f1)):
    f2 = 1-f1[i]
    F = ( r1*f1[i]**2+f1[i]*f2 ) / (r1*f1[i]**2 + 2*f1[i]*f2 + r2*f2**2)

    print("F1: ",F)
    #print("F2", (1-F))
    print(f1[i])
    print()
