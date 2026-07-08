# Antenna Array Beamforming Vector Simulation in Python

This repository contains a simple Python script that calculates the complex weight coefficients for digital **Beamforming** in a multi-antenna wireless communication system using **NumPy**.

## 📌 Project Overview

Beamforming is a signal processing technique used in sensor and antenna arrays to directionalize signal transmission or reception. Instead of broadcasting energy omnidirectionally (in all directions), the signals from multiple antennas are phased-shifted so that they constructively interfere at a specific spatial angle ($\theta_d$) and destructively interfere in others.

For a linear antenna array with uniform element spacing of half-wavelength ($d = \frac{\lambda}{2}$), the steering or beamforming vector $w$ needed to direct a beam toward an Angle of Arrival/Departure ($\theta$) is mathematically modeled as:

$$w = \begin{bmatrix} 1 \\ 
e^{j\pi\sin(\theta)} \\ 
e^{j2\pi\sin(\theta)} \\ 
\vdots \\ 
e^{j(N_T-1)\pi\sin(\theta)} \end{bmatrix}$$


## 📖 Step-by-Step Code Explanation

### Step 1: Importing NumPy

The script begins by importing `numpy` to manipulate arrays and solve trigonometric calculations using complex numbers.

```python
import numpy as np

```

### Step 2: Setting Antenna and Geometric Configurations

The parameters define a base station or device equipped with $4$ transmit antennas ($n_t = 4$) and $2$ receive antennas ($n_r = 2$). The target direction or Angle of Arrival (AoA) where we want to steer our signal beam is set to $45^\circ$ ($\theta_d = \frac{\pi}{4}$ radians).

```python
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2
# Desired angle of arrival
theta_d = np.pi/4

```

> Note: While `n_r` is defined in the variables, the beamforming vector generated below specifically focuses on weights applied across the transmit array (`n_t`).

### Step 3: Computing the Complex Beamforming Vector

The script creates the progressive phase shifts required across each physical antenna element using Euler's formula ($e^{j\phi}$).

```python
# Generating a beamforming vector
w = np.exp(1j*np.arange(n_t)*np.pi*np.sin(theta_d))

```

* `np.arange(n_t)` creates an index array `[0, 1, 2, 3]` representing the sequential spatial position of each antenna element.
* Multiplying by `1j` ensures the calculation handles complex numbers (imaginary numbers, where $j = \sqrt{-1}$).
* This maps an incremental phase delay across the array line, allowing the physical wave front to tilt precisely toward $\frac{\pi}{4}$.

### Step 4: Printing the Weight Coefficients

Finally, the array of $4$ complex exponential weight elements is printed to the console window. Each complex number dictates the specific amplitude gain and phase offset needed on that antenna path.

```python
# Printing the beamforming vector
print("Beamforming Vector: ", w)

```

---

## 🚀 How to Run the Script

1. **Install Requirements:**
```bash
pip install numpy

```


2. **Save the Code:** Save the full snippet into a file named `beamforming_simulation.py`.
3. **Execute:** Run the file directly via your terminal:
```bash
python beamforming_simulation.py

```
