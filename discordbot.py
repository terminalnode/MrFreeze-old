# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging
import asyncio

bot = commands.Bot(command_prefix='!')

async def not_implemented(message, command):
    await message.channel.send(message.author.mention " The command '" + command "' isn't implemented yet. Try again some other time!")
    return

# This will be printed in the console once the
# bot has been connected to discord.
@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))
    print ('User name: ' + str(bot.user.name))
    print ('User ID: ' + str(bot.user.id))
    print ('-----------')

############################
########## banish ##########
### BANISH TO ANTARCTICA ###
############################
@bot.command()
async def banish(message, member: discord.Member):
    if discord.utils.get(message.guild.roles, name='Administration') in message.author.roles:
        print ('SUCCESS - Command "banish" issued by {0.author}, ID: '.format(message) + str(message.author.id))
        await message.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(message.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(message.guild.roles, name='Antarctica'))
    else:
        print ('FAIL - Command "banish" issued by {0.author}, ID: '.format(message) + str(message.author.id))
        await message.channel.send('Sorry ' + message.author.mention + ', you need to be a mod to do that.'.format(message))

#######################
######## ban ##########
### BAN FROM SERVER ###
#######################
@bot.command()
async def ban(message, member: discord.Member):
    not_implemented(message, 'ban')

########################
######### kick #########
### KICK FROM SERVER ###
########################
@bot.command()
async def kick(message, member: discord.Member):
    not_implemented(message, 'kick')

#################
##### mute ######
### MUTE USER ###
#################
@bot.command()
async def mute(message, member: discord.Member):
    not_implemented(message, 'mute')

#############################
########### rps #############
### ROCK, PAPER, SCISSORS ###
#############################
@bot.command()
async def rps(message, choice):
    not_implemented(message, 'rps')

##############################
######## temperature #########
### TEMPERATURE CONVERSION ###
##############################
@bot.command()
async def temperature(message, temp, unit):
    not_implemented(message, 'temperature)

# Log setup in accordance with:
# https://discordpy.readthedocs.io/en/rewrite/logging.html#logging-setup
# No one will ever read this...
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Client.run with the bots token
token = open('token', 'r').read().strip()
bot.run(token)
