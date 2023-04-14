import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def saline_viscosity(x,a,b,c):
    mu=a*(x**2)+b*x+c
    return mu


visc_water_20=1.0016 #mPa s #Viscosity of water at correct temp here
visc_water_35=0.7191
visc_water_40=0.6527

relative_visc20=[1,1.0091, 1.0457, 1.1003, 1.2225, 1.3691] #Table values here
relative_visc35=[1,1.0098, 1.0504, 1.1050, 1.2296, 1.3774] #Table values here
relative_visc40=[1,1.0100, 1.0513, 1.1066, 1.2320, 1.3801] #Table values here
dynamic_visc20=visc_water_20*np.array(relative_visc20)
dynamic_visc35=visc_water_35*np.array(relative_visc35)
dynamic_visc40=visc_water_40*np.array(relative_visc40)
#print(dynamic_visc)

conc20=[0,0.1,0.5,1,2,3] #Table values 20
conc35=[0,0.1,0.5,1,2,3] #Table values 35
conc40=[0,0.1,0.5,1,2,3] #Table values 40

experimental_concentrations=np.array([0,0.15,0.3,0.6])

def plotter(conc,dynamic_visc,relative_visc,label,color):
    plt.scatter(conc,dynamic_visc,color = color)
    popt,pcov=curve_fit(saline_viscosity,conc,dynamic_visc)
    #print(pcov)
    x_fit=np.linspace(0,4,1000)
    a=popt[0]
    b=popt[1]
    c=popt[2]

    y_fit=saline_viscosity(x_fit,a,b,c)
    plt.plot(x_fit,y_fit, label = label, color = color)
    calc_visc=saline_viscosity(experimental_concentrations,a,b,c)

    #plt.vlines(0.3,1,1.3)
    plt.grid(True)


    return calc_visc

print("concentrations: ", experimental_concentrations)
print("20C: ", plotter(conc20,dynamic_visc20,relative_visc20,"20$^\circ$C","black"))
print("35C: ", plotter(conc35,dynamic_visc35,relative_visc35,"35$^\circ$C","red"))
print("40C: ", plotter(conc40,dynamic_visc40,relative_visc40,"40$^\circ$C","blue"))


x = [0.71938082, 0.7296517,  0.74026742, 0.76253332]
y = [0.65296938, 0.66247009, 0.67227417, 0.69279242]


def plot37(x,y):
    _37 = []
    for i in range(len(x)):
        _37.append(0.6*x[i] + 0.4*y[i])

    print(_37)
    conc40=[0,0.15,0.6,1]
    plt.scatter(experimental_concentrations,_37,color = "purple")
    plt.plot(experimental_concentrations,_37, label = "37$^\circ$C", color = "purple")


plot37(x,y)
plt.xlabel("Concentration (mM NaCl)")
plt.ylabel("Dynamic viscosity (Pa s)")
plt.legend()
plt.show()
