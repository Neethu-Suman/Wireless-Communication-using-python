# Step 1: Importing Dependencies
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Defining the Carrier Signal
carrier_freq = 10 # carrier signal frequency
carrier_amp = 1 # carrier signal amplitude
carrier_phase = 0 # carrier signal phase
carrier_time = np.linspace(0, 1, 1000) # carrier signal time
carrier_signal = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)

# Step 3: Defining the Message Signal
message_freq = 2 # message signal frequency
message_amp = 1 # message signal amplitude
message_phase = 0 # message signal phase
message_time = np.linspace(0, 1, 1000) # message signal time
message_signal = message_amp*np.cos(2*np.pi*message_freq*message_time + message_phase)

# Step 4: Signal Modulation (DSB-SC)
# Multiplying the carrier signal and the message signal to generate AM signal
am_signal = carrier_signal*message_signal

# Step 5: Demodulation Process
# Demodulation of the AM signal to obtain the original message signal
envelope_detector = np.abs(am_signal) # Using the absolute value of the AM signal
demodulated_signal = envelope_detector*np.cos(2*np.pi*message_freq*message_time + message_phase)

# Step 6: Plotting the Results
# Plotting the modulated and demodulated signal
plt.plot(carrier_time, am_signal, label='Modulated signal')
plt.plot(carrier_time, demodulated_signal, label='Demodulated signal')
plt.legend()
plt.show()
