import cv2
import os

frames_folder = 'DownSampledVideo_Frames'

keypoints_list = []
descriptors_list = []

orb = cv2.ORB_create()

# Function to read frames from a folder and extract keypoints and descriptors
def extract_features(folder_path):
    keypoints_list = []
    descriptors_list = []

    frame_paths = sorted([os.path.join(folder_path, frame) for frame in os.listdir(folder_path) if frame.endswith('.png') and int(frame.split('_')[1].split('.')[0]) % 2 == 0])

    for frame_path in frame_paths:
        # Read the frame
        frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)

        # Find keypoints and descriptors
        keypoints, descriptors = orb.detectAndCompute(frame, None)

        # Store keypoints and descriptors
        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)

    return keypoints_list, descriptors_list

keypoints_list, descriptors_list = extract_features(frames_folder)

# Perform feature matching between consecutive frames
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

for i in range(len(descriptors_list) - 1):
    # Match descriptors
    matches = bf.match(descriptors_list[i], descriptors_list[i + 1])

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw matches
    img_matches = cv2.drawMatches(
        cv2.imread(os.path.join(frames_folder, f'frame_{i * 2:04d}.png')),
        keypoints_list[i],
        cv2.imread(os.path.join(frames_folder, f'frame_{(i + 1) * 2:04d}.png')),
        keypoints_list[i + 1],
        matches[:50],  # Change the number to visualize more or fewer matches
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    Output_window = f'Matches between frame {i * 2} and frame {(i + 1) * 2}'
    cv2.imshow(Output_window, img_matches)
    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()