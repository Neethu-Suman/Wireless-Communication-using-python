# Quadrature Phase Shift Keying (QPSK) Simulation in Python

This repository contains a Python script that simulates Quadrature Phase Shift Keying (QPSK) modulation and demodulation. QPSK is a digital modulation scheme that conveys data by changing (modulating) the phase of a reference signal (the carrier wave).

# 📖 Step-by-Step Code Explanation

## Step 1: Importing Dependencies

The script relies on numpy for handling arrays and mathematical computations (like sine, cosine, and phase extraction) and matplotlib.pyplot for visual plotting.

    import numpy as np
    import matplotlib.pyplot as plt

## Step 2: Defining the Message Signal

The input data is a stream of digital binary data ($0$s and $1$s). In this example, we have an 8-bit message.

        #Define the message signal
        message = [1, 0, 1, 0, 1, 1, 0, 1]

## Step 3: Setting Modulation Constants

We define the phase variables. In a standard QPSK constellation, bits map onto specific phase quadrants separated by angles of $\frac{\pi}{4}$ ($45^\circ$).

        #Constants for QPSK modulation
        pi = np.pi
        mod_index = pi / 4

## Step 4: QPSK Modulation (Encoding)

The script maps each bit into a complex exponential phasor using Euler's relation ($e^{j\theta} = \cos\theta + j\sin\theta$). This shifts the signal phase based on the bit value ($0$ or $1$) combined with its position index.

        #Generate the QPSK modulated signal
        qpsk_signal = np.array([np.cos(mod_index*i + pi*message[i]) + 1j*np.sin(mod_index*i + pi*message[i]) for i in range(len(message))])

## Step 5: QPSK Demodulation (Decoding)

To reverse the modulation, the demodulator analyzes the phase of each complex point in qpsk_signal. By extracting the mathematical angle of each coordinate (np.angle) and tracking out the index-based phase rotation offset (mod_index * i), we can accurately rebuild the original binary stream.

        #Demodulation of the QPSK signal to recover original bits
        demodulated_message = []
        for i in range(len(qpsk_signal)):
            # Extract the total phase angle of the received complex signal
            received_phase = np.angle(qpsk_signal[i])
            
            # Subtract the index shift to isolate the phase introduced by the message bit
            base_phase = received_phase - (mod_index * i)
            
            # Normalize the phase to be within [-pi, pi]
            base_phase = (base_phase + pi) % (2 * pi) - pi
            
            # If the phase is close to pi or -pi, the bit was 1; if close to 0, the bit was 0
            if np.abs(base_phase) > pi / 2:
                demodulated_message.append(1)
            else:
                demodulated_message.append(0)
        
        print("Original Message:   ", message)
        print("Demodulated Message:", demodulated_message)

Step 6: Plotting the Constellation Diagram
Finally, the script plots the complex QPSK points onto a 2D grid where the X-axis is the In-phase (Real) component and the Y-axis is the Quadrature (Imaginary) component.
Python
# Plot the modulated signal (Constellation Diagram)
plt.figure(figsize=(6, 6))
plt.scatter(qpsk_signal.real, qpsk_signal.imag, color='red', marker='o', s=100, label='QPSK Symbols')

# Labeling coordinates for clarity
for i, txt in enumerate(message):
    plt.annotate(f"Bit {txt} (i={i})", (qpsk_signal.real[i]+0.05, qpsk_signal.imag[i]+0.05))

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('Real (In-phase)')
plt.ylabel('Imaginary (Quadrature)')
plt.title('QPSK Constellation Diagram & Demodulation Mapping')
plt.legend()
plt.show()
🚀 How to Run the Script
1.	Install Requirements:
Bash
pip install numpy matplotlib
2.	Save the Code: Copy the steps above into a single file named qpsk_simulation.py.
3.	Execute:
Bash
python qpsk_simulation.py

