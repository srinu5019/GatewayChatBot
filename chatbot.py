from urllib.request import urlopen

data = urlopen("https://raw.githubusercontent.com/srinu5019/mypublicdata/master/Intents.txt").read().decode("utf-8") 
#data = open("static/intents.txt").read()
conversation = data.splitlines()
 
class ChatBot(object):
    convMap = {}
    """
    Allows the chat bot to be trained using data from the
    conversations above.
    """
    def __init__(self):
        self.convMap={}
    def train(self, conversation):
        index=1
        key=""
        value=""
        for line in conversation:
            if index%2 == 1:
                key = line
            else:
                value=line
            self.convMap[key]=value
            index += 1
    def get_response(self, key):
        presets = ["home","support","thanks"]
        if key in self.convMap.keys():
            if self.convMap[key] in presets:
                key = self.convMap[key]
            if key == "home" or key == "thanks":
                return "", self.convMap[key]
            else:
                return key, self.convMap[key]
        else:
            return "", ""

chatbot = ChatBot()
chatbot.train(conversation)
print (chatbot.convMap)