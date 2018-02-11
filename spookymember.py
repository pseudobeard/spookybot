import discord

class SpookyMember:
    def __init__(self, did: discord.Member):
        self.info = {}
        self.discordID = did
        self.info['name'] = self.discordID.name
        self.characters = []