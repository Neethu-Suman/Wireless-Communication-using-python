# Amplitude Modulation (AM) and Demodulation Simulation in Python

This contains a Python script that simulates the generation, modulation, and demodulation of an analog signal using NumPy for mathematical computations and Matplotlib for visualization.

# 📖 Step-by-Step Code Explanation

## Step 1: Importing Dependencies

The script begins by importing the necessary libraries. numpy handles the array generation and trigonometric math, while matplotlib.pyplot handles the visual plotting.

    import numpy as np
    import matplotlib.pyplot as plt

## Step 2: Defining the Carrier Signal

The carrier signal is the high-frequency wave used to "carry" the information through space. Here, we define its parameters (frequency = $10\text{ Hz}$, amplitude = $1$)  and create a time vector spanning from $0$ to $1$ second with $1000$ sample points.

    #Defining the carrier signal
    carrier_freq = 10 # carrier signal frequency
    carrier_amp = 1 # carrier signal amplitude
    carrier_phase = 0 # carrier signal phase
    carrier_time = np.linspace(0, 1, 1000) # carrier signal time
    carrier_signal = carrier_amp*np.cos(2*np.pi*carrier_freq*carrier_time + carrier_phase)

## Step 3: Defining the Message Signal

The message signal (or modulating signal) represents the actual data or audio we want to transmit. It has a much lower frequency ($2\text{ Hz}$) compared to the carrier wave.

    #Defining the message signal
    message_freq = 2 # message signal frequency
    message_amp = 1 # message signal amplitude
    message_phase = 0 # message signal phase
    message_time = np.linspace(0, 1, 1000) # message signal time
    message_signal = message_amp*np.cos(2*np.pi*message_freq*message_time + message_phase)

## Step 4: Signal Modulation (DSB-SC)

To modulate the signal, the script multiplies the carrier wave by the message wave point-by-point. Because no DC offset is added to the message, this results in Double-Sideband Suppressed-Carrier (DSB-SC) 
modulation.

    #Multiplying the carrier signal and the message signal to generate AM signal
    am_signal = carrier_signal*message_signal

## Step 5: Demodulation Process

Demodulation is the process of extracting the original message from the modulated wave.

np.abs(am_signal) acts as a full-wave rectifier (turning all negative peaks positive).

Multiplying this rectified signal by a coherent cosmic wave attempts to shift the frequencies back to the baseband.

    #Demodulation of the AM signal to obtain the original message signal
    envelope_detector = np.abs(am_signal) # Using the absolute value of the AM signal
    demodulated_signal = envelope_detector*np.cos(2*np.pi*message_freq*message_time + message_phase)

⚠️ Note on Output: In a perfect hardware/software implementation, a Low-Pass Filter (LPF) is required right after this step to smooth out the high-frequency ripples and isolate the pure $2\text{ Hz}$ message 
wave.Step 6: Plotting the ResultsFinally, the script overlays the modulated waveform and the resulting demodulated waveform on a single graph to visually evaluate the system.

    #Plotting the modulated and demodulated signal
    plt.plot(carrier_time, am_signal, label='Modulated signal')
    plt.plot(carrier_time, demodulated_signal, label='Demodulated signal')
    plt.legend()
    plt.show()

🚀 How to Run the Script
Install Requirements:

    pip install numpy matplotlib
    
Save the Code: Save the full script as am_simulation.py.

Execute:

    python am_simulation.py
