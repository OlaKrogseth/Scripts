import math

# Constants
R = 8.314  # J/(mol·K)
F = 96485  # C/mol

def calculate_conductance(V, I):
    V = V / 1000  # Convert mV to V
    I = I / 1e12  # Convert pA to A

    # Calculate the conductance using Ohm's law
    conductance = I / V
    return conductance

def calculate_ps(V, I, T, KCl_concentration):
    conductance = calculate_conductance(V, I)
    conductance_ps = conductance * 1e12  # Convert to pS
    return conductance_ps

# Example usage
V = -25  # mV
I = 2   # pA
T = 25   # Celsius
KCl_concentration = 0.15  # M (not used in the corrected code, but left for consistency)

pS_value = calculate_ps(V, I, T, KCl_concentration)
print(f"pS value: {pS_value:.2f} pS")
