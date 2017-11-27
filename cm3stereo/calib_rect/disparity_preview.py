# This program undistort and rectify two images

import numpy
import cv2
import io
import picamera
from matplotlib import pyplot as plt

undistortion_map_left = numpy.load('maps/undistortion_map_left.npy')
rectification_map_left = numpy.load('maps/rectification_map_left.npy')

undistortion_map_right = numpy.load('maps/undistortion_map_right.npy')
rectification_map_right = numpy.load('maps/rectification_map_right.npy')

stream = io.BytesIO()
index = 0
#stereo =  cv2.StereoBM_create()
stereo = cv2.StereoSGBM_create(minDisparity = 0, numDisparities = 16, blockSize = 3)

with picamera.PiCamera(stereo_mode = 'side-by-side') as camera:
    camera.resolution = (1280,480)
    camera.vflip = True
    while True:
        print(index)
        camera.capture(stream, format = 'jpeg', use_video_port = True)
        buff = numpy.fromstring(stream.getvalue(), dtype = numpy.uint8)
        image = cv2.imdecode(buff, 1)

        imgL = cv2.remap(image[:,0:640], undistortion_map_left, rectification_map_left, cv2.INTER_NEAREST)
        imgR = cv2.remap(image[:,640:1280], undistortion_map_right, rectification_map_right, cv2.INTER_NEAREST)
        left = cv2.cvtColor(imgL, cv2.COLOR_RGB2GRAY)
        right = cv2.cvtColor(imgR, cv2.COLOR_RGB2GRAY)
        disparity = stereo.compute(left,right)
        disparity = cv2.normalize(disparity, disparity,alpha=0, beta= 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        #print(disparity.max())
        #print(disparity.min())
        
        cv2.imshow('disparity', disparity)
        #plt.imshow(disparity, 'gray', block=False)
        #plt.show()
        cv2.waitKey(1)
        index= index+1
        stream.seek(0)
