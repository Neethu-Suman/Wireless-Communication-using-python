# Massive MIMO Channel & Signal Transmission Simulation in Python

This repository contains a Python script that models signal transmission over a **Massive MIMO (Multiple-Input Multiple-Output)** channel using **NumPy**.

## 📌 Project Overview

Massive MIMO is a core technology for modern 5G and 6G wireless networks. By deploying large antenna arrays at the base station (transmitter), massive MIMO systems can focus energy toward target users via beamforming and handle simultaneous transmissions over identical frequency bands.

This script demonstrates a basic transmission simulation involving:

1. Setting up a large-scale antenna array ($128$ transmit antennas $\times$ $32$ receive antennas).
2. Generating a physical channel gain matrix.
3. Defining precoding and combining matrices.
4. Simulating signal propagation across the channel and displaying the received data.

---

## 📖 Step-by-Step Code Explanation

### Step 1: Importing Dependencies

The script begins by importing `numpy` to manage large multidimensional matrices and linear algebra calculations.

```python
import numpy as np

```

### Step 2: Defining Antenna Array Dimensions

The script configures a Massive MIMO system featuring $128$ antennas at the transmitter (`num_tx_antennas = 128`) and $32$ antennas at the receiver (`num_rx_antennas = 32`).

```python
# Define the number of antennas at the transmitter and receiver
num_tx_antennas = 128
num_rx_antennas = 32

```

### Step 3: Generating the Channel Matrix

The script constructs the channel matrix `channel_matrix` of shape $32 \times 128$ ($N_{Rx} \times N_{Tx}$) populated with standard normal random values. Each element $H_{i,j}$ represents the complex path attenuation between transmit antenna $j$ and receive antenna $i$.

```python
# Generate the channel matrix
channel_matrix = np.random.randn(num_rx_antennas, num_tx_antennas)

```

### Step 4: Defining Precoding and Combining Matrices

The code calculates a Zero-Forcing (ZF) style pseudoinverse precoding matrix (`precoding_matrix`) using `np.linalg.pinv()`. It also initializes an identity matrix (`np.eye`) for the receiver's `combining_matrix`, representing an unweighted, direct signal reception across the $32$ receive paths.

```python
# Perform precoding and combining
precoding_matrix = np.linalg.pinv(channel_matrix)
combining_matrix = np.eye(num_rx_antennas)

```

### Step 5: Transmitting and Receiving Data

A random vector of $128$ symbols (`transmitted_data`) is generated. Signal propagation across the wireless link is computed using matrix multiplication (`@`), where the raw transmitted vector is transformed by the channel matrix and collected via the receive combining matrix.

```python
# Transmit and receive data
transmitted_data = np.random.randn(num_tx_antennas, 1)
received_data = combining_matrix @ (channel_matrix @ transmitted_data)

```

> 💡 **Technical Note:** In this specific script, the `precoding_matrix` variable is computed but not directly multiplied into `transmitted_data`. To apply Zero-Forcing precoding in the transmission path, the transmission equation can be updated to:
> ```python
> received_data = combining_matrix @ (channel_matrix @ precoding_matrix @ user_symbols)
> 
> ```
> 
> 

### Step 6: Displaying the Received Signal

Finally, the resulting $32 \times 1$ received data vector is printed directly to the terminal console.

```python
# Print the received data
print("Received data: \n", received_data)

```

---

## 🚀 How to Run the Script

1. **Install Requirements:**
Make sure you have `numpy` installed:
```bash
pip install numpy

```


2. **Save the Code:** Copy the full Python snippet into a local file named `massive_mimo.py`.
3. **Execute:** Run the script using your terminal:
```bash
python massive_mimo.py

```
