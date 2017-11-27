# This program loads the camear distortion parameters and undistort the images
# using these parameters. It shows the original pictures coming from camera as
# well as these pictures after undistortion

# Waqar Rashid
# 13 November 2016
# Collision avoidance project
import cv2
import numpy as np
import time

#camera0 = cv2.VideoCapture(0)
camera1 = cv2.VideoCapture(1)

# Load camera mappings from files here, go to calibrate.py to calculate them
mapx = np.load("mapx.param")
mapy =  np.load("mapy.param")

print("Device openend")
while True:
    #ret0, frame0 = camera0.read()
    ret1, frame1 = camera1.read()
    cv2.imshow('Camera Direct', frame1)

    # Perform the undistortion
    st = cv2.remap(frame1,mapx,mapy,cv2.INTER_LINEAR)

    
    #cv2.imshow('picture from camera 0', frame0)
    cv2.imshow('After undistortion', st)
    #time.sleep(3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#camera0.release()
camera1.release()
cv2.destroyAllWindows()
# opencv bug, call cv2.waitKey(1) 4 times for one window
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
