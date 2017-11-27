## Display side by side stereo video from compute module 3.
##      4-6 FPS when using video port for 1280x720
##      1.2 FPS when not using video port for 1280x720

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
with picamera.PiCamera(stereo_mode= 'side-by-side', sensor_mode = 7) as camera:
    camera.resolution = (1280, 480)
    camera.vflip = True # Images were upside down
    while True:
        start_time = time.time()
        camera.capture(stream, use_video_port = True, format='jpeg')

        #Convert the picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)
         
        # display the image on screen and wait for a keypress
        cv2.imshow("Stereo image", image)
        cv2.waitKey(1)
        stream.seek(0)
        total_time = time.time()-start_time
        print(1/total_time)
