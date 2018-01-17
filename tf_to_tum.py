#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(300.0)
    F = open("datos_odometria_frame_camara2.txt","w") 
    L = open("datos_aruco_frame_camara2.txt","w")
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/base_map', '/CameraTop_optical_frame', rospy.Time(0))
            (trans_ar,rot_ar) = listener.lookupTransform('/base_map','/camera_position',rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        now = rospy.Time.now()
        print "{} {} {} {} {} {} {} {}".format(now,trans[0],trans[1],trans[2],rot[0],rot[1],rot[2],rot[3])
        F.write("{} {} {} {} {} {} {} {}\n".format(now,trans[0],trans[1],trans[2],rot[0],rot[1],rot[2],rot[3]))
        L.write("{} {} {} {} {} {} {} {}\n".format(now,trans_ar[0],trans_ar[1],trans_ar[2],rot_ar[0],rot_ar[1],rot_ar[2],rot_ar[3]))
        rate.sleep()
    
    F.close()
    L.close()