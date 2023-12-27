import cv2,os

video_path = './Dataset/video.mp4'
output_path = 'downsampled_video.mp4'
output_folder = 'DownSampledVideo_Frames'

downsampling_factor = 2  # Adjust as needed
frame_number = 0

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

# downsampling_rate = 1 / downsampling_factor

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     if frame_number % downsampling_factor == 0:
#         output_filename = f'{output_folder}/frame_{frame_number:04d}.png'
#         cv2.imwrite(output_filename, frame)   
#         # out.write(frame)         
#     frame_number += 1

# cap.release()
