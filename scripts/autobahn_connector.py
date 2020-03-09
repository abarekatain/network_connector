#!/usr/bin/env python3


from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
import os
import argparse
import six
import rospy
from std_msgs.msg import String

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
    for topic in sub2net_topics:
        print (topic)
    #run([component])
    #while not rospy.is_shutdown():
    #    rospy.spin()
    print("main gone")