import os
import discord
from decouple import config
from discord.ext import commands
from pretty_help import PrettyHelp

intents =discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= "-", help_command = PrettyHelp(), intents = intents)

def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("moderations.kicks")
    bot.load_extension("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)
