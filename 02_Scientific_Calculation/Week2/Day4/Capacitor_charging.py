import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
R = 1000        # 1 kΩ
C = 1e-6        # 1 µF
V_in = 5        # 5 V
tau = R * C     # Time constant

# Differential equation: dVc/dt = (Vin - Vc) / (R*C)
def circuit_rc(t, Vc):
    return (V_in - Vc) / tau

# Resolution from 0 to 5*tau (5 ms)
t_span = (0, 5 * tau)
Vc0 = [0]  # Initial voltage = 0 V
t_eval = np.linspace(0, 5*tau, 1000)

solution = solve_ivp(circuit_rc, t_span, Vc0, t_eval=t_eval)

# Plot
plt.plot(solution.t * 1000, solution.y[0], 'b', linewidth=2)
plt.axhline(y=V_in, color='r', linestyle='--', label=f'Vin = {V_in} V')
plt.axvline(x=tau*1000, color='g', linestyle='--', label=f'τ = {tau*1000:.2f} ms')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage Vc (V)')
plt.title('Capacitor charging (RC series)')
plt.legend()
plt.grid(True)
plt.savefig('02_scientific_calculation/week2/day4/capacitor_charging.png')
