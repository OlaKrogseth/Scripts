#Harry-plotter

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

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
        Q = []
        IQ = []

        f1 = f.readlines()[3:]
        for line in f1:
            if not line.strip() or line.startswith('@') or line.startswith('#'):
                continue
            row = line.split()
            Q.append(float(row[0]))
            IQ.append(float(row[1]))
        f.close()
        return plt.scatter(Q,IQ, label = sample_name)

def fitfetch(fit):
    with open(fit, "r") as f:
        Q = []
        IQ = []

        for line in f:
            if not line.strip() or line.startswith('@') or line.startswith('#'):
                continue
            row = line.split()
            Q.append(float(row[0]))
            IQ.append(float(row[1]))
        f.close()
        return plt.plot(Q,IQ, "r", label = "Fit")
datafetch(data)
fitfetch(fit)
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
newname_end = "figure_"+newname_start
newfilename = str(data).replace(newname_start,newname_end)
newfilename = newfilename.replace(".dat", ".png")

plt.savefig(newfilename, dpi=300)
plt.show()
