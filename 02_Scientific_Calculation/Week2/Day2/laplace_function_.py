import sympy as sp

# 1. Declaration of symbols
s = sp.symbols('s')
R, C = sp.symbols('R C', positive=True)

# 2. Laplace impedances
Z_C_s = 1 / (s * C)
Z_R_s = R

print("Z_C(s) =")
sp.pprint(Z_C_s)

# 3. Transfer function
H_s = Z_C_s / (Z_R_s + Z_C_s)
H_s_simple = sp.simplify(H_s)

print("\nSimplified H(s) =")
sp.pprint(H_s_simple)

# 4. Numerical substitution
R_val = 1000
C_val = 1e-6
H_s_num = H_s_simple.subs({R: R_val, C: C_val})

print("\nH(s) with R=1kΩ, C=1µF:")
sp.pprint(H_s_num)

# 5. Time constant
tau = R_val * C_val
print(f"\nTime constant τ = {tau} s")