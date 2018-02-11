import discord
from discord.ext import commands
import spookymember
import helper
import yaml


with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

description = 'Spooky bot is the admin bot for 2spooky server'
bot = commands.Bot(command_prefix='!', description=description)
helper = helper.Helper()
spooky_members = []


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    print('Loading discord members')
    spooky_members.extend(helper.loadMembers())
    print('SPOOKYBOT READY')

@bot.event
async def on_member_join(member):
    await bot.send_message(member, "Welcome to the 2spooky server, " + member.mention + "!")
    spooky_members.append(spookymember.SpookyMember(member))
    helper.saveMembers(spooky_members)

@bot.command(pass_context=True, description="Roll")
async def roll(ctx, *args):
    await bot.say("Rollin'")


bot.run(cfg['init']['token'])

