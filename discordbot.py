# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging
import asyncio
import time
import fractions, decimal

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
@bot.command(name='banish')
async def _banish(ctx, member: discord.Member):
    if discord.utils.get(ctx.guild.roles, name='Administration') in ctx.author.roles:
        await commandlog('SUCCESS\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'User ' + str(member.name) + "#"+ str(member.discriminator) + ' was banished.')
        await ctx.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
    else:
        await commandlog('FAIL\t\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'User did not have sufficient privilegies.' +
                         '\n\t\t\t\t\t' + 'They tried to banish: ' + str(member.name) + '#' + str(member.discriminator))
        await ctx.channel.send('Sorry ' + ctx.author.mention + ', you need to be a mod to do that.'.format(ctx))

#######################
######## ban ##########
### BAN FROM SERVER ###
#######################
@bot.command(name='ban')
async def _ban(ctx, *kwargs):
    await not_implemented(ctx, 'ban')

#################
##### rules #####
### GET RULES ###
#################
@bot.command(name='rules')
async def _rules(ctx, *kwargs):
    await not_implemented(ctx, 'ban')

########################
######### kick #########
### KICK FROM SERVER ###
########################
@bot.command(name='kick')
async def _kick(ctx, member: discord.Member):
    await not_implemented(ctx, 'kick')

#################
##### mute ######
### MUTE USER ###
#################
@bot.command(name='mute')
async def _mute(ctx, *kwargs):
    await not_implemented(ctx, 'mute')

#############################
########### rps #############
### ROCK, PAPER, SCISSORS ###
#############################
@bot.command(name='rps')
async def _rps(ctx, *kwargs):
    await not_implemented(ctx, 'rps')

#####################
###### region #######
### SELECT REGION ###
#####################
@bot.command(name='region')
async def _region(ctx, *kwargs):
    await not_implemented(ctx, 'region')

###################
###### vote #######
### CALL A VOTE ###
###################
@bot.command(name='vote')
async def _vote(ctx, *kwargs):
    await not_implemented(ctx, 'region')

##############################
############ temp ############
### TEMPERATURE CONVERSION ###
##############################
@bot.command(name='temp')
async def _temp(ctx, *kwargs):
    # Check if we have any kwargs
    if not kwargs:
        kwargs = ('help',)

    if kwargs[0] == 'help':
        await ctx.channel.send('**Example usage:**\n' +
                               '!temp 50 C or !temp 50 F')
        await commandlog('HELP\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))
        return

    elif len(kwargs) < 2:
        await ctx.channel.send('Hey there ' + ctx.author.mention + '! You need to specify both temperature and unit.\n' +
                               'Type !temp help for instructions.')
        await commandlog('FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'Invalid formatting, command requires at least two arguments.')
        return

    else:
        pass

    if kwargs[0].lower() == 'c' or kwargs[0].lower() == 'f':
        # First argument is the unit
        temp = kwargs[1]
        unit = kwargs[0].lower()
    elif kwargs[1].lower() == 'c' or kwargs[1].lower() == 'f':
        # Second argument is the unit
        temp = kwargs[0]
        unit = kwargs[1].lower()
    else:
        await ctx.channel.send('Hey there ' + ctx.author.mention + '! You forgot to specify a unit.\n' +
                               'Valid units are C for celcius and F for Fahrenheit.\n' +
                               'Type !temp help for instructions.')
        await commandlog('FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'No unit specified.')
        return

    try:
        temp = float(temp)
    except ValueError:
        await ctx.channel.send('You need to specify temperature first and original unit afterwards.' +
                               'Type !temp help for instructions.')
        await commandlog('FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                             '\n\t\t\t\t\t' + 'Invalid formatting, command requires an integer.')
        return
    else:
        if unit == 'c':
            # [°F] = [°C] × ​9⁄5 + 32
            newtemp = temp * fractions.Fraction(9, 5) + 32
            t_origin = ' °C'
            t_target = ' °F'
        elif unit == 'f':
            # [°C] = ([°F] − 32) × ​5⁄9
            newtemp = (temp - 32) * fractions.Fraction(5, 9)
            t_origin = ' °F'
            t_target = ' °C'
        newtemp = float(newtemp) # ensures that the number isn't a fraction
        newtemp = round(newtemp,2) # rounds to two decimal points
        await ctx.channel.send(ctx.author.mention + ' ' + str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!' )
        await commandlog('SUCCESS\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!' )

@bot.command(name='source')
async def _source(ctx, *kwargs):
    await ctx.channel.send('My source code is available at:\n https://github.com/kaminix/DrFreeze')
    await commandlog()

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
