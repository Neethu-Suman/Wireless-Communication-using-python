import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

# Defining the parameters
num_bits = int(1e6) # number of bits to simulate
snr_db = np.linspace(0, 20, 21) # range of snr in dB
snr = np.power(10, snr_db / 10) # converting snr from dB to linear scale
# Generating the data
data = np.random.randint(2, size=num_bits) # generating random binary data
# Modulation
modulated_data = 2*data - 1 # BPSK modulation

ber = np.zeros(len(snr)) # Initializing the bit error rate array
# Loop over different snr values
for i in range(len(snr)):
    # Adding noise
    noise = np.sqrt(1 / (2 * snr[i])) * np.random.randn(num_bits) # generating gaussian noise
    received_signal = modulated_data + noise # adding noise to the modulated signal
    # Demodulation
    demodulated_data = (received_signal > 0)*1 # demodulating
    # Calculating the bit error rate
    ber[i] = np.sum(data != demodulated_data) / num_bits

# Plotting the BER
plt.semilogy(snr_db, ber, 'bo-')
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate')
plt.title('BER for BPSK')
plt.grid()
plt.show()