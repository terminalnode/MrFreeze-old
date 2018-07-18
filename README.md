# MrFreeze
This is a discord bot only meant for use on the The Penposium discord server, a discord server for fountain pens. It's made available here mainly for backup and versioning, but feel free to use this code or parts of it for your own bot if you find it useful. The reason for making this is simply that we couldn't find a pre-made bot that filled our needs.

If you have an interest in fountain pens and want to chat with likeminded people you're welcome to check our server out, it's available via this URL: [The Penposium discord server](https://discord.gg/khY7JYs). However as of writing this the bot is not yet deployed as it's still under construction. If you'd like to chat about the bot, you may join the discord server where all the testing is made instead. [Invite to MrFreezes Cave discord server](https://discord.gg/wcwshah).

## Instructions
This bot was tested in Python 3.6.5. It will not work in the latest Python version due to being dependent on discord.py (rewrite version), which isn't compatible with Python 3.7. The discord.py package is available through pip. The best way I've found of running an older version of Python is to set it up as a virtual environment in pyenv.

Not wanting to upload the token of my bot to github this is read from a separate text file called 'token' which you place in the same directory as the bot. If you don't do this however, it will produce an error message with instructions on how to set this up.

## Available commands
Below is a list of implemented and planned commands, as well as what I'm currently working on. (Owner) indicates that only I can do it, if you want to use the command you have to run a separate bot and edit the ID that is allowed to do it. (Mod) indicates that only mods are allowed to issue the command.

### Fully implemented (as far as I know)
* **!restart**  - (Owner) Restarts the bot completely. Very useful for testing new code.
* **!banish**   - (Mod) Assigns the tag 'Antarctica' to a user for five minutes.
* **!dmcl**     - (Mod) DM commandlog file for the current server to author.
* **!temp**     - Converts a temperature from fahrenheit to celcius and vice versa.
* **!rules**    - Displays one, several or all rules depending on how the command is executed.
* **!source**   - Posts a link to this github page.
* **!mrfreeze** - Posts a dank Mr. Freeze quote from Batman & Robin. Replaces 'Batman' with you and 'Gotham' with channel name.
* **!activity** - Changes the activity of the bot ('Playing [...]'). No mod requirement, have fun!
* **!region**   - Allows a user to assign a regional role such as continent (could also be used for countries).
* **!vote**     - Creates a vote where users vote by reacting with specified emoji. (works with server but not nitro emojis)

### Next up
* **!kick**     - (Mod) Kicks the user from the server.

### Planned but not yet implemented
* **!ban**      - (Mod) Bans the user from the server.
* **!unban**    - (Mod) Removes ban from the server.
* **!mute**     - (Mod) Mutes the user.
* **!botnick**  - (Mod) Changes the nick of the bot.
* **!quote**    - (Mod) Add, delete, and read random quotes.
* **!rps**      - Play rock, paper, scissors with the bot.
* **!dice**     - Roll a select number of dice. Intend to also implement option to select type of dice.
