#!/usr/bin/env python3


from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import os
import argparse
import six
import rospy
import json
from std_msgs.msg import String

from rostopic import get_topic_type
from rosbridge_library.internal import ros_loader

from network_connector.Subscriber_Handler import Subscriber_Handler



url = u'ws://localhost:8080/ws'
realm = u'realm1'

def get_parameters():
    global pub2net_topics , sub2net_topics, robotID
    pub2net_topics = rospy.get_param("pub2net_topics")
    sub2net_topics = rospy.get_param("sub2net_topics")
    robotID = rospy.get_param("robotID")
    

class ClientSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("Session Attached")
        
        #res = yield self.register(self)
        self.network_subscribe_topic = "com.{}.robot".format(robotID)
        sub = yield self.subscribe(self.on_event, self.network_subscribe_topic)
        print(self.network_subscribe_topic)

        self.handle_ros_subscribers()





        

    def on_event(self, message):
        #process the message
        msg_dict = json.loads(message)
        topic = msg_dict['topic_name']
        topic_type = msg_dict['topic_type']
        del msg_dict['topic_name']
        del msg_dict['topic_type']
        msg = json.dumps(msg_dict)

        #get the topic type
        msg_class = ros_loader.get_message_class(topic_type)






    def handle_ros_subscribers(self):

        Subscriber_Handler.session = self

        for topic_name in pub2net_topics:

            topic_type = get_topic_type(topic_name)[0]
            msg_class = ros_loader.get_message_class(topic_type)

            subscriber_Handler = Subscriber_Handler(topic_name,topic_type)

            rospy.Subscriber(topic_name, msg_class, subscriber_Handler.callback)

            



if __name__ == "__main__":
    rospy.init_node('autobahn_connector', anonymous=False)
    get_parameters()


    runner = ApplicationRunner(url=url, realm=realm)
    runner.run(ClientSession, auto_reconnect=True)

    print("main gone")