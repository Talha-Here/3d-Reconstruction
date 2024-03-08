import cv2,os
import pandas as pd
import resampling_imu
from IMU_Position_Tracking import main
import distances_calculator

#chair 811, 29.603341985723556
#room with chairs 1445, 29.602837137732294
#room without chairs 29.602275594126848, 1042

def extract_frames(video_path, output_folder, factor):
    cap = cv2.VideoCapture(video_path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    interval = factor

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("frames =",frame_count)
    print("fps =",fps)

    # x=0
    # for i in range(0, frame_count, interval):
    #     # Set the frame position
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, i)

    #     # Read the frame
    #     ret, frame = cap.read()

    #     if ret:
    #         # Save the frame with padded numbering
    #         frame_number = x + 1  # Adjust frame numbering starting from 1
    #         frame_number_str = f"{frame_number:02d}"  # Padded with zeros
    #         frame_filename = f"{output_folder}/{frame_number_str}.png"
    #         cv2.imwrite(frame_filename, frame)
    #         x=x+1

    cap.release()
    return frame_count,fps

if __name__ == "__main__":
    video_path = "./Dataset/video.mp4"
    output_folder = "DownSampledVideo_Frames"
    downsampling_factor = 1

    frame_count,fps=extract_frames(video_path, output_folder, downsampling_factor)

    accel_data = pd.read_csv('./Dataset/accel_data.csv',header=None)
    resampling_imu.resampling(accel_data,"./Dataset/resampled_accel_data.csv",frame_count)

    gyro_data = pd.read_csv('./Dataset/gyro_data.csv',header=None)
    resampling_imu.resampling(gyro_data,"./Dataset/resampled_gyro_data.csv",frame_count)

    mag_data = pd.read_csv('./Dataset/mag_data.csv',header=None)
    resampling_imu.resampling(mag_data,"./Dataset/resampled_mag_data.csv",frame_count)

    #Integrating IMU_Position_Tracking
    p=main.plot_trajectory(fps)

    #Calculating distances
    distances_calculator.dist_calc(p)
