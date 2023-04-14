import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *

# Create a Tkinter root window
root = Tk()

# Ask the user to select one or more files to open
files = filedialog.askopenfilenames(parent=root, title='Select files')

# Read the data from each selected file
for file in root.tk.splitlist(files):
    data = []
    with open(file, 'r') as f:
        for line in f:
            # Split the line by whitespace and convert each value to a float
            values = [float(x) for x in line.split()]
            data.append(values)

    # Extract the columns named Q, I(Q), and Error
    Q = [x[0] for x in data]
    I = [x[1] for x in data]
    error = [x[2] for x in data]

    # Plot the data as a dot plot
    plt.loglog(Q, I, '.')
    plt.xlabel("Q ($Å^-1$)")
    plt.ylabel("I(Q) ($cm^-1$)")
    #plt.errorbar(Q, I, error, fmt='none')

# Add a legend to the plot showing the labels and concentration based on the contents of the filenames
labels = []
for file in root.tk.splitlist(files):
    filename = file.rsplit('/', 1)[1]
    label = ''
    if 'Liposome' in filename:
        label += 'Liposome'
    elif 'Gramicidin' in filename:
        label += 'Gramicidin'
    elif 'Indo' in filename:
        label += 'Indolicidin'
    elif 'LL' in filename:
        label += 'LL-37'

    if '150' in filename:
        label += ' (150mM NaCl)'
    elif '300' in filename:
        label += ' (300mM NaCl)'
    elif '600' in filename:
        label += ' (600mM NaCl)'

    if '20' in filename:
        label += ' (@20C)'
    elif '_37' in filename:
        label += ' (@37C)'

    else:
        label += ' (H\u2082O)'
    labels.append(label)


plt.legend(labels, fontsize=16)

plt.show()
