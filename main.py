import discord
import os
import time
import random
import urllib.request
import logging
import asyncio
from discord.ext import commands
from keep_alive import keep_alive
from flask import Flask, render_template
from threading import Thread

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

BLACKLIST_MODE = True

# Initialize bot
bot = commands.Bot(command_prefix='mux, ', intents=intents)
TOKEN = os.getenv("TOKEN")

# Flask app setup
app = Flask(__name__)

# In-memory storage for server activities (server_id: [activities])
activity_log = {}
MAX_ACTIVITIES_PER_SERVER = 100  # Limit activities per server to prevent memory issues

# Logging setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

def ensure_directory_and_file(filepath):
    """Ensure the directory and file exist, creating them if necessary."""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(filepath):
        with open(filepath, 'a'):
            pass

def logwrite(msg, server):
    filepath = f'Serverwise/{server}_MESSAGES.log'
    ensure_directory_and_file(filepath)
    with open(filepath, 'a+', encoding='utf-8') as f:
        f.write(msg + '\n')

def bugwrite(msg):
    ensure_directory_and_file('reports.log')
    with open('reports.log', 'a+', encoding='utf-8') as buglog:
        buglog.write(msg + '\n')

# Ensure required files exist
for file in ['update_log.txt', 'spam.txt']:
    ensure_directory_and_file(file)

# Flask Routes
@app.route('/')
def dashboard():
    servers = []
    for guild in bot.guilds:
        members = [
            {
                'name': member.name,
                'id': member.id,
                'avatar': member.avatar.url if member.avatar else 'https://cdn.discordapp.com/embed/avatars/0.png'
            } for member in guild.members
        ]
        activities = activity_log.get(guild.id, [])
        servers.append({
            'name': guild.name,
            'id': guild.id,
            'member_count': len(members),
            'members': members,
            'activity_count': len(activities),
            'activities': activities
        })
    return render_template('dashboard.html', servers=servers)

# Commands
@bot.command()
async def greet(ctx):
    await ctx.send("""
**Behold, the Guardian bot!**

Ahoy there! I'm Guardia Alpha, the virtual projection of my creator's heart, mind and soul.
Right now, I am not as capable as I was planned to be.
But hopefully in the upcoming days, I shall be stronger and more powerful.

For now, allow me to protect your server from profanity and NSFW materials. Just grant me the role with the permission to 'Manage Messages'. Or better still, give me an administrator role.

I hope I can serve ya well, pal. 😎👌
    """)
    await ctx.send("```version 0.1.9 early access```")

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def ping(ctx):
    await ctx.send("No, I won't ping @everyone .")
    await ctx.send("(Heheh, I just did. 😈)")

@bot.command()
async def muxsays(ctx, *, arg):
    await ctx.send(discord.utils.escape_mentions(arg))

@bot.command()
async def ecoji(ctx, limit):
    ecoji_src = f"https://jackharrhy.dev/urandom/ecoji/{limit}"
    with urllib.request.urlopen(ecoji_src) as response:
        for row in response:
            await ctx.send(row.decode("utf-8"))

@bot.command()
async def kick(ctx, member: discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send(f"🦵 Get lost, {member.mention}")
    except:
        await ctx.send("Why should I? 🤷‍♂️")

@bot.command()
async def warn(ctx, member: discord.Member, *, reason="No reason"):
    await ctx.send(f">>> {member.mention} has been warned{f', for {reason}' if reason != 'No reason' else ''}")
    await member.send(f"Yo {member}.")
    await member.send(f"You have been warned{f' for {reason}' if reason != 'No reason' else ''}.")
    await member.send("Be careful. Or else, punishments will be severe. 😈")

# Events
@bot.event
async def on_ready():
    twitch_url = 'https://twitch.tv/acetylune'
    await bot.change_presence(activity=discord.Streaming(name="Acetylune", url=twitch_url))
    invite_link = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
    print(f"Guardian Discord Bot\n{'-'*69}")
    print(f'Logged in as: {bot.user.name} a.k.a. {bot.user} with ID: {bot.user.id}')
    print(f'Invite Link: {invite_link}')
    print('╭─' + '━'*49 + '╮')
    print(" LIVE CHAT LOG - See the Serverwise Logs For Details ")
    print('╰─' + '━'*49 + '╯')

def log_activity(guild_id, activity):
    """Log server activity in memory for the dashboard."""
    if guild_id not in activity_log:
        activity_log[guild_id] = []
    activity_log[guild_id].append({
        'content': activity,
        'time': time.ctime()
    })
    if len(activity_log[guild_id]) > MAX_ACTIVITIES_PER_SERVER:
        activity_log[guild_id] = activity_log[guild_id][-MAX_ACTIVITIES_PER_SERVER:]

@bot.event
async def on_member_join(member):
    activity = f"Member {member} joined!"
    logwrite(activity, member.guild)
    log_activity(member.guild.id, activity)
    print(activity)

@bot.event
async def on_member_remove(member):
    activity = f"Member {member} removed!"
    logwrite(activity, member.guild)
    log_activity(member.guild.id, activity)
    print(activity)

@bot.event
async def on_guild_role_create(role):
    activity = f"Role {role} was created!"
    logwrite(activity, role.guild)
    log_activity(role.guild.id, activity)
    print(activity)

@bot.event
async def on_guild_role_delete(role):
    activity = f"Role {role} was deleted!"
    logwrite(activity, role.guild)
    log_activity(role.guild.id, activity)
    print(activity)

@bot.event
async def on_guild_channel_create(channel):
    activity = f"Channel {channel} was created!"
    logwrite(activity, channel.guild)
    log_activity(channel.guild.id, activity)
    print(activity)

@bot.event
async def on_guild_channel_delete(channel):
    activity = f"Channel {channel} was deleted!"
    logwrite(activity, channel.guild)
    log_activity(channel.guild.id, activity)
    print(activity)

@bot.event
async def on_guild_channel_update(before, after):
    activity = f"Channel Updated: {after}"
    logwrite(activity, after.guild)
    log_activity(after.guild.id, activity)
    print(activity)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel = message.channel
    server = channel.guild if hasattr(channel, 'guild') else '_privatemsg_'
    log_entry = f"{message.author} said: {message.content} -- Time: {time.ctime()}"
    print(log_entry)
    logwrite(log_entry, server)

    # Store message in activity log for dashboard
    if hasattr(channel, 'guild'):
        log_activity(channel.guild.id, f"{message.author} said: {message.content}")

    if BLACKLIST_MODE:
        black_list = []
        insult_worthy = []
        insults = [
            "How would you feel if your profile showed up in the dark web tonight?",
            "Mind your manners, kid. Or else the consequences will be worse than revealing your browsing history to your parents.",
            "Got your data recorded. What're ya gonna do now? Go ahead, kick me. Your data remains with me. FOREVER.",
            # ... (other insults, truncated for brevity)
        ]

        content_lower = message.content.lower()
        if any(word in content_lower for word in black_list):
            try:
                await message.delete()
            except:
                print("Either msg is in DM or something went wrong.")
                await message.add_reaction('<:kgm_angry:850398050358132756>')

        for replace_char in [" ", ".", "-", ","]:
            check_content = content_lower.replace(replace_char, "")
            if (len(check_content)<= 6 or replace_char == " ") and any(word in check_content for word in insult_worthy):
                choice = random.choice(insults)
                try:
                    await message.delete()
                except:
                    print("Something went wrong while trying to delete a msg.")
                    await message.add_reaction('<:kgm_angry:850398050358132756>')
                await channel.send(choice)
                if random.randint(0, 1) == 0:
                    await message.author.send(f'**Say cheese, {message.author}**')
                    await asyncio.sleep(3)
                    await message.author.send('This will go to the database records.')
                    await asyncio.sleep(5)
                    await message.author.send("I'll be sure to send a copy to your parents. 😈")
                break

    # Smart commands
    content_lower = message.content.lower()
    if "log" in content_lower and "mux" in content_lower:
        await channel.send("Hmm... you want me to report a bug? Very well. Type it down starting with /log")
        def check(msg):
            return msg.content.startswith('/log')
        msg = await bot.wait_for('message', check=check)
        lognote = msg.content[len('/log'):].strip()
        await channel.send("Alright, buddy. I've taken that into account. The developer will handle it from his side.")
        bugwrite(f"{msg.author} said: {lognote} -- Time: {time.ctime()}")

    if content_lower == "/nickname":
        await channel.send("Type /name nicknamehere")
        def check(msg):
            return msg.content.startswith('/name')
        msg = await bot.wait_for('message', check=check)
        name = msg.content[len('/name'):].strip()
        await channel.send(f'{name} is your new nickname')
        await msg.author.edit(nick=name)

    if content_lower == "mux, ulog":
        ensure_directory_and_file('update_log.txt')
        with open("update_log.txt", "r", encoding='utf-8') as f:
            await channel.send(f.read())

    if content_lower == "mux, spam":
        ensure_directory_and_file('spam.txt')
        with open("spam.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()
            await channel.send(random.choice(lines).strip())

    await bot.process_commands(message)

# Run Flask in a separate thread
def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    keep_alive()
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    bot.run(TOKEN)
