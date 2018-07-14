# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging
import asyncio
import time

bot = commands.Bot(command_prefix='!')

###
### This will be used for functions which are planned
### for but not yet implemented to give users a heads up.
###
async def not_implemented(ctx, command):
    await ctx.channel.send(ctx.author.mention + " The command '" + command + "' isn't implemented yet. Try again some other time!")
    return

###
### This will be used to both print a message to the terminal
### as well as put it down in a log.
###
async def commandlog(newlog):
    t = time.asctime(time.gmtime())
    commandlog = open('commands.log', 'w')
    print (t + ' ' + newlog )
    print (t + ' ' + newlog, file=commandlog)
    commandlog.close()

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
async def banish(ctx, member: discord.Member):
    if discord.utils.get(ctx.guild.roles, name='Administration') in ctx.author.roles:
        await commandlog('SUCCESS\t Command "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))
        await ctx.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
    else:
        await commandlog('FAIL\t\t Command "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))
        await ctx.channel.send('Sorry ' + ctx.author.mention + ', you need to be a mod to do that.'.format(ctx))

#######################
######## ban ##########
### BAN FROM SERVER ###
#######################
@bot.command()
async def ban(ctx, member: discord.Member):
    await not_implemented(ctx, 'ban')

########################
######### kick #########
### KICK FROM SERVER ###
########################
@bot.command()
async def kick(ctx, member: discord.Member):
    await not_implemented(ctx, 'kick')

#################
##### mute ######
### MUTE USER ###
#################
@bot.command()
async def mute(ctx, member: discord.Member):
    await not_implemented(ctx, 'mute')

#############################
########### rps #############
### ROCK, PAPER, SCISSORS ###
#############################
@bot.command()
async def rps(ctx, choice):
    await not_implemented(ctx, 'rps')

##############################
######## temperature #########
### TEMPERATURE CONVERSION ###
##############################
@bot.command()
async def temperature(ctx, temp, unit):
    await not_implemented(ctx, 'temperature')

@bot.command()
async def source(ctx):
    await ctx.channel.send('''My source code is available at:
https://github.com/kaminix/DrFreeze''')

# Log setup in accordance with:
# https://discordpy.readthedocs.io/en/rewrite/logging.html#logging-setup
# No one will ever read this...
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Client.run with the bots token
# Place your token in a file called 'token'
# Put the file in the same directory as the bot.
token = open('token', 'r').read().strip()
bot.run(token)
