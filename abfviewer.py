import matplotlib.pyplot as plt
import pyabf
import tkinter as tk
from tkinter import filedialog
import numpy as np

def getfile_paths():  # get files from directory
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(parent=root, title='Select files')
    valid_file_paths = [file for file in file_paths if file.endswith('.abf')]
    if not valid_file_paths:
        print("No .abf files were selected.")
    return valid_file_paths

def rolling_average(data, window_size):
    window = np.ones(window_size) / window_size
    return np.convolve(data, window, mode='same')

file_paths = getfile_paths()

colors = ['black', 'black', 'green', 'red', 'purple', 'brown', 'orange', 'cyan', 'magenta', 'gray']
file_counter = 0

scale = 0.7
window_size = 100  # Adjust this value according to the desired window size

#Mean of signal
def mean_chunks(data, chunk_size):
    num_chunks = len(data) // chunk_size
    chunk_means = [np.mean(data[i*chunk_size:(i+1)*chunk_size]) for i in range(num_chunks)]
    return chunk_means

chunk_size = 8000000

for file_path in file_paths:
    abf = pyabf.ABF(file_path)
    abf.setSweep(0)

    y_scaled = abf.sweepY + scale
    y_rolling_avg = rolling_average(y_scaled, window_size)

    # Calculate the mean of every 10,000 points
    mean_signal_chunks = mean_chunks(y_scaled, chunk_size)

    # Compute x values for the mean signal chunks
    x_mean_signal_chunks = np.linspace(abf.sweepX[0], abf.sweepX[-1], len(mean_signal_chunks))

    plt.plot(abf.sweepX, y_scaled, color=colors[file_counter % len(colors)], label=file_path, alpha=0.3)
    plt.plot(abf.sweepX, y_rolling_avg, color=colors[file_counter % len(colors)], label=f"Rolling Avg {file_path}")

    # Plot the mean signal chunks as a red line
    #plt.plot(x_mean_signal_chunks, mean_signal_chunks, color="r", linestyle='--', label="Mean of every 10,000 points")
    file_counter += 1


# manual mean Plot the new x-axis
x = range(1701)
y = [0] * len(x)
plt.plot(x, y, color="r", linestyle='--')


plt.ylabel("pA")
plt.xlabel("t[s]")
#plt.legend()
plt.show()
