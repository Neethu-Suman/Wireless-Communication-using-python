# Rayleigh Fading Channel Simulation in Python

This repository contains a simple Python script that simulates the characteristics of a **Rayleigh Fading Channel** using **NumPy**. It generates random samples that model multi-path radio signal propagation in wireless communication environments.

## 📌 Project Overview

Rayleigh fading is a statistical model used to describe the effect of a propagation environment on a radio signal. It is typically used to model wireless environments with no dominant line-of-sight (LoS) path between the transmitter and the receiver, such as dense urban areas where signals bounce off buildings, walls, and other obstructions.

The mathematical Probability Density Function (PDF) of a Rayleigh distribution is represented as:

$$f(x; \sigma) = \frac{x}{\sigma^2} e^{-\frac{x^2}{2\sigma^2}}, \quad x \ge 0$$

Where $\sigma$ is the scale parameter representing the root-mean-square (RMS) value of the received components.

---

## 📖 Step-by-Step Code Explanation

### Step 1: Importing NumPy

The script begins by importing `numpy`. This library is essential for scientific computing and contains a built-in module for drawing random samples from specialized statistical distributions.

```python
import numpy as np

```

### Step 2: Defining Channel Parameters

Next, we define our simulation constants. We set the total number of data points to generate ($5$) and set the statistical scale parameter ($\sigma = 1$), which dictates the peak amplitude dispersion of the fading environment.

```python
# Number of samples
n_samples = 5
# Scale parameter for the Rayleigh distribution
scale = 1

```

### Step 3: Generating Fading Channel Samples

The script utilizes the function `np.random.rayleigh()` to simulate the channel. Behind the scenes, this function generates pairs of independent normally distributed random variables (representing the In-phase and Quadrature components of a radio wave) and calculates their magnitude, yielding Rayleigh distributed coefficients.

```python
# Generating samples of a Rayleigh fading channel
rayleigh_samples = np.random.rayleigh(scale, n_samples)

```

### Step 4: Printing Output

Finally, the generated array containing the $1000$ amplitude scaling factors is printed to the console window. These values simulate how a transmitted signal's amplitude would fluctuates wildly over time due to multi-path interference.

```python
print(rayleigh_samples)

```

---

[1.73657908 0.63855817 0.42353736 0.91408733 0.82422608]

## 🚀 How to Run the Script

1. **Install Requirements:**
```bash
pip install numpy

```


2. **Save the Code:**

Save the full snippet into a file named `rayleigh_simulation.py`.

3. **Execute:**

Run the file directly via your terminal:

```bash
python rayleigh_simulation.py

```
