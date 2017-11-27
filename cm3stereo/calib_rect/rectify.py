# This program undistort and rectify two images

import numpy
import cv2

undistortion_map_left = numpy.load('maps/undistortion_map_left.npy')
rectification_map_left = numpy.load('maps/rectification_map_left.npy')

undistortion_map_right = numpy.load('maps/undistortion_map_right.npy')
rectification_map_right = numpy.load('maps/rectification_map_right.npy')

left_image = cv2.imread('test_images/left_02.jpg')
right_image = cv2.imread('test_images/right_02.jpg')

left = cv2.remap(left_image, undistortion_map_left, rectification_map_left, cv2.INTER_NEAREST)

right = cv2.remap(right_image, undistortion_map_right, rectification_map_right, cv2.INTER_NEAREST)

cv2.imshow('left', left)
cv2.imshow('right', right)
cv2.waitKey()
