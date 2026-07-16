# IoT Wireless Protocol Communication Simulation

This repository contains a basic Python script that demonstrates array membership validation and functional simulation of different **Internet of Things (IoT)** wireless communication protocols.

## 📌 Project Overview

In IoT ecosystems, devices rely on distinct wireless standards depending on their range, power, and data throughput requirements. This script sets up a validation check and provides a unified wrapper to simulate data exchanges using:

* **Wi-Fi:** High throughput, high power consumption.
* **Bluetooth:** Short-range, low power (often for personal devices).
* **Zigbee:** Low-power, low-data-rate mesh networking (often for smart homes).
* **LoRaWAN:** Long-range, low-power wide-area networking (often for smart cities/agriculture).
* **NFC:** Near-field, ultra-short-range touch interactions.

---

## 📖 Step-by-Step Code Explanation

### Step 1: Defining the Protocol Pool

The script establishes a global constant list named `IOT_PROTOCOLS`. This serves as the master checklist of allowed or supported wireless options within our simulation.

```python
# Available wireless protocols
IOT_PROTOCOLS = ["Wi-Fi", "Bluetooth", "Zigbee", "LoRaWAN", "NFC"]

```

### Step 2: Creating the Simulation Function & Membership Validation

The function `simulate_communication` is declared, accepting a single string argument (`protocol`). The first operational step checks if the requested string is missing from the global list using the `not in` operator. If it's invalid, the code prints an error warning and terminates execution via a early `return`.

```python
# Function to simulate communication between devices
def simulate_communication(protocol):
    if protocol not in IOT_PROTOCOLS:
        print(f"{protocol} is not a valid wireless protocol.")
        return

```

### Step 3: Mocking the Data Transfer

If the validation passes, the function proceeds to simulate a bidirectional "Hello World!" message loop, logging the transmission and receipt states directly to the terminal.

```python
    print(f"Simulating communication using {protocol}...")
    print("Data sent: Hello World!")
    print("Data received: Hello World!")
    print()

```

### Step 4: Executing the Function Calls

Finally, the script tests its execution paths. It successfully loops through the five supported protocols before intentionally invoking `"InvalidProtocol"` to verify that the conditional error handler functions as intended.

```python
# Example usage of the function
simulate_communication("Wi-Fi")
simulate_communication("Bluetooth")
simulate_communication("Zigbee")
simulate_communication("LoRaWAN")
simulate_communication("NFC")
simulate_communication("InvalidProtocol")

```

---

## 🚀 How to Run the Script

1. **Prerequisites:** This script relies exclusively on Python's native functional structures, so no external framework installations (like `pip`) are needed.
2. **Save the Code:** Copy the full script into a file named `iot_simulation.py`.
3. **Execute:** Run the file directly via your terminal window:
```bash
python iot_simulation.py

```
