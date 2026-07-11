# MIMO Channel Simulation with Python

This Python script models a basic **Multiple-Input Multiple-Output (MIMO)** communication system using the `NumPy` library. It simulates a wireless transmission where a signal vector is transmitted through a flat-fading channel matrix, corrupted by additive white Gaussian noise (AWGN), and received at the destination.

## Code Breakdown

### 1. Library Import

```python
import numpy as np

```

* **What it does:** Imports the NumPy library, which provides powerful tools for handling multi-dimensional arrays, matrices, and complex numbers efficiently.

### 2. Defining Antenna Configuration

```python
# Number of transmit antennas
n_t = 4
# Number of receive antennas
n_r = 2

```

* **What it does:** Sets up the dimensions of our MIMO system.
* **Details:** In this case, we are simulating a $2 \times 4$ MIMO system featuring **4 transmit antennas** ($n_t$) and **2 receive antennas** ($n_r$).

### 3. Generating the MIMO Channel Matrix

```python
# Generating a random MIMO channel matrix
H = np.random.randn(n_r, n_t) + 1j*np.random.randn(n_r, n_t)

```

* **What it does:** Creates a channel matrix $H$ of size $n_r \times n_t$ (2 rows, 4 columns).
* **Details:** Wireless channels shift both the amplitude and phase of a signal, requiring complex numbers. `np.random.randn` generates random values from a standard normal distribution. Adding the real part to the imaginary part (`1j * ...`) creates a **Rayleigh fading channel** (complex Gaussian distribution).

### 4. Simulating the Transmitted Symbols

```python
# Generating a random symbol vector
x = np.random.randn(n_t) + 1j*np.random.randn(n_t)

```

* **What it does:** Creates a vector $x$ containing 4 complex-valued symbols to be transmitted simultaneously from the 4 transmit antennas.

### 5. Adding Wireless Noise

```python
# Generating a noise vector
n = np.random.randn(n_r) + 1j*np.random.randn(n_r)

```

* **What it does:** Generates a complex noise vector $n$ of size 2, representing the Additive White Gaussian Noise (AWGN) introduced at the 2 receive antennas.

### 6. Simulating the Received Signal

```python
# Generating a received signal vector
y = H @ x + n

```

* **What it does:** Computes the final signal vector $y$ arriving at the receiver using the standard linear MIMO model equation:

$$y = Hx + n$$


* **Details:** The `@` operator performs matrix multiplication between the $2 \times 4$ channel matrix $H$ and the $4 \times 1$ transmit vector $x$, resulting in a $2 \times 1$ vector. The noise vector $n$ is then added element-wise.

### 7. Outputting the Results

```python
print("H =", H)
print("x =", x)
print("n =", n)
print("y =", y)

```

* **What it does:** Prints the generated matrices and vectors to the console so you can inspect the values of the channel, sent signal, noise, and resulting received signal.

---

## The Complete Script

```python
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

```
