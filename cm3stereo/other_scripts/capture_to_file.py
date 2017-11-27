## Capture a stereo image in jpeg format and save it as a file
## Author: Waqar Rashid
## Email: waqarrashid33@gmail.com

import picamera
import time

with picamera.PiCamera(camera_num=0,stereo_mode = 'side-by-side') as camera:
	camera.resolution = (1280,720)
	camera.start_preview()
	time.sleep(2)
	camera.capture('capture_to_file_time_test.jpg')

