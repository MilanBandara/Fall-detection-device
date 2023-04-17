import socket
import struct
import matplotlib.pyplot as plt

# Set up the acceleration and gyro plots
fig_accel_gyro, axs_accel_gyro = plt.subplots()
axs_accel_gyro.set_xlabel('Time')
axs_accel_gyro.set_ylabel('Data')
axs_accel_gyro.set_ylim([-32768, 32767])

# Set up the acceleration plot
fig_accel, axs_accel = plt.subplots()
axs_accel.set_xlabel('Time')
axs_accel.set_ylabel('Data')
axs_accel.set_ylim([-32768, 32767])

# Set up the gyro plot
fig_gyro, axs_gyro = plt.subplots()
axs_gyro.set_xlabel('Time')
axs_gyro.set_ylabel('Data')
axs_gyro.set_ylim([-32768, 32767])

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
    
    # Plot the data every 10 iterations
    if i % 10 == 0:
        # Update the acceleration and gyro plot
        axs_accel_gyro.clear()
        axs_accel_gyro.set_xlabel('Time')
        axs_accel_gyro.set_ylabel('Data')
        axs_accel_gyro.set_ylim([-32768, 32767])
        axs_accel_gyro.plot(times, axs, 'r-', label='Accel X')
        axs_accel_gyro.plot(times, ays, 'g-', label='Accel Y')
        axs_accel_gyro.plot(times, azs, 'b-', label='Accel Z')
        axs_accel_gyro.plot(times, gxs, 'c-', label='Gyro X')
        axs_accel_gyro.plot(times, gys, 'm-', label='Gyro Y')
        axs_accel_gyro.plot(times, gzs, 'y-', label='Gyro Z')
        axs_accel_gyro.legend(loc='upper left')
        fig_accel_gyro.show()

        # Update the acceleration plot
        axs_accel.clear()
        axs_accel.set_xlabel('Time')
        axs_accel.set_ylabel('Data')
        axs_accel.set_ylim([-32768, 32767])
        axs_accel.plot(times, axs, 'r-', label='Accel X')
        axs_accel.plot(times, ays, 'g-', label='Accel Y')
        axs_accel.plot(times, azs, 'b-', label='Accel Z')
        axs_accel.legend(loc='upper left')
        fig_accel.show()

        # Update the gyro plot
        axs_gyro.clear()
        axs_gyro
