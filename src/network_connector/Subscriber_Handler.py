import rospy

class Subscriber_Handler():

    def __init__(self, topic_name, topic_type,clientSession):
        self.topic_name = topic_name
        self.topic_type = topic_type
        self.robotID = rospy.get_param("robotID")
        self.session = clientSession

    def callback(self,message):
        self.session.publish('com.myapp.hello', self.topic_name)
        #print(type(self.session))
        
