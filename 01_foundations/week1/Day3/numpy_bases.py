import numpy as np

# 1. Create an array of voltages (10 values from 0 to 5 V)
voltages = np.linspace(0, 5, 10)
print("Voltages (V) :", voltages)

# 2. Ohm's law: I = U / R
R = 1000  # ohms
currents = voltages / R
print("Currents (A) :", currents)

# 3. Power: P = U * I
powers = voltages * currents5
print("Powers (W) :", powers)

# 4. Extract values > 2.5 V
high_voltages = voltages[voltages > 2.5]
print("Voltages > 2.5 V :", high_voltages)