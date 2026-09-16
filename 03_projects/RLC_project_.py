"""
Project: Complete analysis of a series RLC circuit
Author : Roland13-ai
Date   : 2026
Objective: Use NumPy, SymPy, Matplotlib and CSV to study
           a series RLC circuit from the parameters entered by the user.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import csv

# ============================================================
# STEP 1 – Input parameters
# ============================================================
print("=== ANALYSIS OF A SERIES RLC CIRCUIT ===\n")
R = float(input("Resistance R (Ω)     : "))
L = float(input("Inductance L (H)      : "))
C = float(input("Capacitance C (F)        : "))
fmin = float(input("Minimum frequency (Hz) : "))
fmax = float(input("Maximum frequency (Hz) : "))
N = int(input("Number of points       : "))

# ============================================================
# STEP 2 – Numerical calculations with NumPy
# ============================================================
# Frequency vector on a logarithmic scale
f = np.logspace(np.log10(fmin), np.log10(fmax), N)
omega = 2 * np.pi * f

# Elementary impedances
Z_R = R                          # resistance (real)
Z_L = 1j * L * omega             # inductance (positive imaginary)
Z_C = 1 / (1j * C * omega)       # capacitor (negative imaginary)
Z = Z_R + Z_L + Z_C              # total impedance (complex)

# Modulus and phase
module = np.abs(Z)                # modulus in Ω
phase = np.angle(Z, deg=True)     # phase in degrees

# Resonance frequency (minimum modulus)
idx_min = np.argmin(module)       # index of the minimum
f_res = f[idx_min]                # resonance frequency (Hz)
mod_res = module[idx_min]         # modulus at resonance (Ω)

print("\n--- NUMERICAL RESULTS ---")
print(f"Resonance frequency : {f_res:.2f} Hz")
print(f"Modulus at resonance : {mod_res:.2f} Ω")

# ============================================================
# STEP 3 – Symbolic calculation with SymPy

R_s, L_s, C_s, omega_s = sp.symbols('R_s L_s C_s omega_s', positive=True)

# Symbolic impedance
Z_s = R_s + sp.I * L_s * omega_s + 1 / (sp.I * C_s * omega_s)
module_s = sp.sqrt(sp.re(Z_s)**2 + sp.im(Z_s)**2)

# Derivative of the modulus with respect to omega
derivative = sp.diff(module_s, omega_s)
freq_res_s = sp.solve(sp.Eq(derivative, 0), omega_s)

print("\n--- SYMBOLIC RESULTS ---")
print("Total impedance :")
sp.pprint(Z_s)
print("Resonance frequency(ies) (ω₀) :")
sp.pprint(freq_res_s)

# Verification with the classical formula
f0_classical = 1 / (2 * np.pi * np.sqrt(L * C))
print(f"Classical F₀ = {f0_classical:.2f} Hz")

# ============================================================
# STEP 4 – Plotting the Bode diagram (Matplotlib)
# ============================================================
plt.figure(figsize=(10, 8))

# Modulus
plt.subplot(2, 1, 1)
plt.semilogx(f, module, 'b', linewidth=2)
plt.axvline(f_res, color='r', linestyle='--', label=f'Resonance ({f_res:.2f} Hz)')
plt.ylabel('Modulus (Ω)')
plt.title('Bode diagram – Series RLC circuit')
plt.legend()
plt.grid(True)

# Phase
plt.subplot(2, 1, 2)
plt.semilogx(f, phase, 'r', linewidth=2)
plt.axvline(f_res, color='b', linestyle='--', label=f'Resonance ({f_res:.2f} Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (°)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('03_projects/bode_RLC.png')
plt.close()
print("\nGraph saved: 03_projects/bode_RLC.png")

# ============================================================
# STEP 5 – Data export (CSV)
# ============================================================
with open('03_projects/rlc_analyse.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Frequency (Hz)', 'Modulus (Ohm)', 'Phase (deg)'])
    for i in range(N):
        writer.writerow([f"{f[i]:.2f}", f"{module[i]:.2f}", f"{phase[i]:.2f}"])

print("Data exported: 03_projects/rlc_analyse.csv")
print("\n=== ANALYSIS COMPLETE ===")