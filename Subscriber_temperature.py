import time
import datetime as dt
import matplotlib.pyplot as plt
import paho.mqtt.subscribe as subscribe

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102
msg = subscribe.simple("TEMP", hostname="127.0.0.1")

# Sample temperature every second for 10 seconds
for t in range(0, 10):

    # Read temperature (Celsius) from TMP102
    temp_c = msg.payload
    msg = subscribe.simple("TEMP", hostname="127.0.0.1")
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Wait 1 second before sampling temperature again
    time.sleep(1)

# Draw plot
ax.plot(xs, ys)

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('TMP102 Temperature over Time')
plt.ylabel('Temperature (deg C)')

# Draw the graph
plt.show()

