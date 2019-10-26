# Introduction

A Simple trying of face recognition by pure OpenCV algorithm.

## Steps

1. Create dataset

   Run the Create_dataSet.py which will open the camera to capture the image with user face. The image file is named/saved as User.[ID].[Number].jpg into dataSet directory. You should make sure each person has unique ID. The script will capture 200 images for each ID user and you may increase the images to improve the accuracy.

   ```
   $python Create_dataSet.py
   enter your id: 1
   ...
   ```

2. Train the face recognition

   ```
   $python Trainner.py
   ```

3. Verification

   ```
   $python Recognizer
   ```

   