import rospy
from rospy_message_converter import json_message_converter
from std_msgs.msg import *
import json

class Subscriber_Handler():

    session = None
    

    def __init__(self, topic_name, topic_type):
        self.topic_name = topic_name
        self.topic_type = topic_type
        self.robotID = rospy.get_param("robotID")
        self.network_publish_topic = "com.{}.robot".format(self.robotID)
        #self.session = clientSession
        

    def callback(self,message):

        json_str = json_message_converter.convert_ros_message_to_json(message)
        json_str = json.loads(json_str)
        json_str['topic_name'] = self.topic_name
        json_str['topic_type'] = self.topic_type
        json_str = json.dumps(json_str)
        #print(json_str)
        Subscriber_Handler.session.publish(self.network_publish_topic, json_str)
        #print(type(self.session))
        
