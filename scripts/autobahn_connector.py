#!/usr/bin/env python


from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
import os
import argparse
import six
import rospy
from std_msgs.msg import String

from rostopic import get_topic_type
from rosbridge_library.internal import ros_loader

from network_connector.Subscriber_Handler import Subscriber_Handler



url = u'ws://localhost:8080/ws'
realmv = u'realm1'
component = Component(transports=url, realm=realmv)

def get_parameters():
    global pub2net_topics , sub2net_topics
    pub2net_topics = rospy.get_param("pub2net_topics")
    sub2net_topics = rospy.get_param("sub2net_topics")





if __name__ == "__main__":
    rospy.init_node('autobahn_connector', anonymous=False)
    get_parameters()

    for topic_name in pub2net_topics:
        topic_type = get_topic_type(topic_name)[0]
        subscriber_Handler = Subscriber_Handler(topic_name,topic_type)
        msg_class = ros_loader.get_message_class(topic_type)
        rospy.Subscriber(topic_name, msg_class, subscriber_Handler.callback)



    #run([component])
    while not rospy.is_shutdown():
        rospy.spin()
    print("main gone")