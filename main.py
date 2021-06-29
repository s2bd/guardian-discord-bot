# 𝗠𝗨𝗫𝗕𝗢𝗧 (𝗠𝗨𝗞𝗧𝗢) 𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗕𝗢𝗧 - 𝗢𝗥𝗜𝗚𝗜𝗡𝗔𝗟 𝗦𝗢𝗨𝗥𝗖𝗘
# @author dmimukto 2021
# @credits Replit's Discord Bot template, Stack Overflow, Cisc0-gif (https://github.com/Cisc0-gif/Discord-Bot-Template/blob/a53aad3ae91ed02d6f99a97328e1d9e4a9cc4a17/bot.py)
# @license MIT License (https://github.com/dmimukto/Muxbot/blob/main/LICENSE)
# @copyright Asenturisk Corporation 2021


# Importing the necessary modules for booting up and running the bot.
import discord
import os
import sys
import time
import discord.ext
import random
import requests
import urllib
import json
import logging
import datetime
import asyncio
from collections import Counter
import platform
from keep_alive import keep_alive

# Placed a control variable (constant) up here, so that I don't have to scroll down everytime.
# Keep this turned to True if you want the bot to auto-delete messages containing blacklisted words. And set it to False if you really love profanity.
BLACKLIST_MODE = True

# Further imports for running extra features from discord.py and python itself
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

# Defining the variable "client" as discord.Client() (So that I don't have to write discord.Client() everytime. C'mon! If you're reading this, you're definitely a programmer so you should understand the usual etiquettes and shortcuts we use!)
client = discord.Client()
# Here's where you can customize the bot's prefix. Since this is the pure source from a running version of Muxbot (Mukto : https://mukto.live/), the default prefix is "mux" followed by a whitespace.
client = commands.Bot(command_prefix = 'mux, ')

# If you're running your bot on Replit (which I myself used and greatly recommend), you can set up private variables from the sidebar. Elsewhere, you usually create a ".env" file in the directory.
# In that .env file, you just add in a single line "TOKEN = 897wr8iuaf09fWhateverYourTokenIs244324"
TOKEN = os.getenv("TOKEN")


"""
=======================================[    𝐂𝐥𝐢𝐞𝐧𝐭 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬    ]======================================
"""
# Assuming you are already familiar with the official Discord.py API (https://discordpy.readthedocs.io/en/stable/api.html), you should know the basics about client.event and client.command functions.
                                                    
# These are variables linked to some promotional images for Muxbot.
MUXBOT_01 = "https://media.discordapp.net/attachments/816302805560066069/856057289043607562/muktodiscbot.png?width=1101&height=231"
MUXBOT_02 = "https://media.discordapp.net/attachments/816302805560066069/856057306504233010/muxbot_banner.png?width=1101&height=348"

# This is a fairly basic command that greets new users of this on Discord. This is not automated yet, so you manually have to type "mux, greet" into the chat.
# I'm not explaining every single statement for this function.
@client.command()
async def greet(ctx):
  """| Greets new users and the bot introduces himself"""
  await ctx.send(MUXBOT_01)
  await ctx.send("""
**Behold, the Mux bot!**
  
Ahoy there! I'm Mukto, the virtual projection of Dewan Mukto's heart, mind and soul.
Right now, I am not as capable as I was planned to be. 
But hopefully in the upcoming days, I shall be stronger and more powerful.
  
For now, allow me to protect your server from profanity and NSFW materials. Just grant me the role with the permission to 'Manage Messages'. Or better still, give me an administrator role.
  
I hope I can serve ya well, pal. 😎👌
  
  """)
  await ctx.send(MUXBOT_02)
  await ctx.send("```version 0.1.9 early access```")

# Another basic command, but slightly more useful than the previous 'promotional' one
@client.command()
async def choose(ctx, *choices: str):
    """| Chooses between multiple words provided, seperated by spaces."""
    await ctx.send(random.choice(choices))

# This is an annoying command that is better kept a secret than a publicly accessible one
@client.command()
async def ping(ctx):
    """| Testing command"""
    await ctx.send("""No, I won't ping @everyone .""")
    await ctx.send("(Heheh, I just did. 😈)")

# A mimicry command that requires BLACKLIST_MODE to be turned ON.
@client.command()
async def muxsays(ctx, *, arg):
  "| Copies message and tells it via his message"
  copythat = discord.utils.escape_mentions(arg)
  await ctx.send(copythat)

@client.command()
async def ecoji(ctx, limit):
    "| Testing a new plugin for Automata on Muxbot"
     Sends randomly generated emojis from Jack Harrhy's Ecoji project
    ecojiSrc = "https://jackharrhy.dev/urandom/ecoji/"+str(limit)
    ecojiTxt = urllib.request.urlopen(ecojiSrc)
    for row in ecojiTxt:
      ecojiRows = row.decode("utf-8")
      await ctx.send(ecojiRows)

# A standard command that every moderator or administrator loves
@client.command()
async def kick(ctx, member : discord.Member):
    """| Kicks a member. Don't try this!"""
    try:
        await member.kick(reason=None)
        await ctx.send("🦵 Get lost, "+member.mention) # Kickee kickee, heheee XD
    except:
        await ctx.send("""Why should I? 🤷‍♂️""") # Something went wrong

# Another useful command.
@client.command()
async def warn(ctx, member : discord.Member, reason="No reason"):
    """| Warns a member for doing something wrong."""
    if reason == "No reason":
      # It sends a warning in the server's channel
      await ctx.send(">>> "+member.mention+" has been warned")
      # It also sends the warning in the particular violator's DMs (direct messages)
      await message.author.send("Yo "+str(message.author)+".")
      await message.author.send("You have been warned.")
      await message.author.send("Be careful. Or else, punishments will be severe. 😈")
    elif reason != "No reason":
      # Same things happen, except this time, the reason for the warning has been mentioned, too.
      await ctx.send(">>> "+member.mention+" has been warned, for"+str(reason))
      await message.author.send("Yo "+str(message.author)+".")
      await message.author.send("You have been warned for"+str(reason))
      await message.author.send("Be careful. Or else, punishments will be severe. 😈")



# Logging system for recording bot metrics and stats (OPTIONAL)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

# Logging system for recording server messages (OPTIONAL)
def logwrite(msg, server):
  with open('Serverwise/'+str(server)+'_MESSAGES.log', 'a+') as f:
    f.write(msg + '\n')
  f.close()

# Logging system for recording bug reports and suggestions (OPTIONAL)
def bugwrite(msg):
  with open('reports.log', 'a+') as buglog:
    buglog.write(msg + '\n')
  buglog.close()


  
"""
=======================================[    𝐂𝐥𝐢𝐞𝐧𝐭 𝐞𝐯𝐞𝐧𝐭𝐬   ]======================================
"""
# Assuming you are already familiar with the official Discord.py API (https://discordpy.readthedocs.io/en/stable/api.html), you should know the basics about client.event and client.command functions.

@client.event
# This function runs whenever your bot is booted up and is ready to roll!
async def on_ready():
  # You may uncomment and place in one of the following 'activity statuses' for the bot.
  # By default, Muxbot runs a 'streaming' status and it is connected to my Twitch URL. (Speaking of which, follow the link and check me out please!)
  twitch_url = 'https://twitch.tv/dukemantwo'
  await client.change_presence(activity=discord.Streaming(name="DukeManTwo", url=twitch_url))
                                                    
                                                    
                                                    
# ⊱ ──────────────────────── {.⋅ ✯ ⋅.} ──────────────────────── ⊰ #
# Set`Playing ` status
#await client.change_presence(activity=discord.Game(name="add your game))

# Set`Streaming ` status
#await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Set`Listening ` status
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Set `Watching ` status
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
# ⊱ ──────────────────────── {⋅. ✯ .⋅} ──────────────────────── ⊰ #

                                                    
  # The following wordmark is for decorative purposes only. Please remove it since you are not hosting the Mukto bot nor the Muxbot 'as is'.
  print("""
                                                 .-'''-.     
                                                '   _    \   
 __  __   ___                 .               /   /` '.   \  
|  |/  `.'   `.             .'|              .   |     \  '  
|   .-.  .-.   '          .'  |           .| |   '      |  ' 
|  |  |  |  |  |         <    |         .' |_\    \     / /  
|  |  |  |  |  |  _    _  |   | ____  .'     |`.   ` ..' /   
|  |  |  |  |  | | '  / | |   | \ .' '--.  .-'   '-...-'`    
|  |  |  |  |  |.' | .' | |   |/  .     |  |                 
|__|  |__|  |__|/  | /  | |    /\  \    |  |                 
               |   `'.  | |   |  \  \   |  '.'               
               '   .'|  '/'    \  \  \  |   /                
                `-'  `--''------'  '---'`'-'                  """)
  print('---------------------------------------------------------------------')
  print('')
  print('https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=' + str(client.user.id))
  print('--------------------------------------------------------------------------')
  print('Logged in as:')
  print("Username : "+str(client.user.name)+" a.k.a. "+str(client.user)+" with ID : "+str(client.user.id))
  print('╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮')
  print(" LIVE CHAT LOG - See the Serverwise Logs For Details ")
  print("╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")

# End of on_ready()


# This event
@client.event
async def on_member_join(member):
  server = member.guild
  print("Member:", member, "joined!")
  logwrite("Member: " + str(member) + " joined!", server)

@client.event
async def on_member_remove(member):
  server = member.guild
  print("Member:", member, "removed!")
  logwrite("Member: " + str(member) + " removed!", server)

@client.event
async def on_guild_role_create(role):
  server = role.guild
  print("Role:", role, "was created!")
  logwrite("Role: " + str(role) + " was created!", server)

@client.event
async def on_guild_role_delete(role):
  server = role.guild
  print("Role:", role, "was deleted!")
  logwrite("Role: " + str(role) + " was deleted!", server)

@client.event
async def on_guild_channel_create(channel):
  server = channel.guild
  print("Channel:", channel, "was created!")
  logwrite("Channel: " + str(channel) + " was created!", server)

@client.event
async def on_guild_channel_delete(channel):
  server = channel.guild
  print("Channel:", channel, "was deleted!")
  logwrite("Channel: " + str(channel) + " was deleted!", server)

@client.event
async def on_guild_channel_update(before, after):
  server = after.guild
  print("Channel Updated:", after)
  logwrite("Channel Updated: " + str(after), server)

@client.event
async def on_message(message):
  # First up, set up the conditions that the bot ignores whatever it says, otherwise there could be an infinite loop
  if message.author == client.user:
    return 
  channel = message.channel
  try:
    server = channel.guild
  except:
    # If the messages are sent in the direct messaging inbox of the bot, then they are stored seperately in the logging directory
    print("Message sent in DMs")
    server = '_privatemsg_'
  print(message.author, "said:", message.content, "-- Time:", time.ctime()) #reports to discord.log and live chat
  logwrite(str(message.author) + " said: " + str(message.content) + "-- Time: " + time.ctime(), server)


# Muxbot's defensive system against profanity/blacklisted words

  if BLACKLIST_MODE:
      blackList = [] # Add your own set of blacklisted words into this list.

      insultworthy = [] # Additional list of blacklisted words if the previous one fails to detect any.
      # The list below is a default set of insults that Muxbot himself sends to counter the offenders. They have been directed at youngsters.
      insults = ["How would you feel if your profile showed up in the dark web tonight?","Mind your manners, kid. Or else the consequences will be worse than revealing your browsing history to your parents.","Got your data recorded. What're ya gonna do now? Go ahead, kick me. Your data remains with me. FOREVER.","Watch your tongue. You don't wanna mess with me. 'Cause I can track your IP, store your ID, and play pranks on ya in real life. For the rest of your unworthy life.","You certainly show what your parents taught ya. I dunno who should be sorry - you or your parents.","One wrong move, and I'm gonna send local thugs after you.","I'm gonna crack your balls and cook omellettes with it.","I'm gonna do the Fukouna Shoujo thing to you.","Lol. You cheated, so did I!","Got your data recorded. What're ya gonna do now? Go ahead, kick me. Your data remains with me. FOREVER.","I will pray for you to go to Hell.","The world is not meant for people like you. Go run to your parents' lap and cry!","You're a disgrace to your religion.","Look at you, sending NSFW words and content. I hope you wouldn't mind if I send people to do them practically to you.", "Your brain called me last night. It wants a divorce. Go crack your skull, you degenerate creep! Atleast your brain will have some peace.","Nope. You can't do this here.", "Bad luck.", "Peace be upon your sad life.","Oh, is that the best word you know?","You know, I can be a better racist, human.","تَبَّتْ يَدَآ أَبِى لَهَبٍ وَتَبَّ","Got the guts, huh? Lemme warn ya in advance, in case you don't piss your pants, you overgrown speck of meat! I'll teach ya proper manners today.","By the time you've even finished reading this message, your data is halfway across the Pacific. So start praying to your God. I doubt He'll want to protect you because of the sick stench of sin.","Still you wanna humiliate yourself further? Go ahead and hit a thumbs up if you're even worthy of an average life, sucker.","Got your data recorded. What're ya gonna do now? Go ahead, kick me. Your data remains with me. FOREVER."]
      
      # This section of code runs if it finds any direct blacklisted words in the chat
      if any(word in message.content.lower() for word in blackList):
          try:
            await message.delete()
          except:
            print("Either msg is in DM or something went wrong.")
            await message.add_reaction('<:kgm_angry:850398050358132756>') # An emoji from KoGaMa (https://kogama.com), utilized in a Discord server for reference

      # This section of code runs if anyone tries to cheat the auto-detection system, e.g. by adding in lots of spaces or dots or other symbols to bypass Muxbot's sensitivity
      if len(message.content.lower().replace(" ","")) <=6 and any(word in message.content.lower().replace(" ","") for word in insultworthy):
        dice = random.randint(0,len(insults)-1)
        choice = insults[dice]
        try:
          await message.delete()
        except:
          print("Something went wrong while trying to delete a msg.")
          await message.add_reaction('<:kgm_angry:850398050358132756>')
        await channel.send(choice)
        if dice // 2 == 0:
          await message.author.send('**Say cheese, ' + str(message.author) + '**')
          await asyncio.sleep(3)
          await message.author.send('This will go to the database records.')
          await asyncio.sleep(5)
          await message.author.send("I'll be sure to send a copy to your parents. 😈")

      elif any(word in message.content.strip() for word in insultworthy):
        dice = random.randint(0,len(insults)-1)
        choice = insults[dice]
        try:
          await message.delete()
        except:
          print("Something went wrong while trying to delete a msg.")
          await message.add_reaction('<:kgm_angry:850398050358132756>')
        await channel.send(choice)
        if dice // 2 == 0:
          await message.author.send('**Say cheese, ' + str(message.author) + '**')
          await asyncio.sleep(3)
          await message.author.send('This will go to the database records.')
          await asyncio.sleep(5)
          await message.author.send("I'll be sure to send a copy to your parents. 😈")

      elif any(word in message.content.replace(".","") for word in insultworthy):
        dice = random.randint(0,len(insults)-1)
        choice = insults[dice]
        try:
          await message.delete()
        except:
          print("Something went wrong while trying to delete a msg.")
          await message.add_reaction('<:kgm_angry:850398050358132756>')
        await channel.send(choice)
        if dice // 2 == 0:
          await message.author.send('**Say cheese, ' + str(message.author) + '**')
          await asyncio.sleep(3)
          await message.author.send('This will go to the database records.')
          await asyncio.sleep(5)
          await message.author.send("I'll be sure to send a copy to your parents. 😈")

      elif any(word in message.content.replace("-","") for word in insultworthy):
        dice = random.randint(0,len(insults)-1)
        choice = insults[dice]
        try:
          await message.delete()
        except:
          print("Something went wrong while trying to delete a msg.")
          await message.add_reaction('<:kgm_angry:850398050358132756>')
        await channel.send(choice)
        if dice // 2 == 0:
          await message.author.send('**Say cheese, ' + str(message.author) + '**')
          await asyncio.sleep(3)
          await message.author.send('This will go to the database records.')
          await asyncio.sleep(5)
          await message.author.send("I'll be sure to send a copy to your parents. 😈")

      elif any(word in message.content.replace(",","") for word in insultworthy):
        dice = random.randint(0,len(insults)-1)
        choice = insults[dice]
        try:
          await message.delete()
        except:
          print("Something went wrong while trying to delete a msg.")
          await message.add_reaction('<:kgm_angry:850398050358132756>')
        await channel.send(choice)
        if dice // 2 == 0:
          await message.author.send('**Say cheese, ' + str(message.author) + '**')
          await asyncio.sleep(3)
          await message.author.send('This will go to the database records.')
          await asyncio.sleep(5)
          await message.author.send("I'll be sure to send a copy to your parents. 😈")



  # THE FOLLOWING ARE SOME 'SMART COMMANDS' that don't need a prefix to work. Muxbot simply fishes out its instruction parameters if some conditions are met
  # To ensure better sensitivity, the commands are not case-sensitive since Muxbot converts all text strings into lowercase English ASCII.
  
  # Bug report trigger
  if ("log") in message.content.lower() and ("mux") in message.content.lower():
    await channel.send("Hmm... you want me to report a bug? Very well. Type it down starting with /log")
    def check(msg):
      return msg.content.startswith('/log')
    message = await client.wait_for('message', check=check)
    lognote = message.content[len('/log'):]
    await channel.send("Alright, buddy. I've taken that into account. The real `Mukto` will handle it from his side.")
    bugwrite(str(message.author) + " said: " + str(lognote) + "-- Time: " + time.ctime())

  # Invite link for Heartbreak - Muxbot's female counterpart (and elder 'sister')
  if ("mux") in message.content.lower() and ("where") in message.content.lower() and ("your") in message.content.lower() and (("sister") in message.content.lower() or ("partner") in message.content.lower()):
    await channel.send("Oh, right...")
    await asyncio.sleep(2)
    await channel.send("Invite her here, please : https://mukto.live/bots/heartbreak")

  # Changes nickname of a user (permission required)
  if message.content.lower() == "/nickname":
    await channel.send("Type /name nicknamehere")
    def check(msg):
        return msg.content.startswith('/name')
    message = await client.wait_for('message', check=check)
    name = message.content[len('/name'):].strip()
    await channel.send('{} is your new nickname'.format(name))
    await message.author.edit(nick=name)
  
  # Shows update log (must be pre-stored in the directory)
  if message.content.lower() == "mux, ulog":
    try:
      f = open("update_log.txt","r")
      if f.mode == 'r':
        contents = f.read()
        await channel.send(contents)
    finally:
      f.close()
  
  # Sends random spam links and junk (must be pre-stored in the directory)
  if message.content == "mux, spam": #if author types /ulog bot displays updatelog
    try:
      f = open("spam.txt","r")
      if f.mode == 'r':
        txtLines = f.readlines()
        numLines = len(txtLines)
        dice = random.randint(0,numLines)
        f.seek(0)
        contents = txtLines[dice]
        await channel.send(contents)
    finally:
      f.close()
  
  # THIS SINGLE LINE OF CODE IS VERY VERY IMPORTANT TO ENSURE THAT BOTH THE CLIENT.COMMAND AND CLIENT.EVENT COMMANDS CAN RUN SMOOTHLY WITHOUT CLASHING OR LAGGING
  await client.process_commands(message)


# This function keeps the bot alive by opening up a webserver (Replit recommended) (Needs a bot from https://uptimerobot.com in order to work)
# The keep_alive.py module is included with this repository. However, it is not by me. It was pre-equipped with the Replit bot template.
keep_alive()

# Last, but not the least, don't forget to run your bot!
client.run(os.getenv("TOKEN"))
