# Discord bot by TerminalNode
import discord
from discord.ext import commands
import logging
import asyncio

bot = commands.Bot(command_prefix='!')

# This will be printed in the console once the
# bot has been connected to discord.
@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))
    print ('User name: ' + str(bot.user.name))
    print ('User ID: ' + str(bot.user.id))
    print ('-----------')


@bot.command()
async def banish(self, member: discord.Member):
    if discord.utils.get(self.guild.roles, name='Administration') in self.author.roles:
        print ('SUCCESS - Command "banish" issued by {0.author}, ID: '.format(self) + str(self.author.id))
        await self.channel.send(member.mention + ' will be banished to the frozen hells of Antarctica for 5 minutes!')
        await member.add_roles(discord.utils.get(self.guild.roles, name='Antarctica'))
        await asyncio.sleep(5*60)
        await member.remove_roles(discord.utils.get(self.guild.roles, name='Antarctica'))
    else:
        print ('FAIL - Command "banish" issued by {0.author}, ID: '.format(self) + str(self.author.id))
        await self.channel.send('Sorry ' + self.author.mention + ', you need to be a mod to do that.'.format(self))

#Experiments:
# print (type(member)) #discord.member.Member
#    print (type(self.author)) #discord.member.Member
#    print ('self: ' + str(self) + ', is type:\n' + str(type(self)))       ### context
#    print ('target: ' + str(target) + ', is type:\n' + str(type(target))) ### string
#    await self.add_roles()


#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#
#    else:
#        await message.channel.send(message.content + " :emoji:")

####
#@bot.event
#async def on_message_delete(message):
#        await message.channel.send("The following message was deleted:\n" + message.content)
####

# Log setup in accordance with:
# https://discordpy.readthedocs.io/en/rewrite/logging.html#logging-setup
# No one will ever read this...
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Client.run with the bots token
bot.run('NDY2MjM5OTU2NDgyOTE2MzUy.DiZOJQ._YlctLtAhweMWt6DRdcjT7JheZM')
