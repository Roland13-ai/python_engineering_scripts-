import numpy as np

# Array of 10 different voltages
Vin = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
R1 = 100
R2 = 200

# Vector calculation: all at once
Req = R1 + R2
I = Vin / Req
VR1 = R1 * I
VR2 = R2 * I

print("Vin (V) | I (A) | VR1 (V) | VR2 (V)")
print("-" * 40)
for i in range(len(Vin)):
    print(f"{Vin[i]:6.0f}  | {I[i]:.4f} | {VR1[i]:6.2f} | {VR2[i]:6.2f}")
