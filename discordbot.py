# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging, os, asyncio
import time, fractions

### Cheat, how to make list comprehensions:
### [ expression for item in list if conditional ]

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
async def commandlog(ctx, newlog):
    t = time.asctime(time.gmtime())
    commandlog = open('logs/commandlogs/' + ctx.guild.name + ' ' + str(ctx.guild.id), 'a')
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
    if discord.utils.get(ctx.guild.roles, name='Administration') in ctx.author.roles:
        await commandlog(ctx, 'SUCCESS\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'User ' + str(member.name) + "#"+ str(member.discriminator) + ' was banished.')
        await ctx.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
    else:
        await commandlog(ctx, 'FAIL\t\tCommand "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
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
    # Do not forget to add a register over banned user IDs for unban.

#########################
######## unban ##########
### UNBAN FROM SERVER ###
#########################
@bot.command(name='unban')
async def _ban(ctx, *kwargs):
    await not_implemented(ctx, 'ban')

#################
##### rules #####
### GET RULES ###
#################
@bot.command(name='rules')
async def _rules(ctx, *kwargs):
    ruleprint = str()
    rules = list()
    for line in open('rulesfile', 'r'):
        # .rstrip() strips each line of a trailing linebreak.
        # When open() opens a textfile it escapes all \n (except actual
        # line breaks in the file), .replace() here unescapes them.
        rules.append(line.rstrip().replace('\\n', '\n'))

    if not kwargs:
        # If no arguments were specified the command will default to !rules help.
        kwargs = ('help',)

    # Recreating kwargs as a list
    kwargslist = []
    for i in kwargs:
        kwargslist.append(i)

    for i in range(len(kwargslist)):
        try:
            if kwargslist[i] == 'all' and kwargslist[i+1] == 'rules':
                kwargslist[i] = 'allrules'
                kwargslist.pop(i+1)
            elif kwargslist[i] == 'on' and kwargslist[i+1] == 'topic':
                kwargslist[i] = 'ontopic'
                kwargslist.pop(i+1)
            elif kwargslist[i] == 'be' and kwargslist[i+1] == 'nice':
                kwargslist[i] = 'benice'
                kwargslist.pop(i+1)
            elif kwargslist[i] == 'act' and kwargslist[i+1] == 'your' and kwargslist[i+2] == 'age':
                kwargslist[i] == 'actyourage'
                kwargslist.pop(i+1)
                kwargslist.pop(i+2)
        except IndexError:
            pass

    # This is the key for different aliases by which you can call the rules
    r_aliases = {
        1: ['1', 'topic', 'ontopic'],
        2: ['2', 'civil', 'behave'],
        3: ['3', 'dismissive'],
        4: ['4', 'jokes'],
        5: ['5', 'shoes', 'age', 'act', 'actyourage', 'actage'],
        6: ['6', 'spam'],
        7: ['7', 'benice', 'nice']
    }

    if 'allrules' in kwargslist:
        # If the command is run to show all rules we simply edit it to have called all rules.
        # It's cheating a bit, but it gets the job done.
        kwargslist = [ 1, 2, 3, 4, 5, 6, 7 ]

    # Using the dictionary r_aliases we will now replace the aliases by the correct rule number.
    for i in range(len(r_aliases)):
        rulenumber = i+1 # these are also the keys used in r_aliases
        for rulealias in r_aliases[rulenumber]: # rulealias is the entry, rulenumber is the key/rule number
            kwargslist = [ rulenumber if item == rulealias else item for item in kwargslist ]

    # Discord will remove trailing line breaks when posting ruleprint,
    # so we don't have to worry about adding too many.
    if 1 in kwargslist:
        ruleprint += rules[0] + '\n\n'
    if 2 in kwargslist:
        ruleprint += rules[1] + '\n\n'
    if 3 in kwargslist:
        ruleprint += rules[2] + '\n\n'
    if 4 in kwargslist:
        ruleprint += rules[3] + '\n\n'
    if 5 in kwargslist:
        ruleprint += rules[4] + '\n\n'
    if 6 in kwargslist:
        ruleprint += rules[5] + '\n\n'
    if 7 in kwargslist:
        ruleprint += rules[6] # This one will never require the extra line breaks

    if 'help' in kwargs:
        await ctx.channel.send('**Rules**\n' +
        'Full list of rules are available in ' + discord.utils.get(ctx.guild.channels, name='rules').mention + '.\n'
        'To use this command type !rules followed by the numbers of the rules you wish to have listed,' +
        'or the keyword for the desired rule.\n\n'
        )
        await commandlog(ctx, 'HELP\t\tCommand "rules" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))
        return

    # If the ruleprint is now empty we'll print a message and break off here
    if len(ruleprint) == 0:
        if len(kwargs) > 1:
            await ctx.channel.send(ctx.author.mention + ' None of those are real rules, you smud.')
        else:
            await ctx.channel.send(ctx.author.mention + ' That\'s not a real rule, you smud.')
        await commandlog(ctx, 'FAIL\t\tCommand "rules" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                        '\n\t\t\t\t\t' + 'None of the calls matched any rules: ' + str(kwargslist))
        return

    # Finally, we're ready to post
    await ctx.channel.send(ruleprint)
    await commandlog(ctx, 'SUCCESS\tCommand "rules" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                     '\n\t\t\t\t\t' + 'They called on rules: ' + str(kwargslist))

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

#######################
######## quote ########
### ADD/READ QUOTES ###
#######################
@bot.command(name='quote')
async def _quote(ctx, *kwargs):
    await not_implemented(ctx, 'quote')

###################
###### vote #######
### CALL A VOTE ###
###################
@bot.command(name='vote')
async def _vote(ctx, *kwargs):
    await not_implemented(ctx, 'region')

#######################
####### botnick #######
### CHANGE BOT NICK ###
#######################
@bot.command(name='vote')
async def _vote(ctx, *kwargs):
    await not_implemented(ctx, 'region')
# discord.ClientUser.display_name

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
        await commandlog(ctx, 'HELP\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))
        return

    elif len(kwargs) < 2:
        await ctx.channel.send('Hey there ' + ctx.author.mention + '! You need to specify both temperature and unit.\n' +
                               'Type !temp help for instructions.')
        await commandlog(ctx, 'FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
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
        await commandlog(ctx, 'FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + 'No unit specified.')
        return

    try:
        temp = float(temp)
    except ValueError:
        await ctx.channel.send('You need to specify temperature first and original unit afterwards.' +
                               'Type !temp help for instructions.')
        await commandlog(ctx, 'FAIL\t\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
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
        await commandlog(ctx, 'SUCCESS\tCommand "temp" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id) +
                         '\n\t\t\t\t\t' + str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!')

@bot.command(name='source')
async def _source(ctx, *kwargs):
    await ctx.channel.send('My source code is available at:\n' +
                           'https://github.com/kaminix/DrFreeze')
    await commandlog(ctx, 'SUCCESS\tCommand "source" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id))

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
try:
    token = open('token', 'r').read().strip()
    bot.run(token)
except:
    print ('\nERROR: BOT TOKEN MISSING\n' +
           'Please put your bot\'s token in a separate text file called \'token\'.\n' +
           'This file should be located in the same directory as the bot files.\n')
    exit()
