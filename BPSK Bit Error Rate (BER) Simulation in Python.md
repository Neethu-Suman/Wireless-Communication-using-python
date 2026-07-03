# BPSK Bit Error Rate (BER) Simulation in Python

This contains a Python script that simulates the Bit Error Rate (BER) performance of a Binary Phase Shift Keying (BPSK) modulation scheme over an Additive White Gaussian Noise (AWGN) channel. It compares empirical performance across a range of Signal-to-Noise Ratios (SNR).

# 📖 Step-by-Step Code Explanation

## Step 1: Importing Dependencies

The script begins by importing numpy for efficient array computations and random number generation, alongside matplotlib.pyplot for creating logarithmic performance plots.

        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.stats import norm

Note: While scipy.stats.norm is imported, it is not explicitly used in this basic script. It is commonly included to plot the theoretical BER curve ($$\frac{1}{2}\text{erfc}(\sqrt{\text{SNR}})$$)  for comparison.

## Step 2: Defining the Simulation Parameters

We set up a simulation environment using 1 million bits to guarantee statistical accuracy. The Signal-to-Noise Ratio (SNR) is defined in decibels ($\text{dB}$) ranging from $0$ to $20\text{ dB}$, and then converted to a linear scale using the formula:

$$\text{SNR}_{\text{linear}} = 10^{\frac{\text{SNR}_{\text{dB}}}{10}}$$

        #Defining the parameters
        num_bits = int(1e6) # number of bits to simulate
        snr_db = np.linspace(0, 20, 21) # range of snr in dB
        snr = np.power(10, snr_db / 10) # converting snr from dB to linear scale

## Step 3: Generating and Modulating Data

The input data stream is created by generating a large random array of binary $0$s and $1$s. It is then modulated using BPSK, mapping a bit of 0 to a value of -1 and a bit of 1 to a value of +1.

        #Generating the data
        data = np.random.randint(2, size=num_bits) # generating random binary data
        #Modulation
        modulated_data = 2*data - 1 # BPSK modulation

## Step 4: Iterating Through SNR and Adding AWGN Noise

An empty array is initialized to store our calculated errors. The script loops through each SNR level, calculating the required noise variance ($\sigma^2 = \frac{1}{2\cdot\text{SNR}}$). It then generates a zero-mean Gaussian distribution matching that variance and adds it to our modulated signal to simulate channel interference.

        ber = np.zeros(len(snr)) # Initializing the bit error rate array
        #Loop over different snr values
        for i in range(len(snr)):
            # Adding noise
            noise = np.sqrt(1 / (2 * snr[i])) * np.random.randn(num_bits) # generating gaussian noise
            received_signal = modulated_data + noise # adding noise to the modulated signal

## Step 5: Demodulation (Decision Boundary)

Because the original transmitted points were centered on a zero axis (-1 and +1), the receiver uses $0$ as a hard threshold boundary. If the received_signal value is greater than $0$, it decodes it as a binary 1; otherwise, it maps it as a 0.

        #Demodulation
        demodulated_data = (received_signal > 0)*1 # demodulating

## Step 6: Calculating Bit Error Rate (BER)

At each SNR increment, the script counts how many decoded bits do not match the original transmitted data stream (data != demodulated_data). Dividing this total count by the total number of simulated bits (num_bits) gives the precise statistical probability of error.

    #Calculating the bit error rate
    ber[i] = np.sum(data != demodulated_data) / num_bits

## Step 7: Plotting Performance Curves

Finally, the data is plotted on a logarithmic vertical axis using plt.semilogy. A log scale is standard in communication systems because bit error rates quickly drop by factors of $10$ as signal strength increases.

        #Plotting the BER
        plt.semilogy(snr_db, ber, 'bo-')
        plt.xlabel('SNR (dB)')
        plt.ylabel('Bit Error Rate')
        plt.title('BER for BPSK')
        plt.grid()
        plt.show()

# 🚀 How to Run the Script

## 1.	Install Requirements:
        
        pip install numpy matplotlib scipy

## 2.	Save the Code: Save the full script as bpsk_ber_simulation.py.

## 3.	Execute:

        python bpsk_ber_simulation.py

