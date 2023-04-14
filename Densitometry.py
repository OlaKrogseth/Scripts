import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {"Water":0.998205, "Tris":1.000663, "150mM NaCl":1.007857,
        "300mM NaCl":1.012999,"600mM NaCl":1.025428, "1200mM NaCl":1.050070}
x = list(data.keys())
y = list(data.values())

fig = plt.figure(figsize = (10, 5))
plt.ylim(0.95, 1.075)
# creating the bar plot
plt.bar(x, y, color ='maroon',
        width = 0.4)

# Add a legend
plt.legend([y])

# Add labels to each bar with the y value
for i, v in enumerate(y):
    fig.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')

# Add x and y labels and a title
plt.xlabel("Buffer")
plt.ylabel("$g/cm^3$")
plt.title("$g/cm^3$ of different saline solutions")

# Show the plot
plt.show()
