#!/usr/bin/env python
#coding: utf-8

'''
author: thibault asselborn
date: 6.10.2016
description: Node used to record video from a device using a rospy node. Work with cv2 lib.

'''

import numpy as np
import cv2
import datetime
import rospy
import os
from os.path import expanduser
from std_msgs.msg import String


reccord = True


def callBackEndRecording(data):
	# if something publish in this topicm, stop record video and release everything
	cap.release()
	out.release()
	cv2.destroyAllWindows()

	reccord = False


if __name__ == '__main__':
	# init node
	rospy.init_node("record_video")

	# get param names
	DEVICE = rospy.get_param('~device')
	TOPIC_END_RECORD = rospy.get_param('~topic_end_record')
	rospy.Subscriber(TOPIC_END_RECORD, String, callBackEndRecording)

	# get the folder name
	FOLDER_NAME = rospy.get_param('~identity')
	home = expanduser("~")
	pathFolder = home + "/outputMemory/" + FOLDER_NAME
	# create directory if does not exists
	try:
		os.stat(pathFolder)
	except:
		os.makedirs(pathFolder)

	# cretae video file
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	path = pathFolder + "/outputVideo_" + date + ".avi"

	
	# Define the codec and create VideoWriter object
	cap = cv2.VideoCapture(DEVICE)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(path,fourcc, 20.0, (640,480))

	while reccord == True:
	    ret, frame = cap.read()
	    if ret==True:
	        # write the flipped frame
	        out.write(frame)

	        cv2.imshow('frame',frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	    else:
	        break

	rospy.spin()





