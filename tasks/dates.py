import datetime
from discord.ext import commands, tasks

class Date(commands.Cog):
    """Work with dates"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(hours = 12) #Data e Hora
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(818912896561315840)

        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Date(bot))

        