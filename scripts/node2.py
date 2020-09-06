#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import threading

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #print(data.data)
    msg = " "
    if(data.data == "1"):
        msg = "entered state 1"
    elif(data.data == "2"):
        msg = "entered state 2"
    elif(data.data == "3"):
        msg = "entered state 3"
    elif(data.data == "4"):
        msg = "entered state 4"
    elif(data.data == "5"):
        msg = "entered state 5"

    #print(msg)
    rospy.loginfo(""+msg)

def callback2(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #print(data.data)

    t1 = threading.Thread(target=thread_fsm2, args=(data,))
    t2 = threading.Thread(target=thread_fsm2, args=(data,))
    t3 = threading.Thread(target=thread_fsm2, args=(data,))
    t4 = threading.Thread(target=thread_fsm2, args=(data,))
    t5 = threading.Thread(target=thread_fsm2, args=(data,))

    msg = " "
    if(data.data == "1"):
        t1.start()
        t1.join()
    elif(data.data == "2"):
        t2.start()
        t2.join()
    elif(data.data == "3"):
        t3.start()
        t3.join()
    elif(data.data == "4"):
        t4.start()
        t4.join()
    elif(data.data == "5"):
        t5.start()
        t5.join()

    #print(msg)
    #rospy.loginfo(""+msg)

def thread_fsm(data):
    print("entered state %s\t%s" % (str(data.data), threading.current_thread()))
    rospy.loginfo("entered state %s\t%s" % (str(data.data), threading.current_thread()))

def thread_fsm2(data):
    print("entered state %s" % (str(data.data)))
    rospy.loginfo("entered state %s\t%s" % (str(data.data), threading.current_thread()))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('node2', anonymous=True)

#    rospy.Subscriber("chatter", String, thread_fsm)
    rospy.Subscriber("chatter", String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener() 
