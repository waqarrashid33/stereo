## Capture a N numer of stereo image side by side, convert it to opencv image format,
## then separate the two images and save them along with stereo image
## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com


# import the necessary packages
import cv2
import numpy
import io
import picamera
import time

N = 5 # Number of images
time_period = 1
 

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera(stereo_mode= 'side-by-side') as camera:
    #camera.resolution = (1280, 720)
    camera.resolution = (1280,480)
    camera.vflip = True
    print("Wait {} seconds for first caputre".format(time_period))
    for i in range(N):
        time.sleep(time_period)
        camera.capture(stream, format='jpeg', use_video_port = True)
        #Convert the picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)
        left = image[:,0:640]
        right = image[:,640:1280]

        # display the image on screen and wait for a keypress
        cv2.imwrite('left{}.jpg'.format(str(i).zfill(len(str(N)))), left)
        cv2.imwrite('right_{}.jpg'.format(str(i).zfill(len(str(N)))), right)
        print("Captured {}\n".format(i+1))
        stream.seek(0)
