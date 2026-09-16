# --- Series association ---
class SeriesAssociation:
    def __init__(self, R1, R2, Vin):
        self.R1 = R1
        self.R2 = R2
        self.Vin = Vin
    
    def calculate(self):
        self.Req = self.R1 + self.R2
        self.I = self.Vin / self.Req
        print(f"Req = {self.Req:.2f} Ω")
        print(f"I = {self.I:.4f} A")
    
    def voltage_R1(self):
        VR1 = (self.Vin * self.R1) / (self.R1 + self.R2)
        print(f"VR1 = {VR1:.2f} V")
        return VR1
    
    def voltage_R2(self):
        VR2 = (self.Vin * self.R2) / (self.R1 + self.R2)
        print(f"VR2 = {VR2:.2f} V")
        return VR2


# --- Parallel association ---
class ParallelAssociation:
    def __init__(self, R1, R2, I_total):
        self.R1 = R1
        self.R2 = R2
        self.I_total = I_total
    
    def calculate(self):
        self.Req = (self.R1 * self.R2) / (self.R1 + self.R2)
        self.V = self.Req * self.I_total
        print(f"Req = {self.Req:.2f} Ω")
        print(f"V = {self.V:.2f} V")
    
    def current_R1(self):
        I1 = (self.I_total * self.R2) / (self.R1 + self.R2)
        print(f"I1 = {I1:.4f} A")
        return I1
    
    def current_R2(self):
        I2 = (self.I_total * self.R1) / (self.R1 + self.R2)
        print(f"I2 = {I2:.4f} A")
        return I2


# --- Main program ---
print("=== Voltage divider ===")
print("1 - Series")
print("2 - Parallel")
choice = int(input("Your choice: "))

R1 = float(input("R1 (Ω): "))
R2 = float(input("R2 (Ω): "))

if choice == 1:
    Vin = float(input("Vin (V): "))
    circuit = SeriesAssociation(R1, R2, Vin)
    circuit.calculate()
    
    option = int(input("\n1 - Voltage R1 | 2 - Voltage R2: "))
    if option == 1:
        circuit.voltage_R1()
    elif option == 2:
        circuit.voltage_R2()

elif choice == 2:
    I_total = float(input("I total (A): "))
    circuit = ParallelAssociation(R1, R2, I_total)
    circuit.calculate()
    
    option = int(input("\n1 - Current R1 | 2 - Current R2: "))
    if option == 1:
        circuit.current_R1()
    elif option == 2:
        circuit.current_R2()

else:
    print("Invalid choice.")