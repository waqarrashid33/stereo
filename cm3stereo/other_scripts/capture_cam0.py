## Capture image from a camera , convert it to opencv image format and then display it
## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com

# import the necessary packages
import cv2
import numpy
import io
import picamera
 

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera(camera_num=0, stereo_mode= 'none') as camera:
    camera.resolution = (1280, 720)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)
 
# display the image on screen and wait for a keypress
cv2.imwrite("cam0.jpg", image)
cv2.waitKey(0)
