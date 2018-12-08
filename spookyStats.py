import discord

class spookyStats:
    def __init__(self):
        self.members = []
        self.messages = []
        return
    
    def ingestMessage(self, message: discord.Message):
        if message.author not in self.members:
            self.members.append(message.author)
        self.messages.append(message)
        return

    def getStatsPerAuthor(self, author: discord.Member):
        count = 0
        for message in self.messages:
            if message.author == author:
                count = count + 1
        return count
