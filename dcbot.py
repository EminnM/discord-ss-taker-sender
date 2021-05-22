from discord.ext import commands
import discord

channel_id = "" # you should write discord channel id to here
path = "" #example path: r"C:\users\hello\yourfilename.png"
api_key = ""
bot = commands.Bot(command_prefix=".")
@bot.event
async def on_ready():
    print("ready")

    channel = bot.get_channel(channel_id)
    await channel.send(file=discord.File(path))
    await bot.logout()
bot.run(api_key)
