import numpy as np
# Generate a random binary data stream with a length of 1000
data = np.random.randint(0, 2, 1000)
# Pad the data with zeros to make its length a multiple of 64 * 16
padding = (64 * 16) - (len(data) % (64 * 16))
data = np.pad(data, (0, padding), mode='constant')
# Reshape the data into a 2D array with 64 rows and 16 columns
data = data.reshape((-1, 64 * 16))
# Perform OFDM modulation on the data
# This example uses 64 subcarriers and a cyclic prefix of 16 samples
ofdm_symbols = np.zeros((64, data.shape[0], 16), dtype=complex)
for i in range(data.shape[0]):
    ofdm_symbols[:, i, :] = np.fft.fft(data[i, :].reshape((64, 16)), axis=1)
# Perform the inverse FFT on the OFDM symbols to obtain the time domain signal
ofdm_signal = np.fft.ifft(ofdm_symbols, axis=2)
print(ofdm_signal)