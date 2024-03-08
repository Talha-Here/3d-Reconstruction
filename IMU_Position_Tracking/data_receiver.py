import pandas as pd
import numpy as np

def recieve():
    accel_data = pd.read_csv('./Dataset/resampled_accel_data.csv', usecols=[0, 1, 2],header=None) #resampled_
    gyro_data = pd.read_csv('./Dataset/resampled_gyro_data.csv', usecols=[0, 1, 2],header=None)
    mag_data = pd.read_csv('./Dataset/resampled_mag_data.csv', usecols=[0, 1, 2],header=None)

    # Concatenate the three dataframes horizontally
    data = pd.concat([gyro_data,accel_data, mag_data], axis=1)
    data=np.array(data)

    # print(type(data),np.shape(data))
    return data