import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

def resampling(data,output,frames):
    data.columns = ['x', 'y', 'z', 'timestamp']

    timestamps = data['timestamp'].values
    original_values = data[['x','y','z']].values

    # Generating indices for the downsamscipypled data
    downsampled_indices = np.linspace(0, len(original_values) - 1, frames)
    print(downsampled_indices)

    # Using cubic spline interpolation
    cubic_spline = CubicSpline(np.arange(len(original_values)), original_values)

    # Interpolate at the downsampled indices
    downsampled_values = cubic_spline(downsampled_indices)

    downsampled_df = pd.DataFrame({
        'x': downsampled_values[:, 0],
        'y': downsampled_values[:, 1],
        'z': downsampled_values[:, 2],
        'timestamp': timestamps[downsampled_indices.astype(int)]
    })

    downsampled_df.to_csv(output, index=False,header=False)

