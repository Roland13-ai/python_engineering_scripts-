import csv
import matplotlib.pyplot as plt
from pathlib import Path

# Path to the data/ folder
data_dir = Path(__file__).parent / "data"
csv_file = data_dir / "frequency_response_RC.csv"

# Lists to store the data
freqs, modulus, phases = [], [], []

# Reading the CSV
with open(csv_file, encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skips the header line
    for row in reader:
        freqs.append(float(row[0]))
        modulus.append(float(row[1]))
        phases.append(float(row[2]))

# Creating the graph
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.semilogx(freqs, modules)
ax1.set_ylabel("Modulus (Ω)")
ax1.set_title("Frequency response – RC series circuit")
ax1.grid(True)

ax2.semilogx(freqs, phases)
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Phase (°)")
ax2.grid(True)

plt.tight_layout()
plt.savefig(data_dir / "frequency_response_RC.png")
plt.show()

