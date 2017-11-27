# This program undistort and rectify two images

import numpy
import cv2
from matplotlib import pyplot as plt

undistortion_map_left = numpy.load('maps/undistortion_map_left.npy')
rectification_map_left = numpy.load('maps/rectification_map_left.npy')

undistortion_map_right = numpy.load('maps/undistortion_map_right.npy')
rectification_map_right = numpy.load('maps/rectification_map_right.npy')

left_image = cv2.imread('test_images/left_07.jpg')
right_image = cv2.imread('test_images/right_07.jpg')

imgL = cv2.remap(left_image, undistortion_map_left, rectification_map_left, cv2.INTER_NEAREST)

imgR = cv2.remap(right_image, undistortion_map_right, rectification_map_right, cv2.INTER_NEAREST)

left = cv2.cvtColor(imgL, cv2.COLOR_RGB2GRAY)
right = cv2.cvtColor(imgR, cv2.COLOR_RGB2GRAY)

#stereo = cv2.StereoBM_create(numDisparities = 32, blockSize = 31)
#stereo = cv2.StereoBM_create()
#stereo = cv2.StereoBM_create(numDisparities = 48, blockSize = 5)
stereo = cv2.StereoSGBM_create(minDisparity = 0, numDisparities = 16, blockSize = 3)

disparity = stereo.compute(left, right)

#print(disparity[0:10,0:10])

#cv2.imshow('disparity',disparity) # find a way to display it using opencv
plt.imshow(disparity, 'gray')
plt.show()
cv2.waitKey()
