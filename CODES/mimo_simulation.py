import numpy as np
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t)

# Printing the MIMO channel matrix
print("MIMO Channel Matrix: ", H)