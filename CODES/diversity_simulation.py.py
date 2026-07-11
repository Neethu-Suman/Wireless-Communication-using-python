#Diversity
import numpy as np
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t)
# Generating a diversity combining vector
w = np.ones(n_r)

print("Number of transmit antennas: ", n_t)
print("Number of receive antennas: ", n_r)
print("Random MIMO channel matrix: \n", H)
print("Diversity combining vector: \n", w)