import numpy as np
import os

def label_data():
    fall_folder_path = "D:/Product_design/Fall-detection-device/Fall_data"
    fall_files = os.listdir(fall_folder_path)
    Non_fall_folder_path = "D:/Product_design/Fall-detection-device/Non_fall_data"
    non_fall_files = os.listdir(Non_fall_folder_path)
    print(len(non_fall_files))
    

    for i in range(1,len(fall_files)+1):
        #skip the data with wrong shape
        data = np.load('D:/Product_design/Fall-detection-device/Fall_data/data'+str(i)+".npy")
        data = data[1:]
        label = np.ones(data.shape[1],dtype=np.int8) #data type could cause a problem
        data = np.vstack((label,data))
        np.save('D:/Product_design/Fall-detection-device/positive_labeled/data'+str(i)+'.npy', data)
        np.save('D:/Product_design/Fall-detection-device/training_data/data'+str(i)+'.npy', data)
        # print(data.shape)

    for i in range(1,len(non_fall_files)+1):
        data = np.load('D:/Product_design/Fall-detection-device/Non_fall_data/data'+str(i)+".npy")
        data = data[1:]
        label = np.zeros(data.shape[1],dtype=np.int8) #data type could cause a problem
        data = np.vstack((label,data))
        np.save('D:/Product_design/Fall-detection-device/negative_labeled/data'+str(i)+'.npy', data)
        np.save('D:/Product_design/Fall-detection-device/training_data/data'+str(len(fall_files)+i)+'.npy', data)
        print(data.shape)

def clean_data():
    #complete this function or clean data in the label_data function
    training_data_path = "D:/Product_design/Fall-detection-device/training_data"
    fall_files = os.listdir(training_data_path)
    
    for i in range(1,len(fall_files)+1):
        data = np.load('D:/Product_design/Fall-detection-device/training_data/data'+str(i)+".npy")
        if data.shape != (7,1000):
            print("wrong shape!, index - ",'data'+str(i)+".npy")

# Load the array from the file
# data = np.load('D:/Product_design/Fall-detection-device/Fall_data/data36.npy')
# print(data.shape)

# label_data()
# data = np.load('D:/Product_design/Fall-detection-device/training_data/data41.npy')
# print(data)
clean_data()