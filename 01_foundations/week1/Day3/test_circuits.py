from circuits import (impedance_resistance, impedance_capacitor, impedance_inductor, impedance_series, impedance_parallel)
import numpy as np
r = 1000
c = 1e-6
f = 50
z_r = impedance_resistance(r)
z_c = impedance_capacitor(c, f)
z_rc = impedance_series(z_r, z_c)

print(f"R= {z_r:.2f} ohm")
print(f"Zc at {f} Hz = {z_c :.2f} ohm")
print(f" series equivalent = {z_rc :.2f} ohm")
print(f"Modulus= {abs(z_rc):.2f} ohm")
print(f"Phase = {np.angle(z_rc, deg=True):.2f}°")