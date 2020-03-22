import rospy
import json

from rosbridge_library.internal.outgoing_message import OutgoingMessage

class Subscriber_Handler():

    session = None
    

    def __init__(self, topic_name, topic_type):
        self.topic_name = topic_name
        self.topic_type = topic_type
        self.robotID = rospy.get_param("robotID")
        self.network_publish_topic = "com.{}.robot".format(self.robotID)
        self.occupied = False
        

    def callback(self,message):

        outgoing = OutgoingMessage(message)
        json_str = outgoing.get_json_values()
        json_str['topic_name'] = self.topic_name
        json_str['topic_type'] = self.topic_type
        json_str = json.dumps(json_str)
        #print("Calllllllllllllllllll for {}".format(self.topic_name))

        if not self.occupied:
            from twisted.internet import reactor
            reactor.callFromThread(self.publish_to_network,json_str)


    def publish_to_network(self,json_str):
        self.occupied = True    
        Subscriber_Handler.session.publish(self.network_publish_topic, json_str)
        self.occupied = False
        
        
