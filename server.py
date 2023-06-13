import socket
import struct
import matplotlib.pyplot as plt
import numpy as np
import time

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Data')

# ax.set_ylim([-50000, 50000])

# Set up the plot for acceleration data only
fig2, ax2 = plt.subplots()
ax2.set_xlabel('Time')
ax2.set_ylabel('Acceleration')

# ax2.set_ylim([-32768, 32767])

# fig3, ax3 = plt.subplots()
# ax3.set_xlabel('Time')
# ax3.set_ylabel('Acceleration_rate')

# fig4, ax4 = plt.subplots()
# ax4.set_xlabel('Time')
# ax4.set_ylabel('Acceleration_rate')

# Set up the server
# server_address = '192.168.1.248'
server_address = '192.168.43.200'
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

def on_save(event,times,axs,ays,azs,gxs,gys,gzs):
    reading = "3"
    # "D:\Product_design\Fall-detection-device\Data_2\Right\Tharindi"
    fig.savefig('D:/Product_design/Fall-detection-device/Data_2/Chair_Fall/gyro'+reading+'.png')
    fig2.savefig('D:/Product_design/Fall-detection-device/Data_2/Chair_Fall/acceleration'+reading+'.png')
    time = np.array(times)
    axs_np = np.array(axs)
    ays_np = np.array(ays)
    azs_np = np.array(azs)
    gxs_np = np.array(gxs)
    gys_np = np.array(gys)
    gzs_np = np.array(gzs)
    data = np.vstack((time, axs_np,ays_np,azs_np,gxs_np,gys_np,gzs_np))
    print((data.shape))
    np.save('D:/Product_design/Fall-detection-device/Data_2/Chair_Fall/data'+reading+'.npy', data)

# Add a save button to the figure
save_button_ax = plt.axes([0.85, 0.05, 0.1, 0.075])
save_button = plt.Button(save_button_ax, 'Save')
save_button.on_clicked(lambda event: on_save(event, times, axs, ays, azs, gxs, gys, gzs))



while True:
    # Receive sensor data
    data, address = server_socket.recvfrom(1024)
    ax1, ay, az, gx, gy, gz = struct.unpack('hhhhhh', data)
    # print('Received data: ax={}, ay={}, az={}, gx={}, gy={}, gz={}'.format(ax1, ay, az, gx, gy, gz))

    # Add the new data to the arrays
    
    times.append(i)
    axs.append(ax1)
    ays.append(ay)
    azs.append(az)
    gxs.append(gx)
    gys.append(gy)
    gzs.append(gz)

    # Check if the data arrays have more than 500 points
    if len(times) > 1000:
        times = times[-1000:]
        axs = axs[-1000:]
        ays = ays[-1000:]
        azs = azs[-1000:]
        gxs = gxs[-1000:]
        gys = gys[-1000:]
        gzs = gzs[-1000:]
    
    
    ax_diff = np.diff(axs)
    ay_diff = np.diff(ays)
    az_diff = np.diff(azs)
    gx_diff = np.diff(gxs)
    gy_diff = np.diff(gys)
    gz_diff = np.diff(gzs)

    time_diff = np.arange(ax_diff.shape[0])

    # Plot the data every 10 iterations
    if i % 30 == 0:
        # ax.clear()
        # ax.set_xlabel('Time')
        # ax.set_ylabel('Data')
        # ax.set_ylim([-32768, 32767])
        # ax.plot(times, axs, 'r-', label='Accel X')
        # ax.plot(times, ays, 'g-', label='Accel Y')
        # ax.plot(times, azs, 'b-', label='Accel Z')
        # ax.plot(times, gxs, 'c-', label='Gyro X')
        # ax.plot(times, gys, 'm-', label='Gyro Y')
        # ax.plot(times, gzs, 'y-', label='Gyro Z')
        # ax.legend(loc='upper left')
        # plt.show(block=False)
        # plt.pause(0.001)


        #Gyro plot
        ax.clear()
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyro')
        ax.set_ylim([-32768, 32767])
        ax.plot(times[-1000:], gxs[-1000:], 'r-', label='Gyro X')
        ax.plot(times[-1000:], gys[-1000:], 'g-', label='Gyro Y')
        ax.plot(times[-1000:], gzs[-1000:], 'b-', label='Gyro Z')
        ax.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)


        # Acc plot
        ax2.clear()
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Acceleration')
        ax2.set_ylim([-32768, 32767])
        ax2.plot(times[-1000:], axs[-1000:], 'r-', label='Accel X')
        ax2.plot(times[-1000:], ays[-1000:], 'g-', label='Accel Y')
        ax2.plot(times[-1000:], azs[-1000:], 'b-', label='Accel Z')
        ax2.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)

        # Acceleration rate of change
        # ax3.clear()
        # ax3.set_xlabel('Time')
        # ax3.set_ylabel('acc rate')
        # ax3.set_ylim([-32768, 32767])
        # ax3.plot(time_diff, ax_diff, 'r-', label='Acc x rate')
        # ax3.plot(time_diff, ay_diff, 'g-', label='Acc y rate')
        # ax3.plot(time_diff, az_diff, 'b-', label='Acc z rate')
        # ax3.legend(loc='upper left')
        # plt.show(block=False)
        # plt.pause(0.001)

        # Gyro rate of change
        # ax4.clear()
        # ax4.set_xlabel('Time')
        # ax4.set_ylabel('acc rate')
        # ax4.set_ylim([-32768, 32767])
        # ax4.plot(time_diff, gx_diff, 'r-', label='Acc x rate')
        # ax4.plot(time_diff, gy_diff, 'g-', label='Acc y rate')
        # ax4.plot(time_diff, gz_diff, 'b-', label='Acc z rate')
        # ax4.legend(loc='upper left')
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