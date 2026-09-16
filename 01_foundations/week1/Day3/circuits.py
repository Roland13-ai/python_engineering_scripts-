""" Module for calculating elementary electrical impedances.
Uses complex numbers to represent impedances. """
import numpy as np 
def impedance_resistance(r):
    "Returns the impedance of a resistor (real number)."
    return  complex(r, 0)
def impedance_capacitor(c, frequency):
    """ Returns the impedance of a capacitor: Zc= -j/wC"""
    omega = 2* np.pi * frequency
    return complex(0, -1/(omega* c))
def impedance_inductor(l, frequency):
    """Returns the impedance of an inductor"""
    return complex(0, omega * l)
def impedance_series(z1, z2):
    """ Returns the equivalent impedance of two impedances in series"""
    return  z1 +z2
def impedance_parallel(z1,z2,z3):
    """Returns the equivalent impedance of two impedances in parallel."""
    return (z1*z2*z3)/(z1*z2+z2z3+z1*z3) 
def modulus_and_phase(z):
    """ Returns the modulus (ohm) and phase (degrees) of an impedance """
    return abs(z) , np.angle(z, deg= True)
