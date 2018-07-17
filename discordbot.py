# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging, os, asyncio, sys
import time, fractions, signal, random

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
### Returns True if the author is a mod, otherwise False
###
async def is_mod(ctx):
    return(discord.utils.get(ctx.guild.roles, name='Administration') in ctx.author.roles)

###
### Looks through config/files for URL of a picture matching the file name.
###
def get_image(desired):
    for i in open('config/files', 'r'):
        currentimage = i.strip().split(' ')

        if currentimage[0] == desired:
            return currentimage[1]
    return 'https://imgur.com/pgNlDLT' # This is the NoImage file

###
### This will be used to both print a message to the terminal
### as well as put it down in a log.
###
async def commandlog(ctx, log_category, used_command, *kwargs):
    commandlog = open('logs/cmd_' + ctx.guild.name + '_' + str(ctx.guild.id), 'a')

    # First we'll print the time and whether the command was successful or not.
    t = time.asctime(time.gmtime())
    if log_category == 'SUCCESS':
        logentry = t + ' SUCCESS\t'

    elif log_category == 'FAIL':
        logentry = t + ' FAIL\t\t'

    elif log_category == 'HELP':
        logentry = t + ' HELP\t\t'

    # Second part will be 1) who issued the command, 2) which command was it.
    # Command "banish" issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id)
    logentry += 'Command \'' + used_command + '\' issued by {0.author}, ID: '.format(ctx) + str(ctx.author.id)

    # For some commands a comment on what exactly happened is added to the log.
    # Each kwarg corresponds to one line, which will be one list entry in commentl.
    if len(kwargs) > 0:
        commentl = list()
        for i in range(len(kwargs)):
            logentry += '\n\t\t\t\t\t' + kwargs[i]

    print (logentry)
    commandlog.write(logentry + '\n')
    commandlog.close()

def mrfreezequote():
    mf_quotelist = []
    for i in open('config/mrfreezequotes', 'r'):
        mf_quotelist.append(i.strip())
    return random.choice(mf_quotelist)

# This will be printed in the console once the
# bot has been connected to discord.
@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))
    print ('User name: ' + str(bot.user.name))
    print ('User ID: ' + str(bot.user.id))
    print ('-----------')
    for i in bot.guilds:
        await i.system_channel.send(':wave: ' + mrfreezequote())

########## mrfreeze ###########
### PRINT A MR FREEZE QUOTE ###
###############################
@bot.command(name='mrfreeze')
async def _mrfreeze(ctx, *kwargs):
    if len(kwargs) == 0:
        await ctx.channel.send(mrfreezequote().replace('Batman', ctx.author.mention).replace('Gotham', ctx.channel.mention))
    elif 'help' in kwargs or 'what' in kwargs or 'wtf' in kwargs or 'explanation' in kwargs:
        await ctx.channel.send('*!mrfreeze* will post a dank Dr. Freeze quote from Batman & Robin. All instances of Batman are replaced with your name, and all instances of Gotham are replaced with the channel name.')
    elif 'sucks' in kwargs or 'suck' in kwargs:
        await ctx.channel.send(ctx.author.mention + ' No, *you* suck!')
    else:
        await ctx.channel.send('No, bad ' + ctx.author.mention + '!\nType only *!mrfreeze* for dank Mr. Freeze quotes, or *!mrfreeze* what for an explanation.')

    if len(kwargs) == 0:
        await commandlog(ctx, 'SUCCESS', 'MRFREEZE')
    else:
        await commandlog(ctx, 'SUCCESS', 'MRFREEZE', ('Arguments used: ' + str(kwargs)))

########## banish ##########
### BANISH TO ANTARCTICA ###
############################
@bot.command(name='banish')
# Use this to create an error handler for bad arguments.
# https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
async def _banish(ctx, member: discord.Member):
    if await is_mod(ctx):
        await commandlog(ctx, 'SUCCESS', 'BANISH', ('User ' + str(member.name) + "#"+ str(member.discriminator) + ' was banished.'))
        await ctx.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
    else:
        await commandlog(ctx, 'FAIL', 'BANISH',
                        ('User did not have sufficient privilegies to banish ' + str(member.name) + '#' + str(member.discriminator)))

        await ctx.channel.send('You\'re not  allowed to banish people ' +
                               ', you will now be banished for your transgressions.'.format(ctx) +
                               '\n' + ctx.author.mention + ' will be banished to the frozen hells of Antarctica for 7 minutes!')

        await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60) # 5*60 seconds = 5 minutes
        await ctx.author.remove_roles(discord.utils.get(ctx.guild.roles, name='Antarctica'))

######## ban ##########
### BAN FROM SERVER ###
#######################
@bot.command(name='ban')
async def _ban(ctx, *kwargs):
    await not_implemented(ctx, 'ban')
    # Do not forget to add a register over banned user IDs for unban.

######## unban ##########
### UNBAN FROM SERVER ###
#########################
@bot.command(name='unban')
async def _ban(ctx, *kwargs):
    await not_implemented(ctx, 'ban')

####### restart #######
### RESTART THE Bot ###
#######################
@bot.command(name='restart')
async def _restart(ctx, *kwargs):
    if ctx.author.id == 154516898434908160: # This is my discord user ID. If you're modifying this, change to your ID.
        await ctx.channel.send(ctx.author.mention + " Yes boss... I will restart now.")
        await commandlog(ctx, 'SUCCESS', 'RESTART')
        print ('\n') # extra new line after the commandlog() output
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await ctx.channel.send(ctx.author.mention + " You're not the boss of me, I restart when Terminal wants me to.")
        await commandlog(ctx, 'FAIL', 'RESTART')

##### rules #####
### GET RULES ###
#################
@bot.command(name='rules')
async def _rules(ctx, *kwargs):
    ruleprint = str()
    rules = list()
    for line in open('config/rulesfile', 'r'):
        # .rstrip() strips each line of a trailing linebreak.
        # When open() opens a textfile it escapes all \n (except actual
        # line breaks in the file), .replace() here unescapes them.
        rules.append(line.rstrip().replace('\\n', '\n'))

    if not kwargs:
        # If no arguments were specified the command will default to !rules help.
        kwargs = ('help',)

    # Recreating kwargs as a list
    kwargsl = []
    for i in kwargs:
        kwargsl.append(i)

    for i in range(len(kwargsl)):
        try:
            if kwargsl[i] == 'all' and kwargsl[i+1] == 'rules':
                kwargsl[i] = 'allrules'
                kwargsl.pop(i+1)
            elif kwargsl[i] == 'on' and kwargsl[i+1] == 'topic':
                kwargsl[i] = 'ontopic'
                kwargsl.pop(i+1)
            elif kwargsl[i] == 'be' and kwargsl[i+1] == 'nice':
                kwargsl[i] = 'benice'
                kwargsl.pop(i+1)
            elif kwargsl[i] == 'act' and kwargsl[i+1] == 'your' and kwargsl[i+2] == 'age':
                kwargsl[i] == 'actyourage'
                kwargsl.pop(i+1)
                kwargsl.pop(i+2)
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

    if 'allrules' in kwargsl:
        # If the command is run to show all rules we simply edit it to have called all rules.
        # It's cheating a bit, but it gets the job done.
        kwargsl = [ 1, 2, 3, 4, 5, 6, 7 ]

    # Using the dictionary r_aliases we will now replace the aliases by the correct rule number.
    for i in range(len(r_aliases)):
        rulenumber = i+1 # these are also the keys used in r_aliases
        for rulealias in r_aliases[rulenumber]: # rulealias is the entry, rulenumber is the key/rule number
            kwargsl = [ rulenumber if item == rulealias else item for item in kwargsl ]

    # Discord will remove trailing line breaks when posting ruleprint,
    # so we don't have to worry about adding too many.
    if 1 in kwargsl:
        ruleprint += rules[0] + '\n\n'
    if 2 in kwargsl:
        ruleprint += rules[1] + '\n\n'
    if 3 in kwargsl:
        ruleprint += rules[2] + '\n\n'
    if 4 in kwargsl:
        ruleprint += rules[3] + '\n\n'
    if 5 in kwargsl:
        ruleprint += rules[4] + '\n\n'
    if 6 in kwargsl:
        ruleprint += rules[5] + '\n\n'
    if 7 in kwargsl:
        ruleprint += rules[6] # This one will never require the extra line breaks

    if 'help' in kwargs:
        await ctx.channel.send('**Rules**\n' +
        'Full list of rules are available in ' + discord.utils.get(ctx.guild.channels, name='rules').mention + '.\n'
        'To use this command type !rules followed by the numbers of the rules you wish to have listed,' +
        'or the keyword for the desired rule.\n\n'
        )
        await commandlog(ctx, 'HELP', 'RULES')
        return

    # If the ruleprint is now empty we'll print a message and break off here
    if len(ruleprint) == 0:
        if len(kwargs) > 1:
            await ctx.channel.send(ctx.author.mention + ' None of those are real rules, you ignorant smud.')
            print('uhh')
        else:
            await ctx.channel.send(ctx.author.mention + ' That\'s not a real rule, you ignorant smud.')

        await commandlog(ctx, 'FAIL', 'RULES',
                        ('None of the calls matched any rules: ' + str(kwargsl)))
        return

    # Finally, we're ready to post
    await ctx.channel.send(ruleprint)
    await commandlog(ctx, 'SUCCESS', 'RULES',
                     ('They called on rules: ' + str(kwargsl)))

######### kick #########
### KICK FROM SERVER ###
########################
@bot.command(name='kick')
async def _kick(ctx, member: discord.Member):
    await not_implemented(ctx, 'kick')

##### mute ######
### MUTE USER ###
#################
@bot.command(name='mute')
async def _mute(ctx, *kwargs):
    await not_implemented(ctx, 'mute')

########### rps #############
### ROCK, PAPER, SCISSORS ###
#############################
@bot.command(name='rps')
async def _rps(ctx, *kwargs):
    await not_implemented(ctx, 'rps')

###### region #######
### SELECT REGION ###
#####################
@bot.command(name='region')
async def _region(ctx, *kwargs):
    await not_implemented(ctx, 'region')

######## quote ########
### ADD/READ QUOTES ###
#######################
@bot.command(name='quote')
async def _quote(ctx, *kwargs):
    await not_implemented(ctx, 'quote')

###### vote #######
### CALL A VOTE ###
###################
@bot.command(name='vote')
async def _vote(ctx, *kwargs):
    await not_implemented(ctx, 'region')

####### botnick #######
### CHANGE BOT NICK ###
#######################
@bot.command(name='botnick')
async def _botnick(ctx, *kwargs):
    newnick = str()
    for i in range(len(kwargs)):
        if i != 0:
            newnick += ' '
        newnick += kwargs[i]
    if len(newnick) <= 32:
        if await is_mod(ctx):
            await ctx.ClientUser.edit(nick = newnick)
            await ctx.channel.send(ctx.author.mention + ' Yes my lord, I will henceforth be known by the name of \'' + newnick + '\'.')
            await commandlog(ctx, 'SUCCESS', 'BOTNICK', ('Bot nick was changed to: ' + newnick))
        else:
            await ctx.channel.send(ctx.author.mention + ' Smuds like you aren\'t allowed to change my nick.')
            await commandlog(ctx, 'FAIL', 'BOTNICK', 'Insufficient privilegies.')
    else:
        await ctx.channel.send(ctx.author.mention + ' that nick is too damn long.')
        await commandlog(ctx, 'FAIL', 'BOTNICK', 'Suggested nick is too long.')

############ temp ############
### TEMPERATURE CONVERSION ###
##############################
@bot.command(name='temp')
async def _temp(ctx, *kwargs):
    # Check if we have any kwargs
    if not kwargs:
        kwargs = ('help',)

    if kwargs[0] == 'help':
        # TODO Write better help message
        await ctx.channel.send('**Example usage:**\n' +
                               '!temp 50 C or !temp 50 F')
        await commandlog(ctx, 'HELP', 'TEMP')
        return

    elif len(kwargs) < 2:
        await ctx.channel.send('Hey there ' + ctx.author.mention + '! You need to specify both temperature and unit.\n' +
                               'Type !temp help for instructions.')
        await commandlog(ctx, 'FAIL', 'TEMP', 'Invalid formatting, command requires at least two arguments.')
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
        await commandlog(ctx, 'FAIL', 'TEMP', 'No unit specified.')
        return

    try:
        temp = float(temp)
    except ValueError:
        await ctx.channel.send(ctx.author.mention + ' You didn\'t specify a value for the temperature you wanted me to convert.\n' +
                               'Type !temp help for instructions.')
        await commandlog(ctx, 'FAIL', 'TEMP', 'Invalid formatting, command requires an integer.')
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

        # This is the message we will print:
        full_temp_message = (ctx.author.mention + ' ' + str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!')

        # At this point, we're adding a small gif of a dog saying Welcome to Hell
        # If the temperature in celcius is above a certain threshold.
        hell_threshold = 35
        above_threshold = False
        if (t_origin == ' °C' and temp >= hell_threshold) or (t_origin == ' °F' and newtemp >= hell_threshold):
            above_threshold = True

        # Finally, we're ready to print the message:
        if above_threshold == True:
            image = discord.Embed().set_image(url=get_image('WelcomeToHell'))
            await ctx.channel.send(full_temp_message, embed=image)
            await commandlog(ctx, 'SUCCESS', 'TEMP', (str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!' +
                            ' Hell dog awoken.'))
        else:
            await ctx.channel.send(full_temp_message)
            await commandlog(ctx, 'SUCCESS', 'TEMP', (str(temp) + t_origin + ' is ' + str(newtemp) + t_target + '!'))

@bot.command(name='source')
async def _source(ctx, *kwargs):
    await ctx.channel.send('My source code is available at:\n' +
                           'https://github.com/kaminix/DrFreeze')
    await commandlog(ctx, 'SUCCESS', 'SOURCE')

# Log setup in accordance with:
# https://discordpy.readthedocs.io/en/rewrite/logging.html#logging-setup
# No one will ever read this...
if not os.path.exists('logs/'):
    os.makedirs('logs/')
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
    sys.exit(0)

# Graceful exit
def signal_handler(sig, frame):
        print('\n\nYou pressed Ctrl+C!\nI will now do like the tree, and get out of here.')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.pause()
