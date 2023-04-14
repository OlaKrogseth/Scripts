
"""
This calculator estimates various properties of surface seawater at a given
salinity and temperature, assuming that pressure is held constant at
0.1 MPa (1 atm). The code is based on MATLAB algorithms released in the
The Seawater Thermophysical Properties Library[1]

http://web.mit.edu/seawater/

!!!Values shown are done through interpolation!!!
"""

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
T = 20
conc = [0,0.1,0.5,1]
water = 0.0010016
# 0.0010016 kg*s/m (water at 20C)

# List of values Kg*s/m:
hamzasreef = [0.0010017, 0.0010131,0.0010631,0.0011359]
vk_table = [1.0091,1.0476,1.1003]
usace = []

# Calculating parts per thousand of Moles NaCl i solution for hamzasreef calc
PSU = []
for i in range(len(conc)):
    PSU.append(conc[i]*58.44)
    plt.scatter(conc[i],hamzasreef[i], color = "blue", label = hamzasreef)
print("PSU",PSU)

# Calculating through equation from HEC-RAS 2D Sediment Technical Reference Manual
for i in range(len(conc)):
    S = 58.44*conc[i]
    usace.append((1.802863*10**-3) - ((6.1086*10**-5)*T) + ((1.31419*10**-6)*T**2) - ((1.35576*10**-8)*T**3) + ((2.15123*10**-6)*S) + ((3.59406*10**-11)*S**2))
    plt.scatter(conc[i],usace[i], color = "red")

# Finding values from vladimir findings
vk = []
for i in range(len(conc)-1):
    vk.append(water*vk_table[i])
    plt.scatter(conc[i+1],vk[i], color = "green")





#Ploting
print("usace (red)", usace)
print("hamzasreef (blue)", hamzasreef)
print("vk (green)", vk)
plt.title("Dynamic viscosity of saline water")
plt.ylabel("$Kg*s/m$")
plt.show()

# interpolation
# use linear interpolation for the hamzasreef data
f_hamzasreef = interp1d(conc, hamzasreef, kind='linear')

# use linear interpolation for the usace data
f_usace = interp1d(conc, usace, kind='linear')

# use linear interpolation for the usace data
f_vk = interp1d(conc[1:], vk, kind='linear')

# create a new set of x values to interpolate at
x_new = [0.15, 0.3, 0.6]
vk_x_new = [0.15, 0.3, 0.6]
# interpolate the hamzasreef,usace and vk data at the new x values
hamzasreef_interp = f_hamzasreef(x_new)
usace_interp = f_usace(x_new)
vk_interp = f_vk(vk_x_new)

# plot the interpolated data on the same plot as the original data
plt.plot(conc, hamzasreef, color="blue")
plt.scatter(x_new, hamzasreef_interp, color="blue", marker="x", label="hamzasreef")
plt.plot(conc, usace, color="red")
plt.scatter(x_new, usace_interp, color="red", marker="x", label="usace")
plt.plot(conc[1:], vk, color="green")
plt.scatter(vk_x_new, vk_interp, color="green", marker="x", label="vk")

# Print the new data-values
print("\nInterpolated Molar-values:", vk_x_new)
print("\nhamzasreef_interp",hamzasreef_interp,"Kg*s/m\n")
print("usace_interp",usace_interp,"Kg*s/m\n")
print("vk",vk_interp,"Kg*s/m\n" )

plt.title("Interpolated")
plt.ylabel("$Kg*s/m$")

plt.show()

# extrapolate data to show 1.2 Molar
f_hamzasreef = interp1d(conc, hamzasreef, kind='linear', bounds_error=False, fill_value="extrapolate")
f_usace_extrap = interp1d(conc, usace, kind='linear', bounds_error=False, fill_value="extrapolate")
f_vk = interp1d(conc[1:], vk, kind='linear', bounds_error=False, fill_value="extrapolate")

oex = 1.2
uex = 0

oex_hamzasreef = f_hamzasreef(oex)
oex_usace_extrap = f_usace_extrap(oex)
oex_vk = f_vk(oex)

# extrapolate data to show 0 Molar
uex_hamzasreef = f_hamzasreef(uex)
uex_usace_extrap = f_usace_extrap(uex)
uex_vk = f_vk(uex)

# Print the new data-values of molar values: oex
print("\nExtrapolated Molar-values:", oex," Molar")
print("hamzasreef",oex_hamzasreef,"Kg*s/m")
print("usace",oex_usace_extrap,"Kg*s/m")
print("vk",oex_vk,"Kg*s/m" )

# Print the new data-values of molar values: uex
print("\nExtrapolated Molar-values:", uex," Molar")
print("hamzasreef",uex_hamzasreef,"Kg*s/m")
print("usace",uex_usace_extrap,"Kg*s/m")
print("vk",uex_vk,"Kg*s/m" )

# Plot the extrapolated data together with interpolated (linear) to see if it makes sense
plt.scatter(oex, oex_hamzasreef, color="blue",marker = "o", label="Hamzasreef")
plt.scatter(uex, uex_hamzasreef, color="blue", marker = "o")
plt.scatter(oex, oex_usace_extrap, color="red",marker = "o", label="usace")
plt.scatter(uex, uex_usace_extrap, color="red",marker = "o")
plt.scatter(oex, oex_vk, color="green",marker = "o", label="vk")
plt.scatter(uex, uex_vk, color="green",marker = "o")

plt.title("Extrapolated")
plt.ylabel("$Kg*s/m$")

plt.plot(conc, hamzasreef, color="blue")
plt.plot(conc, usace, color="red")
plt.plot(conc[1:], vk, color="green")

plt.show()
