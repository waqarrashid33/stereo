# This program loads the calibration results and generate undistortion and rectification maps for both left and right cameras.
# It saves these maps in a folder

# Author Waqar Rashid
# Email waqarrashid33@gmail.com

import numpy
import cv2


cam_mats_left = numpy.load('stereo_result/cam_mats_left.npy')
cam_mats_right = numpy.load('stereo_result/cam_mats_right.npy')
dist_coefs_left = numpy.load('stereo_result/dist_coefs_left.npy')
dist_coefs_right = numpy.load('stereo_result/dist_coefs_right.npy')
rect_trans_left = numpy.load('stereo_result/rect_trans_left.npy')
rect_trans_right = numpy.load('stereo_result/rect_trans_right.npy')
proj_mats_left = numpy.load('stereo_result/proj_mats_left.npy')
proj_mats_right = numpy.load('stereo_result/proj_mats_right.npy')
image_size = (640,480)
(undistortion_map_left, rectification_map_left) = cv2.initUndistortRectifyMap(  cam_mats_left,
                                                                                dist_coefs_left,
                                                                                rect_trans_left,
                                                                                proj_mats_left,
                                                                                image_size,
                                                                                cv2.CV_32FC1)
print(undistortion_map_left.shape)
print(rectification_map_left.shape)
numpy.save('maps/undistortion_map_left.npy',undistortion_map_left)
numpy.save('maps/rectification_map_left.npy',rectification_map_left)

(undistortion_map_right, rectification_map_right) = cv2.initUndistortRectifyMap(  cam_mats_right,
                                                                                dist_coefs_right,
                                                                                rect_trans_right,
                                                                                proj_mats_right,
                                                                                image_size,
                                                                                cv2.CV_32FC1)

print(undistortion_map_right.shape)
print(rectification_map_right.shape)
numpy.save('maps/undistortion_map_right.npy',undistortion_map_right)
numpy.save('maps/rectification_map_right.npy',rectification_map_right)
