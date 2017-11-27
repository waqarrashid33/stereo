## Capture a stereo image in jpeg format and save it as a file
## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com

import picamera
import time

with picamera.PiCamera(camera_num=0,stereo_mode = 'side-by-side') as camera:
	camera.resolution = (2560,720)
	time.sleep(2)
	camera.capture('capture_full_size.jpg')

