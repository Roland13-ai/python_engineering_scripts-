KIRCHHOFF
import numpy as np

# Circuit: E = 10 V, R1 = 100 Ω, R2 = 200 Ω
# Equations:
#  I1*R1 + (I1 - I2)*R2 = E
#  (I2 - I1)*R2 + I2*R1 = 0   (mesh 2 with a load R1)

# In matrix form: A * I = B
A = np.array([[300, -200],
              [-200, 300]])
B = np.array([10, 0])

# Resolution
currents = np.linalg.solve(A, B)
print("Currents:", currents)

# Verification
print("A * I =", A @ currents)