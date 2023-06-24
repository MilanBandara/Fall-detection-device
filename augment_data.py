import numpy as np
import os
import matplotlib.pyplot as plt


def time_shift_left(shift):
    fall_folder_path = "D:/Product_design/Fall-detection-device/training_data"
    fall_files = os.listdir(fall_folder_path)
    length = len(fall_files)

    for i in range(1,len(fall_files)+1):
        #skip the data with wrong shape
        shifted_time = shift
        data = np.load('D:/Product_design/Fall-detection-device/training_data/data'+str(i)+".npy")
        selected = data[1:,shifted_time:]
        selected2 = data[1:,(1000-shifted_time):]
        data[1:,0:(1000-shifted_time)] = selected
        data[1:,(1000-shifted_time):] = selected2
        np.save('D:/Product_design/Fall-detection-device/Augmented_data/data'+str(i)+'.npy', data)
def time_shift_right(shift):
    #complete this
    fall_folder_path = "D:/Product_design/Fall-detection-device/training_data"
    fall_files = os.listdir(fall_folder_path)
    length = len(fall_files)

    for i in range(1,len(fall_files)+1):
        #skip the data with wrong shape
        shifted_time = shift
        data = np.load('D:/Product_design/Fall-detection-device/training_data/data'+str(i)+".npy")
        selected = data[1:,shifted_time:]
        selected2 = data[1:,(1000-shifted_time):]
        data[1:,0:(1000-shifted_time)] = selected
        data[1:,(1000-shifted_time):] = selected2
        np.save('D:/Product_design/Fall-detection-device/Augmented_data/data'+str(i)+'.npy', data)
        
time_shift_left(200)

data1 = np.load('D:/Product_design/Fall-detection-device/training_data/data4.npy')[1:,:]
data2 = np.load('D:/Product_design/Fall-detection-device/Augmented_data/data4.npy')[1:,:]
time = np.arange(0,1000,1)
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

ax.set_xlabel('Time')
ax.set_ylabel('Data')
ax.plot(time, data1[3], 'r-', label='Acc X')
ax.plot(time, data1[4], 'g-', label='Acc Y')
ax.plot(time, data1[5], 'b-', label='Acc Z')

ax2.set_xlabel('Time')
ax2.set_ylabel('Data')
ax2.plot(time, data2[3], 'r-', label='Acc X')
ax2.plot(time, data2[4], 'g-', label='Acc Y')
ax2.plot(time, data2[5], 'b-', label='Acc Z')

plt.show()
