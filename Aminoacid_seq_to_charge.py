import matplotlib.pyplot as plt
import numpy as np

seq = list(str(input("Seq: ")))
non_polar = ["G","A","V","C","P","L","I","M","W","F"]
polar = ["S","T","Y","N","Q"]
pos_charge = ["K","R","H"]
neg_charge = ["D","E"]




colseq = []
for i in range(len(seq)):
    if seq[i] in str(non_polar):
        colseq.append(1)
    elif seq[i] in str(polar):
        colseq.append(2)
    elif seq[i] in str(pos_charge):
        colseq.append(3)
    elif seq[i] in str(neg_charge):
        colseq.append(4)
    else:
        colseq.append(0)
print(colseq)
col =[]

for i in range(0, len(colseq)):
    if colseq[i]==0:
        col.append('black')
    elif colseq[i]==1:
        col.append('yellow')
    elif colseq[i]==2:
        col.append('blue')
    elif colseq[i]==3:
        col.append('green')
    elif colseq[i]==4:
        col.append('purple')
x = range(0,len(seq))
y = np.ones(len(seq))
for i in range(len(x)):

    # plotting the corresponding x with y
    # and respective color
    plt.scatter(x[i], y[i], c = col[i], s = 500,
                linewidth = 0.5)

print(" non-polar: Yellow \n Polar: Blue \n +Charge: Green \n -Charge: Purple")
plt.show()
