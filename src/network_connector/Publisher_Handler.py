import json
import rospy
#from std_msgs.msg import *
import rospy

from rosbridge_library.internal import ros_loader, message_conversion

class Publisher_Handler():

    

    def __init__(self):
        self.pub_objects = {}

    def on_event(self, message):
        #process the message
        msg_dict = json.loads(message)
        topic_name = msg_dict['topic_name']
        topic_type = msg_dict['topic_type']
        del msg_dict['topic_name']
        del msg_dict['topic_type']

        #get the topic type
        msg_class = ros_loader.get_message_class(topic_type)

        # Create a message instance
        inst = msg_class()

        # Populate the instance, propagating any exceptions that may be thrown
        message_conversion.populate_instance(msg_dict, inst)

        if not topic_name in self.pub_objects:
            self.pub_objects[topic_name] = rospy.Publisher(topic_name, msg_class, queue_size=10)

        self.pub_objects[topic_name].publish(inst)    
