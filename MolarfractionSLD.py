
M_NaCl = 58.44 # Molecular weight NaCl
M_H2O = 18.015 # Molecular weight H2O

moles_NaCl = [0,0.00015,0.0003,0.000600, 0.001200]
# water volume ml
v_water = 50
# density [tris, 150mM, 300mM, 600mM, 1200 mM]
density20 = [1.000663, 1.007857, 1.012999, 1.025428, 1.050070]
density37 = [0.998783, 1.000255, 1.005710, 1.017472, 1.043208]

# Include additional variables
el_r = 2.82E-13 #cm
ZH2O = 10
ZNaCl = 28
Na = 6.0221408E+23

# bi for electrons
bw = ZH2O*el_r
bNaCl = ZNaCl*el_r
print("tris, 150mM, 300mM, 600mM, 1200 mM")
def sld(density):

    for i in range(len(moles_NaCl)):
        test = (Na * el_r *( (density[i] - (M_NaCl*moles_NaCl[i]))* (ZH2O/M_H2O)+ ZNaCl*moles_NaCl[i]))
        print("\nSLD: ", f"{test: .4e}")
    print("Done\n")

print("\n20C")
sld(density20)
print("\n37C")
sld(density37)
