import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Parameters
R = 1000
C = 1e-6

# Function whose root we are looking for: |Z| = R/√2
def equation(omega):
    Z_module = np.sqrt(R**2 + 1/(C**2 * omega**2))
    return Z_module - R / np.sqrt(2)

# Initial value (guess)
omega_guess = 500

# Resolution
omega_c = fsolve(equation, omega_guess)[0]
f_c = omega_c / (2 * np.pi)

print(f"Cutoff frequency: {f_c:.2f} Hz")
print(f"Verification: τ = RC = {R*C:.6f} s")
print(f"theoretical f_c = 1/(2πRC) = {1/(2*np.pi*R*C):.2f} Hz")