import random
import math
import csv
import matplotlib.pyplot as plt

random.seed(42)

readings = []

for i in range(1, 31):
    temperature = round(
        27.0 + 0.08 * i + 0.8 * math.sin(i / 3) + random.uniform(-0.35, 0.35), 2
    )
    humidity = round(
        68.0 - 0.12 * i + 3.0 * math.cos(i / 4) + random.uniform(-1.2, 1.2), 2
    )
    readings.append((i, temperature, humidity))

# Save simulated sensor data to CSV
with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading", "Temperature_C", "Humidity_percent"])
    writer.writerows(readings)

# Visualize the simulated sensor data
reading_no = [row[0] for row in readings]
temperature = [row[1] for row in readings]
humidity = [row[2] for row in readings]

plt.figure(figsize=(10, 5))
plt.plot(reading_no, temperature, marker="o", label="Temperature (°C)")
plt.plot(reading_no, humidity, marker="s", label="Humidity (%)")
plt.xlabel("Reading Number")
plt.ylabel("Sensor Value")
plt.title("IoT Sensor Data Simulation")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("sensor_plot.png", dpi=200)
plt.show()
