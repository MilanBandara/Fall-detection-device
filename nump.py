import numpy as np
import matplotlib.pyplot as plt

# Create an array
arr = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# arr3 = np.array([1, 2, 3])
# data = np.vstack((arr,arr2,arr3))
# np.save('data.npy', data)

# Load the array from the file
data = np.load('data.npy')

print(data.shape)
plt.plot(data[0],data[3])
plt.show()