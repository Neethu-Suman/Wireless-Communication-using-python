# Available wireless protocols
IOT_PROTOCOLS = ["Wi-Fi", "Bluetooth", "Zigbee", "LoRaWAN", "NFC"]

# Function to simulate communication between devices
def simulate_communication(protocol):
    if protocol not in IOT_PROTOCOLS:
        print(f"{protocol} is not a valid wireless protocol.")
        return
    print(f"Simulating communication using {protocol}...")
    print("Data sent: Hello World!")
    print("Data received: Hello World!")
    print()

# Example usage of the function
simulate_communication("Wi-Fi")
simulate_communication("Bluetooth")
simulate_communication("Zigbee")
simulate_communication("LoRaWAN")
simulate_communication("NFC")
simulate_communication("InvalidProtocol")
