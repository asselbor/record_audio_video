#!/usr/bin/env python
#coding: utf-8

'''
author: thibault asselborn
date: 6.10.2016
description: Node used to record sound from a device using a rospy node. Work with alsaaudio lib.

'''

import os, rospy, datetime, alsaaudio, wave, numpy
from os.path import expanduser
from std_msgs.msg import String

reccord = True

def callBackEndRecording(data):
	# if comething was publish in this topic, stop recording
	reccord = False
	rospy.signal_shutdown("Done.")


if __name__ == '__main__':
	# init node
	rospy.init_node("record_audio")

	# get params name
	DEVICE = rospy.get_param('~device')
	TOPIC_END_RECORD = rospy.get_param('~topic_end_record')
	rospy.Subscriber(TOPIC_END_RECORD, String, callBackEndRecording)

	# get the folder name
	FOLDER_NAME = rospy.get_param('~identity')

	# create folder where to put the audio file
	home = expanduser("~")
	pathFolder = home + "/outputMemory/" + FOLDER_NAME
	# create directory concerning the name of the user if does not exists
	try:
		os.stat(pathFolder)
	except:
		os.makedirs(pathFolder)
	# file name
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	path = pathFolder + "/outputAudio_" + date + ".wav"

	# create listener
	inp = alsaaudio.PCM(DEVICE)
	inp.setchannels(1)
	inp.setrate(44100)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	inp.setperiodsize(1024)

	w = wave.open(path, 'w')
	w.setnchannels(1)
	w.setsampwidth(2)
	w.setframerate(44100)

	# record sound
	while reccord == True:
		l, data = inp.read()
		a = numpy.fromstring(data, dtype='int16')
		w.writeframes(data)


	# start node
	rospy.spin()




