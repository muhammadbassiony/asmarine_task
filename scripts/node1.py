#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        counter = 0
        while(counter < 5):
            counter += 1 
            rospy.loginfo(str(counter))
            pub.publish(str(counter))
            rospy.sleep(10.)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
