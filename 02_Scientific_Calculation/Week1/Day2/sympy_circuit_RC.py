"""Declare R, C, omega as positive symbols
Write ZC = 1/(j × C × omega)
Write Z_eq = R + ZC
Calculate the modulus |Z| (exact formula)
Replace R=1000, C=1e-6, omega=314 and display the numerical value with sp.N()
"""
import sympy as sp 
R, C , omega = sp.symbols('R, C , omega', positive = True )
j= sp.I
ZC = 1/(j*C*omega)
Z_eq = R + ZC 
sp.pprint(sp.simplify(Z_eq))
Mod_Z = sp.sqrt(R**2 + sp.im(ZC)**2)
sp.pprint(sp.simplify(Mod_Z))
Val_num = Mod_Z.subs({ R:1000, C:1e-6, omega:314})
sp.pprint(sp.N(Val_num))