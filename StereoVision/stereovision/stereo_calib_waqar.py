
import cv2
import numpy as np
import time
import calibration
import exceptions

# important variables
rows = 6
columns = 9
square_size = 2.89
index = 1
camera0 = cv2.VideoCapture(0)
camera1 = cv2.VideoCapture(1)
num_pictures = 10
#timer = time.time()
# Create calibrator object
calibrator = calibration.StereoCalibrator(rows, columns, square_size, (480,640))

print("Device openend")
key = 'c'
# Loop for taking pictures and detecting corners
while index<=num_pictures:

    # Taking pictures
    ret0, frame_r = camera0.read()
    ret1, frame_l = camera1.read()
    cv2.imshow('Camera right', frame_r)
    cv2.imshow('Camera left', frame_l)
    cv2.waitKey(1) # required to make imshow show image
    #print("Loop")

    # StereoCalibration part Press "c" to activate this part
    if cv2.waitKey(1) & 0xFF == ord(key):
        if(key=='c'): # state machine sort of
            key='d'
        else:
            key='c'        
        try:
            print('Looking for Chessboard')
            calibrator.add_corners((frame_l,frame_r), show_results=False)  #Bug: Make a specific exception for chessboard not found            
            print("Chessboard number {} found".format(index))
            cv2.imwrite('images2/right_{}.ppm'.format(str(index).zfill(len(str(num_pictures)))),frame_r)
            cv2.imwrite('images2/left_{}.ppm'.format(str(index).zfill(len(str(num_pictures)))),frame_r)
            print('Press {} to Check for Chessboard'.format(key))
            index +=1
        except Exception as e:
            print(e)
            print('Press {} to Check for Chessboard'.format(key))
            continue
        
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

if index==num_pictures+1:        
    # Actual Calibration, calibration is the object of stereocalibration class
    calibration =calibrator.calibrate_cameras()

    print("Average Error is:")
    print(calibrator.check_calibration(calibration))
    calibration.export("result")
    print("Result saved...")
    #print("Picures taken")


camera0.release()
camera1.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
