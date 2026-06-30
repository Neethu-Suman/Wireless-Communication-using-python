#Step 1: Importing Dependencies
import numpy as np
import matplotlib.pyplot as plt

#Step 2: Defining the Carrier Signal
# Defining the carrier signal
carrier_freq = 10 # carrier signal frequency
carrier_amp = 1 # carrier signal amplitude
carrier_phase = 0 # carrier signal phase
carrier_time = np.linspace(0, 1, 1000) # carrier signal time
carrier_signal = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)

#Step 3: Defining the Message Signal
# Defining the message signal
message_freq = 2 # message signal frequency
message_amp = 1 # message signal amplitude
message_time = np.linspace(0, 1, 1000) # message signal time
message_signal = message_amp*np.cos(2*np.pi*message_freq*message_time)

#Step 4: Setting the Modulation Index
# Generating the phase modulation index
modulation_index = 0.5
pm_index = modulation_index*message_signal

#Step 5: Generating the Modulated Signal
# Generating the modulated signal
pm_signal = carrier_signal*np.exp(1j*pm_index)

#Step 6: Coherent Demodulation
# Demodulation of the PM signal using coherent demodulation
local_oscillator = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)
demodulated_signal = np.real(pm_signal*np.conj(local_oscillator))

#Step 7: Plotting the Results
# Plotting the modulated and demodulated signal
plt.plot(carrier_time, np.real(pm_signal), label='Modulated signal')
plt.plot(carrier_time, demodulated_signal, label='Demodulated signal')
plt.legend()
plt.show()
