# Stop-and-Wait ARQ Protocol Simulation in Python

This repository contains a Python script that simulates a fundamental networking concept: the **Stop-and-Wait Automatic Repeat reQuest (ARQ)** error control protocol. It models frame transmissions through an 
imperfect channel and calculates transmission efficiency.

## 📌 Project Overview

In computer networks, the Stop-and-Wait ARQ protocol ensures reliable data transmission over unreliable channels. The sender transmits one data frame and then stops to wait for feedback from the receiver:

* **ACK (Acknowledgement):** Signals that the frame arrived safely; the sender can move to the next frame.
* **NAK (Negative Acknowledgement):** Signals that the frame was corrupted or lost; the sender must retransmit the same frame.

# 📖 Step-by-Step Code Explanation

## Step 1: Importing Dependencies

The script begins by importing the native Python `random` module, which is used to mimic the unpredictable nature of network channel noise.

```python
import random

```

### Step 2: Defining the Simulation Parameters

We configure the parameters for our network simulation environment. We set a simulation size of $100$ unique frames and a channel error probability of $10\%$ ($0.1$). We also initialize trackers for our total transmissions and errors.

```python
# Number of frames to be transmitted
n_frames = 100
# Probability of error in the channel
p_error = 0.1
# Initializing counters
n_transmissions = 0
n_errors = 0

```

### Step 3: Simulating Frame Transmission & Channel Noise

The code enters a `for` loop to transmit each frame sequentially. For each attempt, it increments our tracking counter. It then samples a floating-point number between $0.0$ and $1.0$ using `random.random()`. If this number falls below our threshold (`p_error`), a channel error is triggered.

```python
# Transmitting the frames
for i in range(n_frames):
    # Incrementing the number of transmissions
    n_transmissions += 1

    # Generating random error
    if random.random() < p_error:
        n_errors += 1
        # Sending NAK
        print("NAK received, retransmitting frame", i)
    else:
        # Sending ACK
        print("ACK received, frame", i, "transmitted successfully")

```

> ⚠️ **Note on Protocol Logic:** While the print statement explicitly states *"retransmitting frame i"*, this basic script continues to the next item in the loop (`i + 1`) rather than actually executing a loop reset to retransmit. In a full implementation, a nested loop or `while` loop would be used to hold the loop index until a successful `ACK` is registered.

### Step 4: Calculating and Displaying Network Efficiency

Finally, the script evaluates performance metrics. Link efficiency is mathematically computed as the ratio of successful unique frames delivered to the total transmission attempts made.

```python
# Calculating the efficiency
efficiency = (n_frames - n_errors) / n_transmissions
# Printing the results
print("Number of transmissions:", n_transmissions)
print("Number of errors:", n_errors)
print("Efficiency:", efficiency)

```

---

## 🚀 How to Run the Script

1. **Prerequisites:**

    This script relies completely on Python's built-in standard library, so no third-party installations (like `pip`) are necessary.

2. **Save the Code:**

    Save the full snippet into a file named `arq_simulation.py`.

3. **Execute:**
  
    Run the file directly via your terminal:

```bash
python arq_simulation.py

```
