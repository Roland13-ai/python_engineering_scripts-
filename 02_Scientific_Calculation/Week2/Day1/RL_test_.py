import sympy as sp

# Basic symbols
R, C, L, omega = sp.symbols('R C L omega', positive=True)

# The three impedances
Z_R = R                              # Resistance: Z = R
Z_C = 1 / (sp.I * C * omega)         # Capacitor: Z = -j/(Cω)
Z_L = sp.I * L * omega               # Inductance: Z = jLω
"""
print("Resistance impedance:")
sp.pprint(Z_R)

print("\nCapacitor impedance:")
sp.pprint(Z_C)

print("\nInductance impedance:")
sp.pprint(Z_L)"""
def series_association(Z_R, Z_C):
    # Series: we add
    return Z_R + Z_C

def parallel_association(Z_R, Z_C): 
    # Parallel: (Z1*Z2) / (Z1+Z2)
    return (Z_R * Z_C) / (Z_R + Z_C)
  
def impedance_modulus(Z):
    """Returns the symbolic modulus of a complex impedance."""
    return sp.sqrt(sp.re(Z)**2 + sp.im(Z)**2)

# Test 
Z_C_num = Z_C.subs({C: 40, omega: 314})
Z_R_num= Z_R.subs(R, 200)

Z_par= parallel_association(Z_R_num, Z_C_num)
Z_ser= series_association(Z_R_num, Z_C_num)
Z_C_mod= impedance_modulus(Z_R_num)
Z_R_mod= impedance_modulus(Z_C_num)

print(f"Zeq_Series= {Z_ser}")
print(f"Zeq_parallel= {Z_par}") 
print(f"Modulus_ZC= {Z_C_mod}")
print(f"Modulus_ZR= {Z_R_mod}")