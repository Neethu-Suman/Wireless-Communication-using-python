import numpy as np
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t) + 1j*np.random.randn(n_r, n_t)
# Generating a random symbol vector
x = np.random.randn(n_t) + 1j*np.random.randn(n_t)
# Generating a noise vector
n = np.random.randn(n_r) + 1j*np.random.randn(n_r)
# Generating a received signal vector
y = H @ x + n
print("H =", H)
print("x =", x)
print("n =", n)
print("y =", y)
