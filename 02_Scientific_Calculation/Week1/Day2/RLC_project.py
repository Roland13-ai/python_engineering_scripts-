import numpy as np
import sympy as sp  
import matplotlib.pyplot as plt
import csv

# Step 1: Input parameters
R = float(input("Resistance R (Ω): "))
L = float(input("Inductance L (H): "))
C = float(input("Capacitance C (F): "))
fmin = float(input("Minimum frequency (Hz): "))
fmax = float(input("Maximum frequency (Hz): "))
N = int(input("Number of points: "))
# Step 2: Calculations with NumPy
f = np.logspace(np.log10(fmin), np.log10(fmax), N)
omega = 2 * np.pi * f
Z_R = R
Z_L = 1j * L * omega
Z_C = 1 / (1j * C * omega)
Z = Z_R + Z_L + Z_C

module = np.abs(Z)
phase = np.angle(Z, deg=True)

# Resonance frequency (minimum modulus)
idx_min = np.argmin(module)
f_res = f[idx_min]
mod_res = module[idx_min]

print(f"\nResonance frequency: {f_res:.2f} Hz")
print(f"Modulus at resonance: {mod_res:.2f} Ω")

R_s, L_s, C_s, omega_s= sp.symbols('R_s, L_s, C_s, omega_s',  positive= True)
Z_s = R_s + (sp.I * L_s * omega_s + 1/(sp.I * C_s * omega_s))
Z_simp= sp.simplify( Z_s)
sp.pprint(Z_simp)

Mod_Zs= sp.sqrt((Z_s)**2+sp.im(Z_s)**2)
sp.pprint(Mod_Zs)

# Resolution: imaginary part = 0 → L_s*omega_s - 1/(C_s*omega_s) = 0
equation = sp.Eq(L_s * omega_s, 1/(C_s * omega_s))
solution = sp.solve(equation, omega_s)
print("\nResonance angular frequency(ies):")
sp.pprint(solution)

#Create a figure of size 10×8
plt.figure(figsize=(10,8))
#Plot the modulus as a function of frequency in the top subplot (semi-log scale)
pltsubplot(2,1,1)
plt.plot(Mod_Zs, f)
plt.xlog("f")
plt.ylog("Module")
#Plot the phase as a function of frequency in the bottom subplot (semi-log scale)
pltsubplot(2,1,2)
plt.plot(phase, f)
plt.xlog("phase")
plt.ylog("f")
#Add a vertical line at the resonance frequency on each graph
plt.plot(f_res)
#Add labels, titles and grids
plt.title("RLC graphics")
#Save the image bode_RLC.png in 03_projects/
plt.savefig("03_projects")
#Close the figure
plt.show()