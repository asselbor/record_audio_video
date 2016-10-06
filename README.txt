
author: thibault asselborn
date: 6.10.2016
description: Node used to record sound and video from a device using a rospy node. Work with alsaaudio lib.

To use this lib, you need to have ROS installed in your computer (http://wiki.ros.org/fr/ROS/Installation).
You can change the Id of your device(s) in the launch file (record_launch.launch). Once done, start the nodes by executing the launch file:
roslaunch record_launch.launch identity:="folderName". 
To stop recording, publish something in the topic "/topic_end_record".
If you want to record just audio or just video, you just have to remove the node launching in the launch file.