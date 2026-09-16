import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Create a noisy signal
t = np.linspace(0, 1, 1000)
pure_signal = np.sin(2 * np.pi * 5 * t)    # 5 Hz signal
noise = 0.5 * np.random.randn(len(t))      # Random noise
noisy_signal = pure_signal + noise

# Butterworth low-pass filter
fc = 10               # Cutoff frequency 10 Hz
fs = 1000              # Sampling frequency
order = 4
b, a = signal.butter(order, fc / (fs/2), btype='low')
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, alpha=0.5, label='Noisy')
plt.plot(t, pure_signal, 'k--', linewidth=2, label='Pure')
plt.plot(t, filtered_signal, 'r', linewidth=2, label='Filtered')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Low-pass filtering (Butterworth)')
plt.legend()
plt.grid(True)
plt.savefig('02_scientific_calculation/week2/Day5/Signal_filtering.png')
plt.close()