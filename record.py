import cv2
import numpy as np
import os
import time

i = 0
MAX_FRAMES = int(input("Number of frames to capture:"))
FPS = int(input("FPS:"))
SOURCE = r'C:\\Users\\ronal\\Downloads\\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\\openpose\\examples\\media'
OUT_NAME = 'CAPTURE_{}_FPS_{}_FRAMES.avi'.format(str(FPS), str(MAX_FRAMES))


# delete any video files
# os.system('del *.avi')

# Create a VideoCapture object
cap = cv2.VideoCapture(1)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(OUT_NAME, cv2.VideoWriter_fourcc('M','J','P','G'), FPS, (frame_width,frame_height))

while(True):
  ret, frame = cap.read()

  if ret == True and i < MAX_FRAMES + 1: 
    
    # Write the frame into the file 'output.avi'
    out.write(frame)

    # Display the resulting frame    
    cv2.imshow('frame',frame)

    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q') or i > MAX_FRAMES:
      break

    i += 1

    # print("frame :", i)

  # Break the loop
  else:
    break  

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
