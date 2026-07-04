import random

# Number of frames to be transmitted
n_frames = 100
# Probability of error in the channel
p_error = 0.1
# Initializing counters
n_transmissions = 0
n_errors = 0

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

# Calculating the efficiency
efficiency = (n_frames - n_errors) / n_transmissions
# Printing the results
print("Number of transmissions:", n_transmissions)
print("Number of errors:", n_errors)
print("Efficiency:", efficiency)
