import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it
import  tkinter as tk
from tkinter import filedialog

def getfile_path(): #get file from directory
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if ".dat" in file_path:
        print(file_path[:-4])
        return file_path[:-4]
    else:
        print("File selected is not a .dat file.")

filepath = getfile_path() + ".dat" #adding ".dat" to the path-name

with open(filepath, 'r') as datFile: #Reading file from path
    datalines = [data.split() for data in datFile] #splitting all data to nested lists
    x1 = [x[0] for x in datalines[4:1000]] #Sorting data to corrosponding x,y,z lists
    y1 = [y[1] for y in datalines[4:1000]]
    z1 = [z[2] for z in datalines[4:1000]]
    datFile.close()

newname = str(filepath) #Creating new file name and directory path
last_position = newname.rfind("/")
newname = newname[newname.rfind("/"):]
newname_start = newname.replace("/", "")
newname_end = "s_"+newname_start
newfilename = str(filepath).replace(newname_start,newname_end) #Adding a s_ to path (s_ = scaled)


with open(newfilename, "w") as newfile: #Writing in new file and scaling x and y axis.
    for i in range(len(x1)):
        line = str(eval(x1[i])*0.1)+" "+str(eval(y1[i])*0.000802551)+" "+str(eval(z1[i])*0.000802551)
        newfile.write(line)
        newfile.write("\n")

    newfile.close()
