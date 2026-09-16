import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

# ============================================
# PART 1 - NumPy/SciPy: time response
# ============================================
R, C, Vin = 1000, 1e-6, 5
tau = R * C

def rc_ode(t, Vc):
    return (Vin - Vc) / tau

sol = solve_ivp(rc_ode, (0, 5*tau), [0], t_eval=np.linspace(0, 5*tau, 500))

# ============================================
# PART 2 - SymPy: transfer function
# ============================================
s = sp.symbols('s')
R_s, C_s = sp.symbols('R_s C_s', positive=True)
H_s = 1/(R_s*C_s*s + 1)
H_num = sp.lambdify(s, H_s.subs({R_s:R, C_s:C}), 'numpy')

# ============================================
# PART 3 - Comparative plot
# ============================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Time response
ax1.plot(sol.t*1000, sol.y[0], 'b', linewidth=2)
ax1.axhline(Vin, color='r', linestyle='--', alpha=0.5)
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Vc (V)')
ax1.set_title('Capacitor charging (SciPy)')
ax1.grid(True)

# Frequency response
f = np.logspace(0, 5, 500)
omega = 2*np.pi*f
H_vals = np.abs(H_num(1j*omega))
ax2.semilogx(f, 20*np.log10(H_vals), 'r', linewidth=2)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Gain (dB)')
ax2.set_title('Bode diagram (SymPy + NumPy)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('02_scientific_calculation/Week2/Day6/Summary_RC.png')
plt.close()
print("Synthesis complete. Graph saved.")