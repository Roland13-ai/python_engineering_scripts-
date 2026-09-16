import csv
import numpy as np 
from pathlib import Path
import sys


# Adds the day3 folder to the path to import circuits
sys.path.insert(0, str(Path(__file__).parent.parent / "day3"))
from circuits import impedance_resistance, impedance_capacitor, impedance_series, modulus_and_phase

# Circuit parameters
R = 1000         # 1 kΩ
C = 1e-6         # 1 µF
frequencies = np.logspace(0, 5, 50)  # 50 frequencies from 1 Hz to 100 kHz

# Creates the data/ folder if it does not exist
data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)

# Output CSV file
csv_file = data_dir / "frequency_response_RC.csv"

# Writing the CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Frequency (Hz)", "Modulus (Ohm)", "Phase (deg)"])  # Header
    for f_req in frequencies:
        z_r = impedance_resistance(R)
        z_c = impedance_capacitor(C, f_req)
        z_eq = impedance_series(z_r, z_c)
        module, phase = modulus_and_phase(z_eq)
        writer.writerow([f"{f_req:.2f}", f"{module:.2f}", f"{phase:.2f}"])

print(f"File created: {csv_file}")
print(f"Number of lines: {len(frequencies)}")

