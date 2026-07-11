# Beamforming
import numpy as np
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Desired angle of arrival
theta_d = np.pi/4
# Generating a beamforming vector
w = np.exp(1j*np.arange(n_t)*np.pi*np.sin(theta_d))

# Printing the beamforming vector
print("Beamforming Vector: ", w)