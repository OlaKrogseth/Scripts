import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import statistics
import tkinter.filedialog as fd
import tkinter as tk





# n files read per run
n = 5




def Avg_plotter(x,y,z,a,b):

    # Open file dialog(s) to select .dat file


    root = tk.Tk()
    paths = fd.askopenfilenames(parent=root, title='Choose a file')

    Sample = [x,y,z,a,b]
    D = []
    for i in range(n):

        # read .dat to a list of lists
        data = [i.strip().split() for i in open(paths[i]).readlines()]

        # Plotting angle, Diameter

        Diameter = []

        for i in range(len(data)-1):
            Diameter.append(float(data[i+1][7]))



        Diameter = statistics.mean(Diameter)
        D.append(Diameter)
        print(Diameter)

    for i, txt in enumerate(D):
        plt.annotate(txt, (Sample[i], D[i]))

    plt.scatter(Sample,D)
    plt.xlabel("Sample")
    plt.ylabel("Diameter (nm)")
    plt.show()
    root.destroy()
    return D

A = Avg_plotter("A1", "A2", "A3", "A4", "A5")
B = Avg_plotter("B1", "B2", "B3", "B4", "B5")
D = Avg_plotter("D1", "D2", "D3", "D4", "D5")
F = Avg_plotter("F1", "F2", "F3", "F4", "F5")


def correlation_function(x, y):
  # Calculate the means of x and y
  x_mean = np.mean(x)
  y_mean = np.mean(y)

  # Calculate the standard deviations of x and y
  x_std = np.std(x)
  y_std = np.std(y)

  # Calculate the correlation function
  correlation = np.mean((x - x_mean)*(y - y_mean)) / (x_std * y_std)

  return correlation

print("Correlation:")
print("A - B ",correlation_function(A, B))
print("A - D ",correlation_function(A, D))
print("A - F ",correlation_function(A, F))
print("D - F ",correlation_function(D, F))
