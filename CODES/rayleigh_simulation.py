import numpy as np
# Number of samples
n_samples = 5
# Scale parameter for the Rayleigh distribution
scale = 1
# Generating samples of a Rayleigh fading channel
rayleigh_samples = np.random.rayleigh(scale, n_samples)
print(rayleigh_samples)
