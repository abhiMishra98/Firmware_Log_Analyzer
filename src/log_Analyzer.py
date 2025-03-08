import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Dictionary to store counts of received values
data_counts = defaultdict(int)

serialPort = serial.Serial(
    port="COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)

i = 0
while i < 10:  # Read 10 data points
    serialString = serialPort.readline()

    try:
        decoded_string = serialString.decode("ascii").strip()  # Decode and remove newlines
        print(f"Received: '{decoded_string}'")

        if decoded_string.isdigit():  # Check if it's a valid number
            value = int(decoded_string)  # Convert to integer
            data_counts[value] += 1  # Count occurrences
          

    except Exception as e:
        print(f"Error: {e}")
    i += 1  # Only increment if valid data is received
print("Final Data Counts:", dict(data_counts))  # Debugging - Show frequency of values

# If no data was received, exit
if not data_counts:
    print("Error: No valid data received over UART.")
    exit()

# Prepare data for plotting
x = list(data_counts.keys())  # Unique received values
y = list(data_counts.values())  # Their respective counts

# Plot the data
plt.figure(figsize=(8, 5))
plt.bar(x, y, width=0.8, edgecolor="black", linewidth=1)

# Label bars with counts
for j in range(len(x)):
    plt.text(x[j], y[j] + 0.1, str(y[j]), ha='center', fontsize=12, fontweight='bold')

# Axis labels and title
plt.xlabel("Received Value")
plt.ylabel("Count")
plt.title("Frequency of Received UART Values")
plt.xticks(x)  # Ensure all received values appear on x-axis
plt.show()
