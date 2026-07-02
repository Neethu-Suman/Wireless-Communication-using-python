# ==========================================
# Step 1: Importing Dependencies
# ==========================================
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Step 2: Defining the Message Signal
# ==========================================
message = [1, 0, 1, 0, 1, 1, 0, 1]

# Step 3: Setting Modulation Constants
pi = np.pi
mod_index = pi / 4

# ==========================================
# Step 4: QPSK Modulation (Encoding)
# ==========================================
qpsk_signal = np.array([
    np.cos(mod_index * i + pi * message[i]) + 1j * np.sin(mod_index * i + pi * message[i]) 
    for i in range(len(message))
])

# ==========================================
# Step 5: QPSK Demodulation (Decoding)
# ==========================================
demodulated_message = []
for i in range(len(qpsk_signal)):
    # Extract the total phase angle of the received complex signal
    received_phase = np.angle(qpsk_signal[i])
    
    # Subtract the index shift to isolate the phase introduced by the message bit
    base_phase = received_phase - (mod_index * i)
    
    # Normalize the phase to be within [-pi, pi]
    base_phase = (base_phase + pi) % (2 * pi) - pi
    
    # Deciding bit value based on normalized phase
    if np.abs(base_phase) > pi / 2:
        demodulated_message.append(1)
    else:
        demodulated_message.append(0)

print("Original Message:   ", message)
print("Demodulated Message:", demodulated_message)

# ==========================================
# Step 6: Plotting the Constellation Diagram
# ==========================================
plt.figure(figsize=(6, 6))
plt.scatter(qpsk_signal.real, qpsk_signal.imag, color='red', marker='o', s=100, label='QPSK Symbols')

# Labeling coordinates with their corresponding bits
for i, txt in enumerate(message):
    plt.annotate(f"Bit {txt} (i={i})", (qpsk_signal.real[i] + 0.05, qpsk_signal.imag[i] + 0.05))

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
