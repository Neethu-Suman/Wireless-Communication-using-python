# MIMO Channel Matrix Simulation in Python

This repository contains a simple Python script that simulates the physical propagation environment of a **Multiple-Input Multiple-Output (MIMO)** wireless communication system using **NumPy**.

## 📌 Project Overview

MIMO is an antenna technology used in modern wireless communications (such as 5G and Wi-Fi 6) where multiple antennas are used at both the transmitter (source) and the receiver (destination).

The relationships between all transmit and receive antenna paths are mathematically grouped into a **Channel Matrix** ($H$). For a system with $N_T$ transmit antennas and $N_R$ receive antennas, the channel matrix is structured as:

$$H = \begin{pmatrix} 
h_{11} & h_{12} & \cdots & h_{1N_T} \\
h_{21} & h_{22} & \cdots & h_{2N_T} \\
\vdots & \vdots & \ddots & \vdots \\
h_{N_R1} & h_{N_R2} & \cdots & h_{N_RN_T}
\end{pmatrix}$$

Where each element $h_{ij}$ represents the complex attenuation (gain and phase shift) of the wireless path from the $j$-th transmit antenna to the $i$-th receive antenna.

---

## 📖 Step-by-Step Code Explanation

### Step 1: Importing NumPy

The script begins by importing `numpy`. This library is required to create multidimensional matrices and generate random statistical distributions.

```python
import numpy as np

```

### Step 2: Defining Antenna Configurations

The script defines the configuration of the antenna arrays. Here, we set up a $4 \times 2$ MIMO system, meaning the transmitter has $4$ antennas ($n_t = 4$) and the receiver has $2$ antennas ($n_r = 2$).

```python
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2

```

### Step 3: Generating the Random MIMO Channel Matrix

The script uses `np.random.randn()` to build the channel matrix $H$. The function populates a matrix of shape `(n_r, n_t)`—which is $2 \times 4$ in this case—with random values drawn from a standard normal distribution (zero mean and unit variance). This models a scattering radio environment with no line-of-sight path, often referred to as Rayleigh fading.

```python
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t)

```

### Step 4: Printing the Matrix

Finally, the resulting $2 \times 4$ channel matrix is printed to the console window so you can view the independent fading paths generated for the simulation.

```python
# Printing the MIMO channel matrix
print("MIMO Channel Matrix: ", H)

```

## Output

MIMO Channel Matrix:  [[-0.47772002  0.64826043 -0.12883684  0.15489875]
                      [-1.89634973 -0.61273039  0.95666314 -0.53427743]]

## 🚀 How to Run the Script

1. **Install Requirements:**
```bash
pip install numpy

```


2. **Save the Code:**

Save the full snippet into a file named 

`mimo_simulation.py`.

3. **Execute:**

Run the file directly via your terminal:
```bash
python mimo_simulation.py

```
