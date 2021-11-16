from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

class Manager(commands.Cog, description = "Gerenciamento do Bot."):
    """Manage the bot"""
    def __init__(self, bot):
        self.bot = bot

    #@bot.event ->  @commands.Cog.listener
    @commands.Cog.listener() #Iniciar o bot
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado {self.bot.user}")
        activity = discord.Activity(type=discord.ActivityType.listening, name="Bring Me The Horizon")
        await self.bot.change_presence(status=discord.Status.online, activity=activity)

    @commands.Cog.listener() #Boas vindas
    async def on_member_join(self, member):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(795755113742204968)
        url_image = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/bc58172f-01e0-4559-a554-3714bf2bf5bc/dc0mqvx-9d0188d4-7243-4be9-9f46-b7678bc3e26a.jpg/v1/fill/w_1280,h_1280,q_75,strp/caronte_by_dawnbreakerdesigns_dc0mqvx-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2JjNTgxNzJmLTAxZTAtNDU1OS1hNTU0LTM3MTRiZjJiZjViY1wvZGMwbXF2eC05ZDAxODhkNC03MjQzLTRiZTktOWY0Ni1iNzY3OGJjM2UyNmEuanBnIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.KBWaFc0ZS5WSV8-1Z04YGjcKDgrrEc2PBCK8uA2HkH8"
        embed = discord.Embed(
            title = "- Boas-vindas ao Reino de Hades!",
            colour = 16732928, #Laranja
            description = f"Sabemos por que você está aqui, não sabemos {member.mention}? Agora pague pela **{guild.name}**! Pois seu destino já foi traçado."
        )
        embed.set_author(name="Caronte")
        embed.set_image(url = url_image)
        embed.set_footer(text="Reaja ao EMOJI para receber cargo.")
        msg = await channel.send(embed = embed)
        await msg.add_reaction("🥵")
    
    @commands.Cog.listener() #Dar Cargo
    async def on_reaction_add(self, reaction, user):  
        
        print(reaction.emoji)
        if user.id == 895939366222958592:
            pass
        elif reaction.emoji == "🥵":
            role = user.guild.get_role(818859163383103520)
            await user.add_roles(role)
            
    @commands.Cog.listener() #Censura de mensagens
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    
        if "palavrão" in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, não fale tais palavras nesse reino!")

            await message.delete()

    @commands.Cog.listener() #Mensagens de erro
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os Argumentos. Digite -help para ver os parâmetros de cada comando!")
        elif isinstance(error, CommandNotFound ):
            await ctx.send("O comando não existe. Digite -help para ver todos os comandos!")
        else:
            raise error
            
def setup(bot):
    bot.add_cog(Manager(bot))