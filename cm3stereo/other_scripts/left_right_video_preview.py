## Display video from both cameras in pi compute module 3.
##       2-3 FPS when using video port
##       1.2 FPS when not using video port

## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com


# import the necessary packages
import cv2
import numpy
import io
import picamera
import time
 

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera(stereo_mode= 'side-by-side') as camera:
    camera.resolution = (2560, 720)
    while True:
        start_time = time.time()
        camera.capture(stream, use_video_port = False, format='jpeg')

        #Convert the picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)

         
        # display the image on screen and wait for a keypress
        cv2.imshow("Left", image[:,0:1280])
        cv2.imshow("Right", image[:,1280:2560])
        cv2.waitKey(1)
        stream.seek(0)
        total_time = time.time()-start_time
        print(1/total_time)
