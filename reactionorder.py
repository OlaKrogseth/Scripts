import matplotlib.pyplot as plt
import numpy as np
t = [0, 0.5, 1, 1.5]
C = [3.1, 1.3, 0.83, 0.61]
P = []
Xn = []

#1/(1-p) = Xn = 1+M*k*t Second order reaction
for i in range(len(t)):
    P.append((C[0]-C[i])/C[0]) # (startC - C) / (startC)
    Xn.append(1/(1-P[i]))

slope  = np.polyfit(Xn, t, 1)
print(slope)

#k = slope/c0t
#k = Xn-1/C0*t
#if t = 1.25

plt.plot(t,Xn)
plt.xlabel("time")
plt.ylabel("Xn")
plt.show()
plt.plot(t,P)
plt.xlabel("time")
plt.ylabel("P")
plt.show()
