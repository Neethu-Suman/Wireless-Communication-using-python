# Antenna Diversity Combining Simulation in Python

This repository contains a simple Python script that simulates the foundational parameters for **Antenna Diversity** in a Multiple-Input Multiple-Output (MIMO) wireless communication system using **NumPy**.

## 📌 Project Overview

Antenna diversity (also known as space diversity) is a wireless transmission technique that uses two or more antennas to improve the reliability and quality of a wireless link. In fading channels, signals bounce off obstacles and arrive at different times or strengths. By using multiple receive antennas, the system can combine the unique signal paths to mitigate deep fades.

The relationships between all antenna paths are mathematically grouped into a **Channel Matrix** ($H$), while a **Combining Vector** ($w$) represents the weights applied at the receiver to merge these incoming signals (e.g., using a basic Equal Gain Combining technique where all paths are weighted equally).

---

## 📖 Step-by-Step Code Explanation

### Step 1: Importing NumPy

The script begins by importing `numpy` to handle matrix creation and generation of random statistical fading environments.

```python
import numpy as np

```

### Step 2: Defining Antenna Configurations

The script defines the layout of the antenna arrays. This sets up a MIMO link with $4$ transmit antennas ($n_t = 4$) and $2$ receive antennas ($n_r = 2$).

```python
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2

```

### Step 3: Generating the Random MIMO Channel Matrix

The script uses `np.random.randn()` to build a channel matrix $H$ of shape `(n_r, n_t)`—which evaluates to a $2 \times 4$ grid. The elements are drawn from a standard normal distribution, simulating independent Rayleigh fading channels across all paths between the transmitter and receiver.

```python
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t)

```

### Step 4: Creating the Diversity Combining Vector

To combine the signals received across the $2$ receive antennas, the script initializes a combining vector $w$ populated with $1$s using `np.ones(n_r)`.

```python
# Generating a diversity combining vector
w = np.ones(n_r)

```

> 💡 **Technical Note:** In wireless receivers, this represents **Equal Gain Combining (EGC)**, where the signals from both receive antennas are summed with equal weight, rather than scaling them dynamically based on individual channel conditions like in Maximum Ratio Combining (MRC).

### Step 5: Printing the Configuration and Outputs

Finally, the script displays the antenna numbers, the random channel matrix paths, and the uniform weight vector in the terminal.

```python
print("Number of transmit antennas: ", n_t)
print("Number of receive antennas: ", n_r)
print("Random MIMO channel matrix: \n", H)
print("Diversity combining vector: \n", w)

```

---

## 🚀 How to Run the Script

1. **Install Requirements:**
```bash
pip install numpy

```


2. **Save the Code:** Save the full snippet into a file named `diversity_simulation.py`.
3. **Execute:** Run the file directly via your terminal:
```bash
python diversity_simulation.py

```
