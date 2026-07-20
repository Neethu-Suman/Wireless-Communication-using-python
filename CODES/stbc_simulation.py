import numpy as np
# Number of transmit and receive antennas
Nt = 4
Nr = 4
# Generate a random data symbol vector
data = np.random.randint(0, 2, Nt)
# Generate the Space-Time Block Code matrix
STBC = np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
# Encode the data symbol vector using the STBC matrix
encoded_data = np.matmul(STBC, data)
# Add noise to the encoded data symbols
noise = np.random.normal(0, 0.1, (Nr, 1))
received_data = encoded_data + noise
# Use the STBC matrix to decode the received data symbols
decoded_data = np.matmul(STBC.T, received_data)
# Print the original and decoded data symbols
print("Original Data:", data)
print("Decoded Data:", decoded_data)
