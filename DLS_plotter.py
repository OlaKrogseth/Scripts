import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
import statistics
import numpy as np

def plotter():

    # Create a Tkinter root window
    root = Tk()

    # select one or more files to open
    files = filedialog.askopenfilenames(parent=root, title='Select files')
    print(files)
    all_time = []
    all_correlation_coefficient = []
    # Read the data from each selected file
    for file in root.tk.splitlist(files):
        data = []
        with open(file, 'r') as f:
            for line in f:
                if line.startswith('Lag time (s)'):
                    for line in f:
                        # Split the line by whitespace and convert each value to a float
                        if line.startswith('Count Rate History (KHz)'):
                            break
                        values = [float(x) for x in line.split()]
                        data.append(values)


        # Extract the columns named time and correlation_coefficient
        time = [x[0] for x in data[:-1]]
        all_time.append(time)
        correlation_coefficient = [x[1] for x in data[:-1]]
        all_correlation_coefficient.append(correlation_coefficient)

        """
        # Plot the data as a dot plot
        plt.loglog(time, correlation_coefficient,".")
        plt.xlabel("Lag time (s)")
        plt.ylabel("($g^-2$)")
        """
    """
    plt.loglog(all_time, all_correlation_coefficient,".")
    plt.xlabel("Lag time (s)")
    plt.ylabel("($g^-2$)")
    """

    all_time_mean = [statistics.mean(position) for position in zip(*all_time)]
    all_correlation_coefficient_mean = [statistics.mean(position) for position in zip(*all_correlation_coefficient)]

    # Plot the data as a dot plot
    plt.scatter(all_time_mean, all_correlation_coefficient_mean)
    plt.xlabel("Lag time (s), 0 -> 120 seconds")
    plt.ylabel("($g^-2$)")
    plt.xscale("log")
    plt.ylim(-0.05,1.05)




    # Add a legend to the plot showing the labels and concentration based on the contents of the filenames
    for file in root.tk.splitlist(files):
        filename = file.rsplit('/', 2)[1]
        print(filename)
        label = ''
        if 'A1' in filename:
            label += 'Liposome'
        elif 'B1' in filename:
            label += 'Gramicidin'
        elif 'D1' in filename:
            label += 'Indolicidin'
        elif 'F1' in filename:
            label += 'LL-37'

        if 'A2' in filename:
            label += 'Liposome 150mM'
        elif 'B2' in filename:
            label += 'Gramicidin 150mM'
        elif 'D2' in filename:
            label += 'Indolicidin 150mM'
        elif 'F2' in filename:
            label += 'LL-37 150mM'

        if 'A3' in filename:
            label += 'Liposome 300mM'
        elif 'B3' in filename:
            label += 'Gramicidin 300mM'
        elif 'D3' in filename:
            label += 'Indolicidin 300mM'
        elif 'F3' in filename:
            label += 'LL-37 300mM'

        if 'A4' in filename:
            label += 'Liposome 600mM'
        elif 'B4' in filename:
            label += 'Gramicidin 600mM'
        elif 'D4' in filename:
            label += 'Indolicidin 600mM'
        elif 'F4' in filename:
            label += 'LL-37 600mM'

        if '20' in filename:
            label += ' (@20C)'
        elif '37' in filename:
            label += ' (@37C)'

        else:
            label += ' (H\u2082O)'
        return label
        break
# n is the amount of files taht you want to compare
n = 4
labels = []
for i in range(n):
    labels.append(plotter())

plt.legend(labels, fontsize=16)
plt.show()
