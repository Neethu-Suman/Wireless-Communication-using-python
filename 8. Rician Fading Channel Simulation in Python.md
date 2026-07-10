# Rician Fading Channel Simulation in Python

This repository contains a Python script that simulates a **Rician Fading Channel** using **SciPy** for statistical generation and **Matplotlib** for data visualization.

## 📌 Project Overview

Rician fading is a stochastic model used to describe the anomaly of signal propagation in wireless communications. Unlike Rayleigh fading, a Rician fading environment contains a dominant **Line-of-Sight (LoS)** direct path between the transmitter and the receiver, alongside multiple scattered, indirect multi-path components.

The distribution transitions based on the strength of the direct path:

* If the direct path is exceptionally strong, the distribution resembles a Gaussian/Normal distribution.
* If the direct path fades to zero, the channel simplifies directly into a **Rayleigh distribution**.



## 📖 Step-by-Step Code Explanation

### Step 1: Importing Dependencies

The script starts by importing the `rice` module from `scipy.stats` to handle the heavy statistical math and distribution sampling, along with `matplotlib.pyplot` to render the histogram.

```python
from scipy.stats import rice
import matplotlib.pyplot as plt

```

### Step 2: Defining Channel Parameters

Three variables configure the simulation environment:

* `scale`: Controls the scaling or dispersion of the non-line-of-sight scatter components.
* `mean`: Represents the distance of the shifting parameter (the strength of the direct Line-of-Sight signal).
* `n_samples`: The total number of random data points ($1000$) to collect.

```python
scale = 2
mean = 1
n_samples = 1000

```

### Step 3: Generating Rician Fading Samples

The function `rice.rvs()` draws Random Variates (samples) following the Rician probability envelope based on the scale, shape, and size constraints we defined above.

```python
rician_samples = rice.rvs(scale, mean, size=n_samples)

```

### Step 4: Visualizing the Probability Density

Finally, the script bins the $1000$ random samples into a histogram. Setting `density=True` scales the vertical axis so the area of the histogram sums to 1, effectively turning the plot into an empirical Probability Density Function (PDF) curve. `histtype='step'` draws the graph as a clean, unfilled line rather than solid blocks.

```python
plt.hist(rician_samples, bins=20, density=True, histtype='step')
plt.show()

```

## Output

<img src ="https://github.com/Neethu-Suman/Wireless-Communication-using-python/blob/main/Images/rician.jpeg">

## 🚀 How to Run the Script

1. **Install Requirements:**

```bash
pip install numpy scipy matplotlib

```

2. **Save the Code:**

   Save the full snippet into a file named

   `rician_simulation.py`.

3. **Execute:**
  
   Run the file directly via your terminal:

```bash
python rician_simulation.py

```
