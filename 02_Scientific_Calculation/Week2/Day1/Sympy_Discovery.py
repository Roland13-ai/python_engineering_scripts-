import sympy as sp

# -------------------------------
# 1. Define symbols
# -------------------------------
# We declare variables that do NOT contain numbers,
# but letters (as in math).
R, C, L, omega = sp.symbols('R C L omega', positive=True)

# -------------------------------
# 2. Capacitor impedance
# -------------------------------
# In electricity: Zc = 1 / (j*C*omega)
# sp.I represents the imaginary number j
Zc = 1 / (sp.I * C * omega)
print("Capacitor impedance:")
print("Zc =", Zc)

# -------------------------------
# 3. Inductor impedance
# -------------------------------
Zl = sp.I * L * omega
print("\nInductor impedance:")
print("Zl =", Zl)

# -------------------------------
# 4. RC series circuit
# -------------------------------
Z_R = R
Z_eq = Z_R + Zc
print("\nEquivalent RC series impedance:")
print("Z_eq =", Z_eq)

# -------------------------------
# 5. Impedance modulus
# -------------------------------
# The modulus of a complex a+bj is sqrt(a² + b²)
module_squared = sp.re(Z_eq)**2 + sp.im(Z_eq)**2
module = sp.sqrt(sp.simplify(module_squared))
print("\nModulus of Z_eq:")
print("|Z| =", module)

# -------------------------------
# 6. Solve an equation
# -------------------------------
# Question: for which angular frequency ω does the modulus equal R/2?
# We create an equation: |Z| = R/2
equation = sp.Eq(module, R/2)
solution = sp.solve(equation, omega)
print("\nAngular frequency for which |Z| = R/2:")
print("ω =", solution)

# Exercise: impedance of a parallel RL circuit
Z_RL_parallel = (R * Zl) / (R + Zl)
sp.simpli(Z_RL_parallel)
print("\nParallel RL impedance:")
sp.pprint(Z_RL_parallel)   # Displays the formula 