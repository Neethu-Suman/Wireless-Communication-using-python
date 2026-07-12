import numpy as np
from numpy.linalg import det
from math import log2

# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t) + 1j*np.random.randn(n_r, n_t)
# Noise power
N0 = 1
# Diversity gain
SNR_0 = N0/np.trace(H @ H.conj().T)
G_d = 1/(1 + (1 - 1/n_r) * SNR_0)
print("Diversity gain:", G_d)
