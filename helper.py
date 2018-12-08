import pickle
import glob
import discord
from pprint import pprint

class Helper:
    def __init__(self):
        return

    def serializeMessage(self, message_list):
        s_line = ''
        for line in message_list:
            s_line = s_line + line + '\n'
        s_line = '```' + s_line + '```'
        return s_line

    def chunkMessage(self, message_list):
        chunkedMessage = []
        for chunk in self.chunks(message_list):
            chunkedMessage.append(self.serializeMessage(chunk))
        return chunkedMessage

    def chunks(self, l):
        for i in range(0, len(l), 20):
            yield l[i:i + 20]

    def formatMessage(self, message):
        return '`' + message + '`'


    def checkAdmin(self, discordRoles):
        for role in discordRoles:
            if role.permissions.administrator:
                return True
        return False

    def getMembersInVoice(self, server, c_name="General"):
        for channel in server.channels:
            if channel.name == c_name:
                return channel
        return None
