import discord
from discord.ext import commands

class Moderation(commands.Cog, description = "Comandos para Moderação!"):   
    """Works with moderation"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731) #Verificar ping
    @commands.command(help = "-ping, para verificar a latência do bot.") 
    async def ping(self, ctx):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)
        latency = round(self.bot.latency * 1000, 1)
        msg = (f"Ping:{latency}ms")
        await channel.send(msg)

    @commands.has_permissions(ban_members=True) #Banir
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(name = "ban", help = "-ban (@user) (motivo), para banir um membro.") 
    async def ban(self, ctx, user: discord.Member, *, reason = "Não especificado"):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)  
        ban_dm = discord.Embed(
        title = "Você foi banido! :cold_sweat:",
        description =f"**Você foi banido de {ctx.message.guild.name}!**\n \n Motivo: `{reason}` \n \n Por favor, evite esse tipo de comportamento no futuro."
        )
        ban_msg = discord.Embed(
        title =f"{user} foi banido!",
        description =f"Por: @{ctx.author.mention}\n Motivo: `{reason}`" 
        )

        await user.send(embed = ban_dm)
        await user.ban(reason = reason)
        await channel.send(embed = ban_msg)

    @commands.has_permissions(ban_members=True) #Desbanir
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(name = "unban", help = "-unban (Nome#Números), para desbanir um membro.")
    async def unban(self, ctx, *, user):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)
        bannedUsers = await ctx.guild.bans()
        name, discrimator = user.split("#")

        for ban in bannedUsers:
            user = ban.user
            
            if(user.name, user.discriminator) == (name, discrimator):
                unban_msg = discord.Embed(
                title =f"{user} foi desbanido!",
                description =f"Por: @{ctx.author.mention}" 
                )
                await ctx.guild.unban(user)
                await channel.send(embed = unban_msg)
                return
    
    @commands.has_permissions(kick_members=True) #Expulsar 
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(name="kick", help = "-kick (@user) (motivo), para banir um membro.")
    async def kick(self, ctx, user : discord.Member, *, reason = "Não especificado"):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)
        kick_dm = discord.Embed(
        title = "Você foi expulso! :door:",
        description =f"**Você foi expulso de {ctx.message.guild.name}!**\n \n Motivo: `{reason}` \n \n Por favor, evite esse tipo de comportamento no futuro."
        )

        kick_msg = discord.Embed(
        title =f"{user} foi expulso!",
        description =f"Por: @{ctx.author.mention}\n Motivo: `{reason}`" 
        )
    
        await user.send(embed = kick_dm)
        await user.kick(reason = reason)
        await channel.send(embed = kick_msg)

    @commands.has_permissions(manage_messages=True) #Limpar Chat
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(pass_context=True, help = "-clear (all ou valor), para apagar mensagens de um chat.") 
    async def clear(self, ctx, amount: str):
        if amount == "all":
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=(int(amount) + 1) )

    @commands.has_permissions(manage_messages=True) #Silenciar membro
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(help = "-mute, para silenciar.")
    async def mute(self, ctx, user: discord.Member, *, reason="Não especificado"):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Tártaro")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Tártaro")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        mute_msg = discord.Embed(
        title =f"{user} foi Silenciado!",
        description =f"Por: @{ctx.author.mention}\n Motivo: `{reason}`"
        )
        
        mute_dm = discord.Embed(
        title = "Você foi Silenciado! :door:",
        description =f"**Você foi silenciado de {ctx.message.guild.name}!**\n \n Motivo: `{reason}` \n \n Por favor, evite esse tipo de comportamento no futuro."
        )
        
        await user.send(embed = mute_dm)
        await user.add_roles(mutedRole, reason=reason)
        await channel.send(embed = mute_msg)

    @commands.has_permissions(manage_messages=True) #Habilitar chats
    @commands.has_any_role(721809651842154617, 721808954266746940, 820032932857118731)
    @commands.command(help = "-unmute (Nome#Números), para habilitar chats de um membro.")
    async def unmute(self, ctx, user: discord.Member):
        guild = self.bot.get_guild(523964517114183691)
        channel = guild.get_channel(897218908019359745)
        mutedRole = discord.utils.get(ctx.guild.roles, name="Tártaro")

        unmute_msg = discord.Embed(
        title =f"{user} pode interagir nos chats!",
        )

        unmute_dm = discord.Embed(
        title =f"Você pode interagir nos chats da {ctx.message.guild.name} novamente!",
        )

        await user.remove_roles(mutedRole)
        await user.send(embed = unmute_dm)
        await channel.send(embed = unmute_msg)

def setup(bot):
    bot.add_cog(Moderation(bot))

      