import matplotlib.pyplot as plt
import numpy as np


# Set up the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Data')
ax.set_ylim([-50000, 50000])

# Set up the plot for acceleration data only
fig2, ax2 = plt.subplots()
ax2.set_xlabel('Time')
ax2.set_ylabel('Acceleration')
ax2.set_ylim([-32768, 32767])

times = []
axs = []
ays = []
azs = []
gxs = []
gys = []
gzs = []

i = 0

def on_save(event,times,axs,ays,azs,gxs,gys,gzs):
    fig.savefig('D:/Product_design/Fall-detection-device/figure.png')
    fig2.savefig('D:/Product_design/Fall-detection-device/figure2.png')
    time = np.array(times)
    axs_np = np.array(axs)
    data = np.vstack((time, axs_np))
    np.save('data.npy', data)
    

# Add a save button to the figure
save_button_ax = plt.axes([0.85, 0.05, 0.1, 0.075])
save_button = plt.Button(save_button_ax, 'Save')
save_button.on_clicked(lambda event: on_save(event, times, axs, ays, azs, gxs, gys, gzs))


while True:
    times.append(i)
    axs.append(i)
    ays.append(i**2)
    azs.append(2*i)
    gxs.append(3*i)
    gys.append(4*i)
    gzs.append(i**3)

    if len(times) > 500:
        times = times[-500:]
        axs = axs[-500:]
        ays = ays[-500:]
        azs = azs[-500:]
        gxs = gxs[-500:]
        gys = gys[-500:]
        gzs = gzs[-500:]
    
    if i % 30 == 0:
        ax.clear()
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyro')
        ax.set_ylim([-32768, 32767])
        ax.plot(times[-500:], gxs[-500:], 'r-', label='Gyro X')
        ax.plot(times[-500:], gys[-500:], 'g-', label='Gyro Y')
        ax.plot(times[-500:], gzs[-500:], 'b-', label='Gyro Z')
        ax.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)

        ax2.clear()
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Acceleration')
        ax2.set_ylim([-32768, 32767])
        ax2.plot(times[-500:], axs[-500:], 'r-', label='Accel X')
        ax2.plot(times[-500:], ays[-500:], 'g-', label='Accel Y')
        ax2.plot(times[-500:], azs[-500:], 'b-', label='Accel Z')
        ax2.legend(loc='upper left')
        plt.show(block=False)
        plt.pause(0.001)
    i = i + 1