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

    def saveMembers(self, member_list):
        for sm in member_list:
            f = open("members/" + sm.discordID.id + ".pk", 'wb')
            pk = pickle.Pickler(f, 3)
            pk.dump(sm)
            f.close()
        return

    def loadMembers(self):
        member_list = []
        for filename in glob.glob('members/*.pk'):
            f = open(filename, 'rb')
            pk = pickle.Unpickler(f)
            sm = pk.load()
            member_list.append(sm)
            f.close()
        return member_list

    def getPlayerByDiscord(self, member: discord.Member, player_list):
        for player in player_list:
            if player.discordID == member:
                return player
        return None

    def getMembersInVoice(self, server, c_name="General"):
        for channel in server.channels:
            if channel.name == c_name:
                return channel
        return None

    def printPlayerRow(self, p):
        return '{:22.22}'.format(p.info['name']) +  \
                "  " + \
               '{:>4.4}'.format(str(p.info['sr'])) + \
                "  " + \
               '{:<10.10}'.format(p.info['role']) + \
                "  " + \
               '{:>30.30}'.format(p.info['heroes'])