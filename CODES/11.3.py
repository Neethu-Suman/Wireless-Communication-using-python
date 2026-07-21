import numpy as np

# Define the number of antennas at the transmitter and receiver
num_tx_antennas = 128
num_rx_antennas = 32

# Generate the channel matrix
channel_matrix = np.random.randn(num_rx_antennas, num_tx_antennas)

# Perform precoding and combining
precoding_matrix = np.linalg.pinv(channel_matrix)
combining_matrix = np.eye(num_rx_antennas)

# Transmit and receive data
transmitted_data = np.random.randn(num_tx_antennas, 1)
received_data = combining_matrix @ (channel_matrix @ transmitted_data)

# Print the received data
print("Received data: \n", received_data)