from scipy.stats import rice
import matplotlib.pyplot as plt

scale = 2
mean = 1
n_samples = 1000

rician_samples = rice.rvs(scale,mean,size=n_samples)

plt.hist(rician_samples, bins=20, density=True, histtype='step')
plt.show()
