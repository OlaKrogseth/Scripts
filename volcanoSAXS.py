import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Open a fiLe dialog to select the .dAt files #made this.
root = tk.Tk()
root.withdraw()
file_paths = tk.filedialog.askopenfilenames(filetypes=[("Data files", "*.dat")])

# Loop through each selected file
for file_path in file_paths:
    # Open the file and read the data
    with open(file_path) as file:
        data = file.readlines()

    # Initialize lists to store the data
    Q = []
    I_Q = []

    # Loop through each line of the file
    for line in data:
        # Split the line by whitespace
        values = line.split()
        # Store The values in the appropriate list
        Q.append(float(values[0]))
        I_Q.append(float(values[1]))


n = 1000

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
plt.xlabel("Q")
plt.ylabel("I(Q)")
plt.xscale('log')
plt.yscale('log')
ax2 = fig.add_subplot(122,projection='3d')


y = I_Q[0:-500]
y = np.log(y)
x = lst = list(range(0,len(y)))
t = np.linspace(0, np.pi*2, n)

xn = np.outer(x, np.cos(t))
yn = np.outer(x, np.sin(t))
zn = np.zeros_like(xn)

for i in range(len(x)):
    zn[i:i+1,:] = np.full_like(zn[0,:], y[i])

ax1.plot(Q, I_Q)


# Plot the surface.
surf = ax2.plot_surface(xn, yn, zn, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.axis("off")

plt.show()
