import numpy as np
from hmmlearn import hmm


location = "D:/Product_design/Fall-detection-device/Data_for_HMM"

training_data = []
for i in range(1,41):
    itter = "/data" + str(i) + ".npy"
    data = np.load(location + itter)[1:].T
    training_data.append(data)

training_data_array = np.array(training_data,dtype=object)

print(training_data_array.shape)

training_data_array = np.array(training_data_array)
model = hmm.MultinomialHMM(n_components=2)  # Adjust the number of hidden states as needed
model.fit(training_data)
