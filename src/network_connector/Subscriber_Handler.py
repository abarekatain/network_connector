import rospy

class Subscriber_Handler():

    session = None

    def __init__(self, topic_name, topic_type):
        self.topic_name = topic_name
        self.topic_type = topic_type
        self.robotID = rospy.get_param("robotID")
        #self.session = clientSession
        

    def callback(self,message):
        Subscriber_Handler.session.publish('com.myapp.hello', self.topic_name)
        #print(type(self.session))
        
