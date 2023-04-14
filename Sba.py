import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it
import tkinter as tk
from tkinter import filedialog
#Skrevet av Ola Bohne Krogseth

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


print("\nFile names must be identical and end with a number: 0 to n \n")
print("Example: myfile0, myfile1 etc.")
print("Choose sample file")
sfile_name = getfile_path()

print("Choose buffer file")
bfile_name = getfile_path()
frames = 10
name = str(input("Enter new file name: "))

def reader(frames):
    print("\nFiles read: \n")
    plt.figure(figsize=(10, 10), dpi=80)
    for i in range(frames):
        s_data = []
        b_data = []
        buffer_file = bfile_name[:-1]+str(i)+".dat"
        sample_file = sfile_name[:-1]+str(i)+".dat"

        print(sample_file,"\n",buffer_file)
        with open(buffer_file, 'r') as file:
            for line in file:
                b_data.extend(map(eval, line.split()))
        with open(sample_file, 'r') as file:
            for line in file:
                s_data.extend(map(eval, line.split()))

        s_Qx = s_data[0::3]
        s_Qy = s_data[1::3]
        s_Qz = s_data[2::3]

        b_Qx = b_data[0::3]
        b_Qy = b_data[1::3]
        b_Qz = b_data[2::3]

        globals()['s_Qx%s' % i] = s_Qx
        globals()['s_Qy%s' % i] = s_Qy
        globals()['s_Qz%s' % i] = s_Qz

        globals()['b_Qx%s' % i] = b_Qx
        globals()['b_Qy%s' % i] = b_Qy
        globals()['b_Qz%s' % i] = b_Qz


        plt.plot(np.log(b_Qx),np.log(b_Qy),label = "Sample frame "+str(i))
        plt.plot(np.log(s_Qx),np.log(s_Qy),label = "Buffer frame "+str(i))

    plt.legend()
    plt.show()
    file.close()

#Writes as new file
def wr(x,y):
    with open(name+".dat", "w") as file:
        for i in range(len(x)):
            line = str(x[i])+" "+str(y[i])+" "+str(z[i])
            file.write(line)
            file.write("\n")

        file.close()

reader(frames)


#integral of median data
def trapezoidal_int():
    Uscr = 1.01
    Lscr = 0.99
    unsorted_s = []
    unsorted_b = []
    for k in range(frames):
        unsorted_s.append(sum(it.cumtrapz((eval("s_Qy"+str(k))))))
        unsorted_b.append(sum(it.cumtrapz((eval("b_Qy"+str(k))))))
    sorted_s_m=np.median(sorted(unsorted_s))
    sorted_b_m=np.median(sorted(unsorted_b))
    s_keeplist = []
    b_keeplist = []

    s_error = []
    for j in range(frames):
        s_off_score = unsorted_s[j]/sorted_s_m
        if s_off_score >= Uscr:
            s_error.append("Frame %s " %j +"was deleted from sample. High y-value.")
        elif s_off_score <= Lscr:
            s_error.append("Frame %s " %j +"was deleted from sample. Low y-value.")
        else:
            s_keeplist.append(j)
    b_error = []
    for j in range(frames):
        b_off_score = unsorted_b[j]/sorted_b_m
        if b_off_score >= Uscr:
            b_error.append("Frame %s " %j +"was deleted from sample. High y-value.")

        elif b_off_score <= Lscr:
            b_error.append("Frame %s " %j +"was deleted from buffer. Low y-value.")
        else:
            b_keeplist.append(j)

    return s_keeplist, b_keeplist, s_error, b_error

def replot():
    print()
    plt.figure(figsize=(10, 10), dpi=80)
    for i in trapezoidal_int()[0]:
        plt.plot(np.log(eval("s_Qx%s" % i)),np.log(eval("s_Qy%s" % i)),label = "Sample frame "+str(i))
    for i in trapezoidal_int()[1]:
        plt.plot(np.log(eval("b_Qx%s" % i)),np.log(eval("b_Qy%s" % i)),label = "Buffer frame "+str(i))
    for i in range(len(trapezoidal_int()[2])):
        print(trapezoidal_int()[2][i])
    for i in range(len(trapezoidal_int()[3])):
        print(trapezoidal_int()[3][i])
    plt.legend()
    plt.show()

replot()


def Averaged():
    plt.figure(figsize=(10, 10), dpi=80)
    s_all_y = []
    s_all_x = []
    b_all_y = []
    b_all_x = []
    for i in trapezoidal_int()[0]:
        s_all_y.append((eval("s_Qy%s" % i)))
        s_all_x.append((eval("s_Qx%s" % i)))
    for i in trapezoidal_int()[1]:
        b_all_x.append((eval("b_Qx%s" % i)))
        b_all_y.append((eval("b_Qy%s" % i)))

    sy = np.mean(s_all_y, axis=0)
    sx = np.mean(s_all_x, axis=0)
    by = np.mean(b_all_y, axis=0)
    bx = np.mean(b_all_x, axis=0)
    plt.plot(np.log(sx),np.log(sy),label = "Sample avg")
    plt.plot(np.log(bx),np.log(by),label = "Buffer avg")
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 10), dpi=80)
    x = sx
    y = [y1 - y2 for (y1, y2) in zip(sy, by)]
    x_l = np.array(x)/10
    y_l = np.array(y)*0.000802551
    wr(x_l,y_l)
    plt.scatter(np.log(x),np.log(y),label = "Subtracted")
    plt.legend()
    plt.show()

Averaged()
