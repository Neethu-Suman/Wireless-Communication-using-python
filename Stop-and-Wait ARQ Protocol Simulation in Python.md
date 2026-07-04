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

ACK received, frame 0 transmitted successfully
NAK received, retransmitting frame 1
NAK received, retransmitting frame 2
ACK received, frame 3 transmitted successfully
ACK received, frame 4 transmitted successfully
NAK received, retransmitting frame 5
ACK received, frame 6 transmitted successfully
ACK received, frame 7 transmitted successfully
ACK received, frame 8 transmitted successfully
ACK received, frame 9 transmitted successfully
ACK received, frame 10 transmitted successfully
ACK received, frame 11 transmitted successfully
ACK received, frame 12 transmitted successfully
ACK received, frame 13 transmitted successfully
ACK received, frame 14 transmitted successfully
ACK received, frame 15 transmitted successfully
ACK received, frame 16 transmitted successfully
ACK received, frame 17 transmitted successfully
ACK received, frame 18 transmitted successfully
ACK received, frame 19 transmitted successfully
ACK received, frame 20 transmitted successfully
ACK received, frame 21 transmitted successfully
ACK received, frame 22 transmitted successfully
ACK received, frame 23 transmitted successfully
ACK received, frame 24 transmitted successfully
ACK received, frame 25 transmitted successfully
ACK received, frame 26 transmitted successfully
ACK received, frame 27 transmitted successfully
ACK received, frame 28 transmitted successfully
ACK received, frame 29 transmitted successfully
NAK received, retransmitting frame 30
ACK received, frame 31 transmitted successfully
ACK received, frame 32 transmitted successfully
NAK received, retransmitting frame 33
ACK received, frame 34 transmitted successfully
ACK received, frame 35 transmitted successfully
ACK received, frame 36 transmitted successfully
ACK received, frame 37 transmitted successfully
ACK received, frame 38 transmitted successfully
ACK received, frame 39 transmitted successfully
NAK received, retransmitting frame 40
NAK received, retransmitting frame 41
ACK received, frame 42 transmitted successfully
ACK received, frame 43 transmitted successfully
ACK received, frame 44 transmitted successfully
ACK received, frame 45 transmitted successfully
ACK received, frame 46 transmitted successfully
ACK received, frame 47 transmitted successfully
ACK received, frame 48 transmitted successfully
NAK received, retransmitting frame 49
ACK received, frame 50 transmitted successfully
ACK received, frame 51 transmitted successfully
ACK received, frame 52 transmitted successfully
ACK received, frame 53 transmitted successfully
NAK received, retransmitting frame 54
ACK received, frame 55 transmitted successfully
ACK received, frame 56 transmitted successfully
ACK received, frame 57 transmitted successfully
ACK received, frame 58 transmitted successfully
ACK received, frame 59 transmitted successfully
ACK received, frame 60 transmitted successfully
ACK received, frame 61 transmitted successfully
ACK received, frame 62 transmitted successfully
ACK received, frame 63 transmitted successfully
ACK received, frame 64 transmitted successfully
ACK received, frame 65 transmitted successfully
ACK received, frame 66 transmitted successfully
NAK received, retransmitting frame 67
NAK received, retransmitting frame 68
ACK received, frame 69 transmitted successfully
ACK received, frame 70 transmitted successfully
NAK received, retransmitting frame 71
ACK received, frame 72 transmitted successfully
ACK received, frame 73 transmitted successfully
ACK received, frame 74 transmitted successfully
ACK received, frame 75 transmitted successfully
ACK received, frame 76 transmitted successfully
NAK received, retransmitting frame 77
ACK received, frame 78 transmitted successfully
ACK received, frame 79 transmitted successfully
NAK received, retransmitting frame 80
ACK received, frame 81 transmitted successfully
ACK received, frame 82 transmitted successfully
NAK received, retransmitting frame 83
ACK received, frame 84 transmitted successfully
ACK received, frame 85 transmitted successfully
NAK received, retransmitting frame 86
ACK received, frame 87 transmitted successfully
ACK received, frame 88 transmitted successfully
ACK received, frame 89 transmitted successfully
ACK received, frame 90 transmitted successfully
ACK received, frame 91 transmitted successfully
ACK received, frame 92 transmitted successfully
ACK received, frame 93 transmitted successfully
ACK received, frame 94 transmitted successfully
ACK received, frame 95 transmitted successfully
ACK received, frame 96 transmitted successfully
ACK received, frame 97 transmitted successfully
ACK received, frame 98 transmitted successfully
ACK received, frame 99 transmitted successfully
Number of transmissions: 100
Number of errors: 16
Efficiency: 0.84


## 🚀 How to Run the Script

1. **Prerequisites:**

    This script relies completely on Python's built-in standard library, so no third-party installations (like `pip`) are necessary.

2. **Save the Code:**

    Save the full snippet into a file named

   `arq_simulation.py`.

4. **Execute:**
  
    Run the file directly via your terminal:

```bash
python arq_simulation.py

```
