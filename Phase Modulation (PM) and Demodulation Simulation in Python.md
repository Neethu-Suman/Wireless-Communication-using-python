# Phase Modulation (PM) and Demodulation Simulation in Python

This contains a Python script that simulates Phase Modulation (PM) and its subsequent coherent demodulation using complex numbers in NumPy, with visualization provided by Matplotlib.

# 📖 Step-by-Step Code Explanation

## Step 1: Importing Dependencies

The script begins by importing the core libraries needed for numerical operations and plotting.

    import numpy as np
    import matplotlib.pyplot as plt

## Step 2: Defining the Carrier Signal

The carrier signal is the high-frequency wave ($10\text{ Hz}$) that will have its phase altered to carry the underlying data.

    #Defining the carrier signal
    carrier_freq = 10 # carrier signal frequency
    carrier_amp = 1 # carrier signal amplitude
    carrier_phase = 0 # carrier signal phase
    carrier_time = np.linspace(0, 1, 1000) # carrier signal time
    carrier_signal = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)

## Step 3: Defining the Message Signal

The message signal represents our actual data or audio track. It uses a much lower frequency ($2\text{ Hz}$).Python# Defining the message signal

    message_freq = 2 # message signal frequency
    message_amp = 1 # message signal amplitude
    message_time = np.linspace(0, 1, 1000) # message signal time
    message_signal = message_amp*np.cos(2*np.pi*message_freq*message_time)

## Step 4: Setting the Modulation Index

The modulation index ($\beta = 0.5$) determines how intensely the message signal shifts the phase of the carrier signal.Python

    #Generating the phase modulation index
    modulation_index = 0.5
    pm_index = modulation_index*message_signal

## Step 5: Generating the Modulated Signal

This step attempts to apply phase modulation by scaling the phase index into a complex exponential phasor and multiplying it by the carrier signal.

    #Generating the modulated signal
    pm_signal = carrier_signal*np.exp(1j*pm_index)

💡 Technical Note: In traditional analog communications, a Phase Modulated wave is entirely real-valued, mathematically expressed as $A_c \cos(2\pi f_c t + \beta m(t))$. Because this code multiplies a real cosine by a complex exponential ($e^{j\beta m(t)}$), pm_signal becomes a complex array.

## Step 6: Coherent Demodulation

To extract the message back out, the script sets up a local oscillator perfectly synchronized with the original carrier wave. It multiplies the modulated complex signal by the complex conjugate of the local oscillator and extracts the real part.

    #Demodulation of the PM signal using coherent demodulation
    local_oscillator = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)
    demodulated_signal = np.real(pm_signal*np.conj(local_oscillator))

## Step 7: Plotting the Results

Finally, the script plots the real part of the modulated PM signal alongside the recovered demodulated signal to visualize the system performance.

    #Plotting the modulated and demodulated signal
    plt.plot(carrier_time, np.real(pm_signal), label='Modulated signal')
    plt.plot(carrier_time, demodulated_signal, label='Demodulated signal')
    plt.legend()
    plt.show()

# 🚀 How to Run the Script

## 1.	Install Requirements:

    pip install numpy matplotlib

## 2.	Save the Code: 

Save the script to a file named pm_simulation.py.

## 3.	Execute:

    python pm_simulation.py

