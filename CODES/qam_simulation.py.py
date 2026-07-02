#Step 1: Importing Dependencies

import numpy as np
import matplotlib.pyplot as plt

#Step 2: Defining the Carrier Signal

carrier_freq = 10  # carrier signal frequency in Hz
carrier_amp = 1  # carrier signal amplitude
carrier_time = np.linspace(0, 1, 1000)  # carrier signal time
carrier_signal = carrier_amp * np.cos(2 * np.pi * carrier_freq * carrier_time)

#Step 3: Generating the Digital Data

message_binary = np.random.randint(2, size=8)  # generates a random 8-bit message signal
message_signal = message_binary.reshape(2, 4)  # reshaping the message signal to 2x4 matrix

#Step 4: Generating the QAM Signal

qam_signal = np.zeros_like(carrier_signal, dtype=np.complex128)
for i in range(4):
    if message_signal[0, i] == 0:
        qam_signal += (carrier_amp / 2) * np.cos(2 * np.pi * carrier_freq * carrier_time + (np.pi / 2) * message_signal[1, i])
    else:
        qam_signal += (carrier_amp / 2) * np.cos(2 * np.pi * carrier_freq * carrier_time - (np.pi / 2) * message_signal[1, i])

# Step 5: Demodulation Process
# Demodulation of the QAM signal
demodulated_signal = np.zeros_like(message_signal)
for i in range(4):
  demodulated_signal[1, i] = int(np.mean(np.angle(qam_signal[i*250:i*250+250])) > 0)
  
#Step 6: Visualization
# create new time axis
new_time = np.linspace(0, 1, 4)
plt.plot(carrier_time, np.real(qam_signal), label='Modulated signal')
plt.plot(new_time, demodulated_signal[1,:], label='Demodulated signal')
plt.show()
