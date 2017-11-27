# This program undistort and rectify two images

import numpy
import cv2
import io
import picamera

undistortion_map_left = numpy.load('maps/undistortion_map_left.npy')
rectification_map_left = numpy.load('maps/rectification_map_left.npy')

undistortion_map_right = numpy.load('maps/undistortion_map_right.npy')
rectification_map_right = numpy.load('maps/rectification_map_right.npy')

#left_image = cv2.imread('test_images/left_02.jpg')
#right_image = cv2.imread('test_images/right_02.jpg')

stream = io.BytesIO()
index = 0

with picamera.PiCamera(stereo_mode = 'side-by-side') as camera:
    camera.resolution = (1280,480)
    camera.vflip = True
    while True:
        print(index)
        camera.capture(stream, format = 'jpeg', use_video_port = True)
        buff = numpy.fromstring(stream.getvalue(), dtype = numpy.uint8)
        image = cv2.imdecode(buff, 1)
        #imgL = image[:,0:640]
        #imgR = image[:,640:1280]

        image[:,0:640] = cv2.remap(image[:,0:640], undistortion_map_left, rectification_map_left, cv2.INTER_NEAREST)

        image[:,640:1280] = cv2.remap(image[:,640:1280], undistortion_map_right, rectification_map_right, cv2.INTER_NEAREST)

        #cv2.imshow('left', left)
        #cv2.imshow('right', right)
        cv2.imshow('rectified Stereo', image)
        cv2.waitKey(1)
        index= index+1
        stream.seek(0)
