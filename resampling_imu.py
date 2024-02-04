import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

def resampling(data,output):
    # Load your data from the CSV file
    data.columns = ['x', 'y', 'z', 'timestamp']

    # Assuming 'timestamp' is the column with time information and 'value' is your data
    timestamps = data['timestamp'].values
    original_values = data[['x','y','z']].values

    # Generate indices for the downsampled data
    downsampled_indices = np.linspace(0, len(original_values) - 1, 1445)
    print(downsampled_indices)

    # Use cubic spline interpolation
    cubic_spline = CubicSpline(np.arange(len(original_values)), original_values)

    # Interpolate at the downsampled indices
    downsampled_values = cubic_spline(downsampled_indices)

    # Create a DataFrame with the downsampled data
    downsampled_df = pd.DataFrame({
        'x': downsampled_values[:, 0],
        'y': downsampled_values[:, 1],
        'z': downsampled_values[:, 2],
        'timestamp': timestamps[downsampled_indices.astype(int)]
    })

    # Save or further analyze the downsampled data
    downsampled_df.to_csv(output, index=False,header=False)

if __name__ == "__main__":
    accel_data = pd.read_csv('./Dataset/accel_data.csv',header=None)
    resampling(accel_data,"./Dataset/resampled_accel_data.csv")

    gyro_data = pd.read_csv('./Dataset/gyro_data.csv',header=None)
    resampling(gyro_data,"./Dataset/resampled_gyro_data.csv")

    mag_data = pd.read_csv('./Dataset/mag_data.csv',header=None)
    resampling(mag_data,"./Dataset/resampled_mag_data.csv")
