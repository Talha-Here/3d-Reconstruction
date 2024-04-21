---

# 3d Mapping Of Buildings For Inspection

## Description
This project aims to synchronize video recording with Inertial Measurement Unit (IMU) data through an Android app called [OpenCamera Sensors](https://github.com/prime-slam/OpenCamera-Sensors). The recorded videos and IMU data are uploaded to our website where the data is stored in [Firebase](https://firebase.google.com/). The backend of the system then downloads the data from Firebase, extracts frames from the video, and applies downsampling to both the extracted frames and IMU data to match their timestamps. The downsampled frames are used to reconstruct a 3D model using structure from motion (SfM) techniques. Additionally, camera poses are estimated from the downsampled IMU data. The scale consistency of the reconstructed 3D model is then estimated using the camera poses and the data obtained after reconstruction. Finally, the system estimates the scale factor and incorporates it into the 3D model, converting it into a suitable format for visualization and providing it to the front end.

## Project Flow
1. Synchronized video recording with IMU data using the "OpenCamera Sensors" Android app.
2. Upload video with IMU data to the project website for storage in Firebase.
3. Downloading of data from Firebase by the backend.
4. Extraction of frames from the video by the backend.
5. Downsampling of extracted frames and IMU data to match timestamps.
6. Reconstruction of a 3D model using downscaled frames through structure from motion.
7. Estimation of camera poses from the downsampled IMU data.
8. Estimation of scale consistency using camera poses and reconstructed data.
9. Estimation of the scale factor and incorporation into the 3D model.
10. Conversion of the 3D model into a suitable format for visualization and provision to the front end.

## Usage
1. **Recording**: Use the "OpenCamera Sensors" Android app to record synchronized video with IMU data.
2. **Upload**: Upload the recorded video with IMU data to the project website.
3. **Backend Processing**: Backend processing will take some time to process your data and then provide you with a visualization of your 3d model.

## Contributors
- [Ahmad Baseer](https://github.com/Ahmad-Baseer)
- [Talha Hussain Khan](https://github.com/Talha-Here)
- [Arbaz Moin]()
- [Areesha Fateh]()

---
