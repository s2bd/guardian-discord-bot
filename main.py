# 𝗡𝗔𝗧𝗦𝗨𝗞𝗜 (𝗛𝗘𝗔𝗥𝗧𝗕𝗥𝗘𝗔𝗞) 𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗕𝗢𝗧 - 𝗢𝗥𝗜𝗚𝗜𝗡𝗔𝗟 𝗦𝗢𝗨𝗥𝗖𝗘
# @author dmimukto 2021
# @credits Replit's Discord Bot template, Stack Overflow, Cisc0-gif (https://github.com/Cisc0-gif/Discord-Bot-Template/blob/a53aad3ae91ed02d6f99a97328e1d9e4a9cc4a17/bot.py)
# @credits_plugins Automata (https://github.com/MUNComputerScienceSociety/Automata), hamzahap (https://github.com/MUNComputerScienceSociety/Automata/commits?author=hamzahap), mudkip (https://github.com/MUNComputerScienceSociety/Automata/commits?author=Mudkip)
# @license MIT License (https://github.com/dmimukto/Muxbot/blob/main/LICENSE)
# @copyright Asenturisk Corporation 2021


# Importing the necessary modules for booting up and running the bot.
import discord
import os
import sys
import time
import discord.ext
import random
import json
import logging
import datetime
import asyncio
from collections import Counter
import platform
from keep_alive import keep_alive

# Further imports for running extra features from discord.py and python itself
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


# Defining the variable "client" as discord.Client() (So that I don't have to write discord.Client() everytime. C'mon! If you're reading this, you're definitely a programmer so you should understand the usual etiquettes and shortcuts we use!)
client = discord.Client()
# Here's where you can customize the bot's prefix. Since this is the pure source from a running version of Heartbreak (https://mukto.live/bots/heartbreak), The default prefix is a dot "." but it is unnecessary since Heartbreak detects triggers from the regular messages anyway
client = commands.Bot(command_prefix = '.') #put your own prefix here

# If you're running your bot on Replit (which I myself used and greatly recommend), you can set up private variables from the sidebar. Elsewhere, you usually create a ".env" file in the directory.
# In that .env file, you just add in a single line "TOKEN = 897wr8iuaf09fWhateverYourTokenIs244324"
TOKEN = os.getenv("TOKEN")


# TOLERANCE VALUES HERE :
# I still haven't properly set them up for usage.
tolerance_help = 0
tolerance_sus = 0

# These are variables linked to some hardcoded GIFs and videos for Heartbreak.

GIGGLE = "https://cdn.discordapp.com/emojis/821538085741133845.png"
CHIKA_GIF = "https://media.tenor.com/images/639a8f11cddb913ea4a4d81ceda3f8ec/tenor.gif"
PAIMON_GIF = "https://upload-os-bbs.hoyolab.com/upload/2020/07/19/1096276/5d55575548a30ca21fcdb50285b9c694_6465808929343059713.gif"
PAIMON_EHE = "https://media1.tenor.com/images/64eb0176b8ec007e2c0ffa65a92c8dc0/tenor.gif"
SUSCLIP = "https://tribe-video-input-temp.s3.amazonaws.com/5f9adb96fb2c414b6f59de2c/posts/60cb4b950bcc7b081a04aebb/65928_sus.mp4"

"""
=======================================[    𝐂𝐥𝐢𝐞𝐧𝐭 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬    ]======================================
"""
# Assuming you are already familiar with the official Discord.py API (https://discordpy.readthedocs.io/en/stable/api.html), you should know the basics about client.event and client.command functions.

# Sends a GIF of Paimon doing the 'ehe' pose
@client.command()
async def ehe(ctx):
  "| Ehe~"
  await ctx.send(PAIMON_EHE)

# Sends a GIF of Paimon hovering about (like the one in the Genshin Impact idle menu)
@client.command()
async def paimon(ctx):
  """| Have a Paimon!"""
  await ctx.send(PAIMON_GIF)

# Does exactly what the help text says 
@client.command()
async def choose(ctx, *choices: str):
    """| Chooses between multiple words provided, seperated by spaces."""
    await ctx.send(random.choice(choices))

# This plugin/feature has been adapted from https://github.com/MUNComputerScienceSociety/Automata/blob/master/plugins/Hewwo/__init__.py
# @author mudkip (https://github.com/Mudkip)
@client.command()
async def hewwo(ctx, *, speech: str):
#async def hewwo(ctx, *speech: str):
    """| Converts given words to cute words"""
    #try:
    transform = str(discord.utils.escape_mentions(speech).lower().replace('r', 'w').replace('l', 'w').replace('n', 'ny').replace('oo', 'woo'))
    await ctx.send(transform)
    #except:
     # await ctx.send("""🥺 I'm sorry, senpai. I don't understand this command. 😞""")

# A really annoying command that pings @everyone
@client.command()
async def ping(ctx):
    """| Testing command"""
    await ctx.send("""@everyone @everyone @everyone""")

# Sends Mahir Chowdhury's YouTube channel link.
# Was implemented as a sponsorship feature
@client.command()
async def mahir(ctx):
    """| Sends Mahir's channel link."""
    await ctx.send("""
    Here ya go!
    Mahwweeeer Bwwweaats...
    my favorite~ 😊🤗
    https://www.youtube.com/c/MahirBeats
    """)

# This plugin/feature has been adapted from https://github.com/MUNComputerScienceSociety/Automata/blob/master/plugins/Vibe/__init__.py
# @author Hamza Punjabi (https://github.com/hamzahap)
VIBE_IMAGE = "https://s3.gifyu.com/images/catvibe.gif"
VIBIER_IMAGE = "https://s3.gifyu.com/images/ezgif.com-gif-maker-174e18faa852a3028.gif"
VIBIEST_IMAGE = "https://s3.gifyu.com/images/ezgif.com-gif-maker-2664260aedaea9638.gif"
@client.command()
async def vibe(ctx: commands.Context, vibelevel: int = 1):
  """| Replies with a cat bop GIF. Vibe levels can also be specified."""
  if vibelevel <= 1:
    await ctx.send(VIBE_IMAGE)
  elif vibelevel == 2:
    await ctx.send(VIBIER_IMAGE)
  else:
    await ctx.send(VIBIEST_IMAGE)

# This plugin/feature was inspired by the 'hewwo' plugin/feature above
@client.command()
async def says(ctx, *, arg):
  "| Copies message and tells it via her message"
  copythat = discord.utils.escape_mentions(arg)
  await ctx.send(copythat)

# Still haven't implemented a proper 'bug status' output yet, so Heartbreak just sends the rather-inappropriate plugin fail text
@client.command()
async def vomit(ctx):
    """| Spits out errors in her program."""
    await ctx.send("""🥺 senpai, please don't make me do this...""") 

# Member kicker 2000
@client.command()
async def kick(ctx, member : discord.Member):
    """| Kicks a member. Don't try this!"""
    try:
        await member.kick(reason=None)
        await ctx.send("🙄😜 Oopsies, I kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("""I'm sorry, either I don't have the permissions to do this evil thing or I don't want to do this. 😅😓""")

# C'mon! She doesn't want to! You gotta do it the 'hard way' (by coming over to Github and finding the source code by yourself!)
@client.command()
async def xray(ctx):
  """| Shows her entire source code."""
  await ctx.send("""😡 NO I WON'T!""")




# Logging system for recording bot metrics and stats (OPTIONAL)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

# Logging system for recording server messages (OPTIONAL)
def logwrite(msg, server): #writes chatlog to MESSAGES.log
  with open('ServerMsgs/'+str(server)+'_MESSAGES.log', 'a+') as f:
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


# This function runs whenever Heartbreak wakes up from her virtual land of dreams 
@client.event
async def on_ready():
  # The following wordmark is for decorative purposes only. Please remove it since you are not hosting Heartbreak 'as is'.
  print("""
  
.  .             .   .               ,   
|  |             |   |               |   
|--| ,-. ,-: ;-. |-  |-. ;-. ,-. ,-: | , 
|  | |-' | | |   |   | | |   |-' | | |<  
'  ' `-' `-` '   `-' `-' '   `-' `-` ' ` """)
  print('---------------------------------------------------------------------')
  print('')
  print('https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=' + str(client.user.id))
  print('--------------------------------------------------------------------------')
  print('Logged in as:')
  print("Username : "+str(client.user.name)+" a.k.a. "+str(client.user)+" with ID : "+str(client.user.id))
  print('╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮')
  print(" LIVE CHAT LOG - See the Serverwise Logs For Details ")
  print("╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")

  # You may uncomment and place in one of the following 'activity statuses' for the bot.
  # By default, Heartbreak runs a 'listening' status.
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Mahir Beats"))
  
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
  
  # End of on_ready()

  

# Auto-commands that run whenever their respective triggers have been activated

@client.event
async def on_member_join(member):
  #channel = message.channel
  server = member.guild
  print("Member:", member, "joined!")
  #await channel.send("Member:", member, "joined 😀")
  logwrite("Member: " + str(member) + " joined!", server)

@client.event
async def on_member_remove(member):
  #channel = message.channel
  server = member.guild
  print("Member:", member, "removed!")
  #await channel.send("Member:", member, "removed 😞")
  logwrite("Member: " + str(member) + " removed!", server)

@client.event
async def on_guild_role_create(role):
  #channel = message.channel
  server = role.guild
  print("Role:", role, "was created!")
  #await channel.send("Role:", role, "was created! 📝")
  logwrite("Role: " + str(role) + " was created!", server)

@client.event
async def on_guild_role_delete(role):
  #channel = message.channel
  server = role.guild
  print("Role:", role, "was deleted!")
  #await channel.send("Role:", role, "was deleted! ❎")
  logwrite("Role: " + str(role) + " was deleted!", server)

@client.event
async def on_guild_channel_create(channel):
  #channel = message.channel
  server = channel.guild
  print("Channel:", channel, "was created!")
  #await channel.send("Channel:", channel, "was created!")
  logwrite("Channel: " + str(channel) + " was created!", server)

@client.event
async def on_guild_channel_delete(channel):
  #channel = message.channel
  server = channel.guild
  print("Channel:", channel, "was deleted!")
  #await channel.send("Channel:", channel, "was deleted!")
  logwrite("Channel: " + str(channel) + " was deleted!", server)

@client.event
async def on_guild_channel_update(before, after):
  #channel = message.channel
  server = after.guild
  print("Channel Updated:", after)
  #await channel.send("Channel Updated:", after)
  logwrite("Channel Updated: " + str(after), server)


@client.event
async def on_message(message):
  # First up, set up the conditions that the bot ignores whatever it says, otherwise there could be an infinite loop
  if message.author == client.user:
    return #ignore what bot says in server so no message loop
  channel = message.channel
  try:
    server = channel.guild
  except:
    # If the messages are sent in the direct messaging inbox of the bot, then they are stored seperately in the logging directory
    print("Message sent in DMs")
    server = '_privatemsg_'
  print(message.author, "said:", message.content, "-- Time:", time.ctime()) #reports to discord.log and live chat
  logwrite(str(message.author) + " said: " + str(message.content) + "-- Time: " + time.ctime(), server)

  

  # This mechanism works just like Muxbot's blacklist mode, but in place of profanity, Heartbreak deletes her client.command commands, so that everything is clean
  # Also, this allows her to copy a user's messages and then immediately delete the user who sent the original message, making it harder to trace who said that.
  speakHeaders = [".say", ".hewwo", ".ehe",".paimon",".ping",".mahir"]
  if any(word in message.content.lower() for word in speakHeaders):
      try:
        await message.delete()
      except:
        return
  
  # THE FOLLOWING ARE SOME 'SMART COMMANDS' that don't need a prefix to work. Heartbreak simply fishes out its instruction parameters if some conditions are met
  # To ensure better sensitivity, the commands are not case-sensitive since Heartbreak converts all text strings into lowercase English ASCII.

  # BUG LOGGER SYSTEM
  if ("heartbreak") in message.content.lower() and (("report") in message.content.lower() or ("log") in message.content.lower())and ("bug") in message.content.lower():
    await channel.send("Hmm... you want me to report a bug, senpai? 🤔 Okiiii. 😊 Type it down starting with `/log`")
    def check(msg):
      return msg.content.startswith('/log')
    message = await client.wait_for('message', check=check)
    lognote = message.content[len('/log'):]
    await channel.send("Okay, senpai. Your report has been sent to the developer. He'll check it out ASAP.")
    bugwrite(str(message.author) + " said: " + str(lognote) + "-- Time: " + time.ctime())

  # Changes nickname of a user (permission required)
  if message.content.lower() == "/nickname":
    await channel.send("Type /name nicknamehere")
    def check(msg):
        return msg.content.startswith('/name')
    message = await client.wait_for('message', check=check)
    name = message.content[len('/name'):].strip()
    await channel.send('{} is your new nickname'.format(name))
    await message.author.edit(nick=name)
  

  # If you're not feeling in the right mood, you can also make Heartbreak do the same by intercepting the prefix-based commands and making her reply with harsh or depressing words
  #if ("choose") in message.content.lower():
    #await channel.send("Meh, I can't decide today. Sorry. 😒")

    
  # This was meant to be a server-specific command, for testing if she can copy an emoji
  if (":duckdance~1:") in message.content:
    await channel.send(":duckdance~1:")

  # Creates a DM (direct msg) chat with an user
  if message.content.lower() == "dm me":
    await channel.send("Creating DM with " + str(message.author))
    await message.author.send('*DM started with ' + str(message.author) + '*')
    await message.author.send('Hello!')
    await message.author.send("Please note, that some commands may not work here since we're so close together.🥵🤭")

  # CHECK FOR LOL, REPLY WITH GIGGLE
  if (" lol") in message.content:
    await message.add_reaction('<:giggle:821538085741133845>')
  elif ("lol") in message.content.lower():
    await message.add_reaction('<:giggle:821538085741133845>')
  elif (" lol") in message.content:
    await message.add_reaction('<:giggle:821538085741133845>')
  elif ("lollipop") in message.content:
    await channel.send(":lollipop:")
  elif message.content == "lol" or message.content == "Lol" or message.content == "LOL" or message.content =="IoI" or message.content == "/o/" or message.content == "lol":
    await message.add_reaction('<:giggle:821538085741133845>')

  # This command was for playing a sort of 'Russian Roulette' by messing around with probability.
  # Heartbreak either sends a Rick Roll version of the forsaken "Fukouna Shoujo 03" GIF (if you're lucky) or.... sends the dreaded original GIF uncensored (luckly for NSFW people)
  #if ("fukouna") in message.content.lower():
    #dice = random.randint(0,9)
    #if dice > 4:
      #await channel.send("https://i.kym-cdn.com/photos/images/original/002/098/468/b87.gif")
    #else:
      #await channel.send("https://cdn.discordapp.com/attachments/846755146028941392/846807252971290684/fukounashoujo500.gif")
  
  # This command tells Heartbreak to send a GIF of Chika Fujiwara if the message conditions are met
  if (("send") in message.content.lower() or ("give") in message.content.lower() or ("post") in message.content.lower()) and ("chika") in message.content.lower() and ("gif") in message.content.lower():
    await channel.send(CHIKA_GIF)

  # This command has been temporarily turned off due to complaints from a server
  #if any(word in message.content.lower() for word in ["sus","5u5","amogus"]):
    #if tolerance_sus == 9:
      #await channel.send("You're spamming this command, senpai. 😠")
    #elif tolerance_sus >= 10:
      #print("Someone spammed this command")
    #else:
      #dice = random.randint(1,2)
      #if dice == 2:
        #await channel.send("Sus!")
        #await channel.send(SUSCLIP)
      #else:
        #await channel.send(SUSCLIP)

  # Sends a Paimon 'ehe' GIF just like the client.command but with more sensitivity
  if message.content.lower()=="ehe" or message.content.lower()=="ehe~":
    await channel.send(PAIMON_EHE)
  
  # Sends a tampered help list
  if message.content.lower()=="help":
    if tolerance_help == 9:
      await channel.send("You're spamming this command, senpai. 😠")
    elif tolerance_help >= 10:
      print("Someone spammed this command")
    else:
      await channel.send("Oh, I'm sorry 😥")
      await channel.send("There is NO HELP from now on. 😈")
      await channel.send("The range of commands for me are now upto your imagination. 😏")
      await channel.send("Just say `ulog` to review updates.")
      await channel.send("**Have a nice day.** 👋")
      tolerance_help += 1
  
  if message.content=="<3" or message.content=="❤️":
    await channel.send("<3 to you, too!")
  
  # --------------------------------------- QUICK TEMPLATE
  # if message.content=="":
  #   await channel.send()
  # -------------------------------------------------------
  

  # Shows update log (must be pre-stored in the directory)
  if message.content.lower() == "ulog":
    try:
      f = open("update_log.txt","r")
      if f.mode == 'r':
        contents = f.read()
        await channel.send(contents)
    finally:
      f.close()

  # Sends random spam links and junk (must be pre-stored in the directory)
  if "spam" in message.content.lower() and "Heartbreak" in message.content.lower():
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

  if message.content == "/whoami": #if author types /whoami bot responds with username
    await channel.send(message.author)
  
  # THIS SINGLE LINE OF CODE IS VERY VERY IMPORTANT TO ENSURE THAT BOTH THE CLIENT.COMMAND AND CLIENT.EVENT COMMANDS CAN RUN SMOOTHLY WITHOUT CLASHING OR LAGGING
  await client.process_commands(message)


# This function keeps the bot alive by opening up a webserver (Replit recommended) (Needs a bot from https://uptimerobot.com in order to work)
# The keep_alive.py module is included with this repository. However, it is not by me. It was pre-equipped with the Replit bot template.
keep_alive()

# Last, but not the least, don't forget to run your bot!
client.run(os.getenv("TOKEN"))
