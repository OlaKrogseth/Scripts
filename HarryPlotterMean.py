#Harry-plotter

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

print("Select peptide first")
title = str(input("Plot name: "))
sample_name = str(input("Sample name: "))
# Opens up fileprompt to select files (sample and buffer)
def getfile_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if ".dat" in file_path:
        print(file_path[:-4])
        return file_path[:-4]
    else:
        print("File selected is not a .dat file.")


data = str(getfile_path()+".dat")
print(data)
fit = str(getfile_path()+".dat")
print(fit)

def datafetch(data):
    with open(data, "r") as f:
        Q1 = []
        IQ1 = []

        f1 = f.readlines()[3:]
        for line in f1:
            if not line.strip() or line.startswith('@') or line.startswith('#'):
                continue
            row = line.split()
            Q1.append(float(row[0]))
            IQ1.append(float(row[1]))
        f.close()
        return Q1,IQ1

def fitfetch(fit):
    with open(fit, "r") as f:
        Q2 = []
        IQ2 = []

        for line in f:
            if not line.strip() or line.startswith('@') or line.startswith('#'):
                continue
            row = line.split()
            Q2.append(float(row[0]))
            IQ2.append(float(row[1]))
        f.close()
        return Q2,IQ2



#Plotting

Q1,IQ1 = datafetch(data)
Q2,IQ2 = fitfetch(fit)

Q = []
IQ = []
for i in range(len(Q1)):
    Q.append((Q1[i]+Q2[i])/2)
    IQ.append((IQ1[i]+IQ2[i])/2)

plt.plot(Q,IQ)
plt.title(str(title))
plt.xlabel("$Q[Å^{-1}]$")
plt.ylabel("$I(Q) [cm^{-1}]$")
plt.xscale("log")
plt.yscale("log")
plt.legend()


newname = str(data) #Creating new file name and directory path
last_position = newname.rfind("/")
newname = newname[newname.rfind("/"):]
newname_start = newname.replace("/", "")
newname_end = "Peptide_liposome_estimation"+newname_start
newfilename = str(data).replace(newname_start,newname_end)
newfilename = newfilename.replace(".dat", ".png")

plt.savefig(newfilename, dpi=300)
plt.show()
