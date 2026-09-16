import numpy as np
import matplotlib.pyplot as plt

octave:1> % Circuit parameters
octave:1> R = 1000;
octave:2> C = 1e-6;
octave:3> % Generate 100 frequencies from 1 Hz to 100 kHz
octave:3> f = logspace(0, 5, 100);
octave:4> % Calculate the impedance for each frequency
octave:4> Z_R = R * ones(size(f));
octave:5> Z_C = 1 / (1*j * 2 * pi * f * C);
octave:6> Z_eq = Z_R + Z_C;
octave:7> % Modulus and phase
octave:7> module = abs(Z_eq);
octave:8> phase = angle(Z_eq) * 180 / pi;
octave:9> % Plot
octave:9> subplot(2,1,1);
octave:10> semilogx(f, module);
octave:11> ylabel('Modulus (Ohm)');
octave:12> title('Frequency response - RC series (Octave)');
octave:13> grid on;
octave:14> subplot(2,1,2);
octave:15> semilogx(f, phase);
octave:16> xlabel('Frequency (Hz)');
octave:17> ylabel('Phase (deg)');
octave:18> grid on;
octave:19> print -dpng frequency_response_RC_octave.png
octave:20> pwd
ans = C:\Users\ADMIN
octave:21>(* f * C) 
Z_eq = Z_R + Z_C
module = np.abs(Z_eq)
phase = np.angle(Z_eq, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.semilogx(f, module, 'b', linewidth=1.5)
ax1.set_ylabel('Modulus (Ohm)')
ax1.set_title('Frequency response - RC series circuit')
ax1.grid(True)

ax2.semilogx(f, phase, 'r', linewidth=1.5)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('02_scientific_computing/week2/day10/frequency_response_RC.png')
plt.show()
print("Graph saved successfully.")