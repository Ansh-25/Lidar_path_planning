#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray


def obstacle_pub():
    pub = rospy.Publisher('obstacle',Float64MultiArray,queue_size=30)
    obs = Float64MultiArray()
    obs.data = [0,15,0,30,0,45,15,0,15,15,15,30,15,45,30,0,30,15,30,30,30,45,45,0,45,15,45,30,45,45]
    rospy.init_node('obstacle',anonymous=True)
    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        pub.publish(obs)
        rate.sleep

if __name__ == '__main__':
    try:
        obstacle_pub()
    except rospy.ROSInterruptException:
        pass
