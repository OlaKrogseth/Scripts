import matplotlib.pyplot as plt
from tkinter import filedialog, simpledialog
from tkinter import *

# Create a Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

# Ask the user to select one or more files to open
files = filedialog.askopenfilenames(parent=root, title='Select files')

labels = []

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
    # error = [x[2] for x in data]

    # Plot the data as a dot plot
    plt.loglog(Q, I, '.')
    plt.xlabel("Q ($Å^-1$)", fontsize=16)
    plt.ylabel("I(Q) ($cm^-1$)", fontsize=16)
    # plt.errorbar(Q, I, error, fmt='none')

    # Ask the user to input a label for the current dataset
    label = simpledialog.askstring("Label input", "Enter a label for the current dataset:", parent=root)
    labels.append(label)

plt.legend(labels, fontsize=16)

#plt.gca().set_xlim([0.0058, 0.38])
#plt.gca().set_ylim([1.68e-5, 1.05])

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
