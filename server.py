import socket
import struct
import matplotlib.pyplot as plt

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Acceleration')
ax.set_ylim([-32768, 32767])

# Set up the server
server_address = '192.168.1.248'
server_port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

# Initialize the data arrays
times = []
xs = []
ys = []
zs = []

# Start receiving sensor data and updating the plot
i = 0
while True:
    # Receive sensor data
    data, address = server_socket.recvfrom(1024)
    ax1, ay, az = struct.unpack('hhh', data)
    print('Received data: ax={}, ay={}, az={}'.format(ax1, ay, az))

    # Add the new data to the arrays
    times.append(i)
    xs.append(ax1)
    ys.append(ay)
    zs.append(az)
    
    # Plot the data every 10 iterations
    if i % 10 == 0:
        ax.clear()
        ax.set_xlabel('Time')
        ax.set_ylabel('Acceleration')
        ax.set_ylim([-32768, 32767])
        ax.plot(times, xs, 'r-', label='X')
        ax.plot(times, ys, 'g-', label='Y')
        ax.plot(times, zs, 'b-', label='Z')
        ax.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)
    i = i + 1

# Show the final plot
ax.clear()
ax.set_xlabel('Time')
ax.set_ylabel('Acceleration')
ax.set_ylim([-32768, 32767])
ax.plot(times, xs, 'r-', label='X')
ax.plot(times, ys, 'g-', label='Y')
ax.plot(times, zs, 'b-', label='Z')
ax.legend(loc='upper left')
plt.show()
