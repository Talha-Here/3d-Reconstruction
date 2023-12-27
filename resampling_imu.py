# import pandas as pd

# def resample_and_save(input_file, output_file, frames):
#     # Read CSV file without header (column names)
#     data = pd.read_csv(input_file, header=None)

#     # Giving column names as per documentation reference
#     data.columns = ['x', 'y', 'z', 'timestamp']

#     # Calculate the resampling rate
#     resampling_rate = len(data) / frames
#     indices=[]

#     for i in range(1,frames+1):
#         indices.append(round((resampling_rate*i)-1))

#     resampled_data = data.iloc[indices]

#     # Save resampled data to a new CSV file
#     resampled_data.to_csv(output_file, index=True)

# frames=1445

# resample_and_save('./Dataset/accel_data.csv', 'resampled_accel_data.csv', frames)
# resample_and_save('./Dataset/gyro_data.csv', 'resampled_gyro_data.csv', frames)
# resample_and_save('./Dataset/mag_data.csv', 'resampled_mag_data.csv', frames)


## New Appproach


import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Load your data from the CSV file
df = pd.read_csv('accel_data.csv',header=None)
df.columns = ['x', 'y', 'z', 'timestamp']

# Assuming 'timestamp' is the column with time information and 'value' is your data
timestamps = df['timestamp'].values
original_values = df['x'].values

# Generate indices for the downsampled data
downsampled_indices = np.linspace(0, len(original_values) - 1, 1445)
print(downsampled_indices)

# Use cubic spline interpolation
cubic_spline = CubicSpline(np.arange(len(original_values)), original_values)

# Interpolate at the downsampled indices
downsampled_values = cubic_spline(downsampled_indices)

# Create a DataFrame with the downsampled data
downsampled_df = pd.DataFrame({'timestamp': timestamps[downsampled_indices.astype(int)],
                               'downsampled_value': downsampled_values})

# Save or further analyze the downsampled data
downsampled_df.to_csv('downsampled_data.csv', index=True)

# Plot original and downsampled data for visualization
plt.plot(timestamps, original_values, label='Original Data')
plt.plot(downsampled_df['timestamp'], downsampled_df['downsampled_value'], 'o', label='Downsampled Data')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()