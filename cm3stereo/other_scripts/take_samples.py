# Display stereo video and when a specific button is pressed do the corner detection
# thingy, after a specific number of images are taken with corners detected, genrerate
# the files required for undistortion
# use file /home/pi/workspace/git/StereoVision/stereovision/stereo_calib_waqar.py
# use file /home/pi/workspace/git/StereoVision/stereovision/undistortedvideo.py

## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com


# import the necessary packages
import cv2
import numpy
import io
import picamera
from stereovision import calibration
from stereovision import exceptions
import time
 

# important variables
rows = 6
columns = 9
square_size = 2.89
index = 1
num_pictures = 5
time_interval = 10 # Time between checking for chessboard
t1 = time.time()

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

# Create calibrator object
calibrator = calibration.StereoCalibrator(rows, columns, square_size, (480,640))


#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera(stereo_mode= 'side-by-side') as camera:
    camera.resolution = (1280, 480)
    camera.vflip = True
    while index<=num_pictures:
        stream.seek(0)
        camera.capture(stream, use_video_port = True, format='jpeg')

        #Convert the picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)

        # display the stereo on screen, displaying them separately would take too much screen space
        cv2.imshow("Stereo", image)
        cv2.waitKey(1) # required for imshow
        if (time.time()-t1) > time_interval:
            try:
                # Separate images
                left =  image[:,0:640]
                right = image[:,640:1280]
                t1 = time.time()
                print(index)
                #print("Checking images for chessborad")
                #calibrator.add_corners((left,right), show_results = False)
                #print("Chessboard number {} found".format(index))
                cv2.imwrite('images/right_{}.ppm'.format(str(index).zfill(2)),left)
                cv2.imwrite('images/left_{}.ppm'.format(str(index).zfill(2)),right)
                index +=1
            except Exception as e:
                print(e)
                continue
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

##if index==num_pictures+1:
##    print("Calibrating!!")
##    # Actual Calibration, calibration is the object of stereocalibration class
##    calibration =calibrator.calibrate_cameras()
##
##    print("Average Error is:")
##    print(calibrator.check_calibration(calibration))
##    calibration.export("result")
##    print("Result saved...")
##
##cv2.destroyAllWindows()
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
##cv2.waitKey(1)
