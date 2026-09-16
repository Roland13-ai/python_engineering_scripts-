import numpy as np 

# Circuit : R = 100Ω, C = 0.000001F
R= 100
C= 1e-6
pi = np.pi
f= np.logspace(0,5,50)
# 
ZC= -1/C*2*pi*f
Z= np.sqrt(R**2+ZC**2)
phi= 1/C*R*2*pi*f

print("-"*60)
for i in range(len(f)):
    print(f"{f[i]:.1f}   |  {Z[i]:6.3f}    |    {phi[i]:.2f}   |    ")
print("-"*60)