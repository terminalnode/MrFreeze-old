# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging, os
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
async def commandlog(newlog, guildname):
    t = time.asctime(time.gmtime())
    commandlog = open('logs/commandlogs/' + guildname, 'a')
    print (t + ' ' + newlog )
    commandlog.write(t + ' ' + newlog + '\n')
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
# Use this to create an error handler for bad arguments.
# https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
async def _banish(ctx, member: discord.Member):
    print(type(member))
    print(ctx.guild.name)
    if discord.utils.get(ctx.guild.roles, name='Administration') in ctx.author.roles:
        await commandlog('SUCCESS\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'User ' + str(member.name) + "#"+ str(member.discriminator) + ' was banished.', ctx.guild.name)
        await ctx.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
    else:
        await commandlog('FAIL\t\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'User did not have sufficient privilegies.' +
                         '\n\t\t\t\t\t' + 'They tried to banish: ' + str(member.name) + '#' + str(member.discriminator), ctx.guild.name)
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
    prevrule = False
    ruleprint = str()

    def checkprevrule():
        nonlocal prevrule
        nonlocal ruleprint
        if prevrule == True:
            ruleprint += '\n\n'

    if not kwargs:
        kwargs = ('help',)

    if 'help' in kwargs:
        ruleprint += ('**Rules**\n' +
        'Full list of rules are available in ' + discord.utils.get(ctx.guild.channels, name='rules').mention + '.\n'
        'To use this command type !rules followed by the numbers of the rules you wish to have listed,' +
        'or the keyword for the desired rule.\n' +
        '**Keywords:**\n\ntopic, ontopic, civil, dismissive, jokes, shoes, spam, benice, be nice, allrules, all rules'
        )
        return
    if 'allrules' in kwargs or
       'all' and 'rules' in kwargs:
        kwargs = ('1','2','3','4','5','6','7')
    if '1' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 1**\n' +
        'Keep things relevant to the channel you are participating in. ' +
        'It’s okay to be a bit off topic here and there, but it is important to ' +
        'realize and move to the proper channel to continue the conversation.')
        prevrule = True
    if '2' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 2**\n' +
        'Keep things civil. If there is a disagreement, stop when asked to stop.')
        prevrule = True
    if '3' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 3**\n' +
        'Do not be dismissive of others’ opinions.')
        prevrule = True
    if '4' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 4**\n' +
        'No joking based on what people cannot immediately change. ie no jokes on race, weight, sexual orientation.')
        prevrule = True
    if '5' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 5**\n' +
        'Act your age, not your shoe size. Unless of course, your shoe size is somehow above your age, in such cases, act your shoe size.')
        prevrule = True
    if '6' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 6**\n' +
        'No spamming the board.')
        prevrule = True
    if '7' in kwargs:
        checkprevrule()
        ruleprint += ('**Rule 7**\n' +
        'Be nice to everyone. Not following this rule will get you removed from the server quickly and effectively.')
        prevrule = True
    await ctx.channel.send(ruleprint)

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
        await commandlog('HELP\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id), ctx.guild.name)
        return

    elif len(kwargs) < 2:
        await ctx.channel.send('Hey there ' + ctx.author.mention + '! You need to specify both temperature and unit.\n' +
                               'Type !temp help for instructions.')
        await commandlog('FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'Invalid formatting, command requires at least two arguments.', ctx.guild.name)
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
                         '\n\t\t\t\t\t' + 'No unit specified.', ctx.guild.name)
        return

    try:
        temp = float(temp)
    except ValueError:
        await ctx.channel.send('You need to specify temperature first and original unit afterwards.' +
                               'Type !temp help for instructions.')
        await commandlog('FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                             '\n\t\t\t\t\t' + 'Invalid formatting, command requires an integer.', ctx.guild.name)
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
                         '\n\t\t\t\t\t' + str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!', ctx.guild.name)

@bot.command(name='source')
async def _source(ctx, *kwargs):
    await ctx.channel.send('My source code is available at:\n' +
                           'https://github.com/kaminix/DrFreeze')
    await commandlog('SUCCESS\tCommand "source" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id), ctx.guild.name)

# Log setup in accordance with:
# https://discordpy.readthedocs.io/en/rewrite/logging.html#logging-setup
# No one will ever read this...
if not os.path.exists('logs/commandlogs/'):
    os.makedirs('logs/commandlogs/')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/debug.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Client.run with the bots token
# Place your token in a file called 'token'
# Put the file in the same directory as the bot.
token = open('token', 'r').read().strip()
bot.run(token)
