from skypebot import *

class Skype_Bot:
    """
    This class handles communication with Skype via SkypeBot
    """
    def __init__(self, plugins):
        self.skype = Skypebot.Skype(Events=self)
        self.skype.FriendlyName = "Skype Bot Levitan"
        self.skype.Attach()
        self.plugins = plugins

    def AttachmentStatus(self, status):
        if status == Skypebot.apiAttachAvailable:
            self.skype.Attach()

    def MessageStatus(self, msg, status):
        print("INCOMING> %s" % msg.Body)
        # msg.MarkAsSeen()
        if status == Skypebot.cmsReceived:
            for plugin in self.plugins:
                r = plugin.plugin_process_request(msg)
                if r['status']:
                    msg.Chat.SendMessage(r['message'])

    def send(self, topic, message):
        """
        Manual send to CONFERENCES to handle command line interface
        :param topic: topic of the conference (it's name)
        :param message: thing to say
        :return:
        """
        for chat in self.skype.Chats:
            if chat.Topic == topic:
                chat.SendMessage(message)
