#!/usr/bin/python3
import discord
from discord.ext import commands
from collections import deque
import helper
import spookyStats
import yaml
import pickle


with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

with open("spookyStats.pk", 'rb') as pfile:
    pk = pickle.Unpickle(pfile)
    spookyStats = pk.load()

description = 'Spooky bot is the admin bot for 2spooky server'
bot = commands.Bot(command_prefix='sb ', description=description)
helper = helper.Helper()
spookyStats = spookyStats.spookyStats()
spooky_members = []
illegal_roles = []

@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    for server in bot.servers:
        for role in server.roles:
            if role.name == "Illegal":
                illegal_roles.append(role)
    print('SPOOKYBOT READY')


@bot.command(pass_context=True, description="Stats")
async def stats(ctx, *args):
    print("Triggered Stats command")
    await bot.say("You are responsible for " + str(spookyStats.getStatsPerAuthor(ctx.message.author)) + " messages")
    

@bot.event
async def on_message(message):
    #First we check if this is a command, and if so run that
    await bot.process_commands(message)
    spookyStats.ingestMessage(message)
    if len(message.content) == 100:
        response = "100 character messages are illegal"
        for role in illegal_roles:
            if role.server == message.server:
                await bot.add_roles(message.author, role)
        await bot.send_message(message.channel, response)

bot.run(cfg['init']['token'])
