import socket
import struct
import matplotlib.pyplot as plt

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Data')
ax.set_ylim([-32768, 32767])

# Set up the plot for acceleration data only
fig2, ax2 = plt.subplots()
ax2.set_xlabel('Time')
ax2.set_ylabel('Acceleration')
ax2.set_ylim([-32768, 32767])

# Set up the server
server_address = '192.168.1.248'
server_port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

# Initialize the data arrays
times = []
axs = []
ays = []
azs = []
gxs = []
gys = []
gzs = []

# Start receiving sensor data and updating the plot
i = 0
while True:
    # Receive sensor data
    data, address = server_socket.recvfrom(1024)
    ax1, ay, az, gx, gy, gz = struct.unpack('hhhhhh', data)
    print('Received data: ax={}, ay={}, az={}, gx={}, gy={}, gz={}'.format(ax1, ay, az, gx, gy, gz))

    # Add the new data to the arrays
    
    times.append(i)
    axs.append(ax1)
    ays.append(ay)
    azs.append(az)
    gxs.append(gx)
    gys.append(gy)
    gzs.append(gz)

    # Check if the data arrays have more than 500 points
    if len(times) > 500:
        times = times[-500:]
        axs = axs[-500:]
        ays = ays[-500:]
        azs = azs[-500:]
        gxs = gxs[-500:]
        gys = gys[-500:]
        gzs = gzs[-500:]
    
    # Plot the data every 10 iterations
    if i % 20 == 0:
        ax.clear()
        ax.set_xlabel('Time')
        ax.set_ylabel('Data')
        ax.set_ylim([-32768, 32767])
        ax.plot(times, axs, 'r-', label='Accel X')
        ax.plot(times, ays, 'g-', label='Accel Y')
        ax.plot(times, azs, 'b-', label='Accel Z')
        ax.plot(times, gxs, 'c-', label='Gyro X')
        ax.plot(times, gys, 'm-', label='Gyro Y')
        ax.plot(times, gzs, 'y-', label='Gyro Z')
        ax.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)

        # ax2.clear()
        # ax2.set_xlabel('Time')
        # ax2.set_ylabel('Acceleration')
        # ax2.set_ylim([-32768, 32767])
        # ax2.plot(times[-500:], axs[-500:], 'r-', label='Accel X')
        # ax2.plot(times[-500:], ays[-500:], 'g-', label='Accel Y')
        # ax2.plot(times[-500:], azs[-500:], 'b-', label='Accel Z')
        # ax2.legend(loc='upper left')
        # plt.show(block=False)
        # plt.pause(0.001)
    i = i + 1

# Show the final plot
ax.clear()
ax.set_xlabel('Time')
ax.set_ylabel('Data')
ax.set_ylim([-32768, 32767])
ax.plot(times, axs, 'r-', label='Accel X')
ax.plot(times, ays, 'g-', label='Accel Y')
ax.plot(times, azs, 'b-', label='Accel Z')
ax.plot(times, gxs, 'c-', label='Gyro X')
ax.plot(times, gys, 'm-', label='Gyro Y')
ax.plot(times, gzs, 'y-', label='Gyro Z')
ax.legend(loc='upper left')
plt.show()
