

class Subscriber_Handler():

    def __init__(self, topic_name, topic_type):
        self.topic_name = topic_name
        self.topic_type = topic_type

    def callback(self,message):
        #print(self.topic_name)
        pass
