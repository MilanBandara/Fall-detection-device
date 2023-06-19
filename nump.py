import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Create an array
arr = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# arr3 = np.array([1, 2, 3])
# data = np.vstack((arr,arr2,arr3))
# np.save('data.npy', data)

def FFT(signal):
    fourier_transform = np.fft.fft(signal)
    # Compute the frequencies corresponding to the Fourier transform
    frequencies = np.fft.fftfreq(len(signal))

    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(fourier_transform)
    power_spectrum = np.abs(fourier_transform) ** 2
    phase_response = np.angle(fourier_transform)

    # Plot the magnitude spectrum
    plt.plot(frequencies, magnitude_spectrum)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('Magnitude Spectrum')
    plt.show()

def to_image(signal):
    new_signal = signal[1:]
    max_values = np.amax(new_signal, axis=1)
    normalized = new_signal/max_values[:, np.newaxis]
    scaled_array = ((normalized + 1) * 127.5).astype(np.uint8)
    # Resize the grayscale image
    resized_array = cv2.resize(scaled_array, (500, 250))

    # Display the resized grayscale image
    cv2.imshow("Resized Grayscale Image", resized_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def label_data():
    fall_folder_path = "D:/Product_design/Fall-detection-device/Fall_data"
    fall_files = os.listdir(fall_folder_path)
    Non_fall_folder_path = "D:/Product_design/Fall-detection-device/Non_fall_data"
    non_fall_files = os.listdir(Non_fall_folder_path)
    

    for i in range(1,len(fall_files)):
        data = np.load('D:/Product_design/Fall-detection-device/Fall_data/data'+str(i)+".npy")
        print(data.shape,i) #37th data has a problem in dimesions        
    

# Load the array from the file
# data = np.load('Data_2/Forward/Milan/data1.npy')
# print(np.max(data))
# to_image(data)
# FFT(data[4])
# print(data.shape)
# Set up the plot
# fig, ax = plt.subplots()
# ax.set_xlabel('Time')
# ax.set_ylabel('Data')
# ax.plot(data[0], data[1], 'r-', label='Acc X')
# ax.plot(data[0], data[2], 'g-', label='Acc Y')
# ax.plot(data[0], data[3], 'b-', label='Acc Z')
# plt.show()

label_data()