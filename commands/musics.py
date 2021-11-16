from discord.ext import commands
import DiscordUtils
import discord
music = DiscordUtils.Music()

class Music(commands.Cog, description = "Comandos para ouvir músicas."):
    """Works with musics"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["j"], help ="-join, para o bot entrar no canal.") #Join
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        embed_mv = discord.Embed(
            colour= 12255232, #Vermelho
            description = "Para tocar uma música, primeiro se conecte a um canal de voz."
        )
        embed_jn = discord.Embed(
            colour= 8900346, #Azul claro
            description = "O que desejas ouvir?"
        )
        if voicetrue is None:
            return await ctx.send(embed = embed_mv)
        await ctx.author.voice.channel.connect()
        await ctx.send(embed = embed_jn)

    @commands.command(help = "-leave, mandar o bot embora do canal 😭.") #Leave
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        embed_bot = discord.Embed(
            colour= 12255232, #Vermelho
            description = "Eu não estou em um canal de voz."
        )
        embed_user = discord.Embed(
            colour= 12255232, #Vermelho
            description = "Você não está em um canal de voz."
        )
        if voicetrue is None:
            return await ctx.send(embed = embed_user)
        if mevoicetrue is None:
            return await ctx.send(embed = embed_bot)
        await ctx.voice_client.disconnect()

    @commands.command(aliases = ["p"], help = "-play (nome da música ou url), para tocar música.") #Play
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id = ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix = True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search = True)
            song = await player.play()
            embed_play= discord.Embed(
            colour= 8900346, #Azul claro
            description = f"{song.name} está no meu repertório!"
            )
            await ctx.send(embed = embed_play)
        else:
            song = await player.queue(url, search = True)
            embed_queue= discord.Embed(
            colour= 32768, #Verde
            description = f"Você adicionou a música {song.name} à fila!"
            )
            await ctx.send(embed = embed_queue)

    @commands.command(aliases = ["q"], help = "-queue, para ver a fila de músicas.")
    async def queue(self , ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        n = '\n'
        #l = list(enumerate(song.name, start = 1)) Tentar numerar as musicas
        embed_q = discord.Embed(
            colour= 1646116, #Cinza
            description = f'{n}{n.join([song.name for song in player.current_queue()])}'
        )
        await ctx.send(embed = embed_q)

    @commands.command(help = "-pause, para pausar a música.")
    async def pause(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        song = await player.pause()
        embed_p = discord.Embed(
            colour= 1646116, #Cinza
            description = f"{song.name} está pausado ⏸️"
        )
        await ctx.send(embed = embed_p)

    @commands.command(help = "-resume, para retomar a música.")
    async def resume(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        song = await player.resume()
        embed_r = discord.Embed(
            colour= 1646116, #Cinza
            description = f"Retomou {song.name} ▶️"
        )
        await ctx.send(embed = embed_r)

    @commands.command(help = "-loop, para colocar ou tirar a repetição de uma música.")
    async def loop(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            embed_li = discord.Embed(
            colour= 1646116, #Cinza
            description = f"{song.name} está em looping! 🔁"
            )
            return await ctx.send(embed = embed_li)
        else:
            embed_lo = discord.Embed(
            colour= 1646116, #Cinza
            description = f"{song.name} **saiu** do looping! 🔁"
            )
            return await ctx.send(embed = embed_lo)

    @commands.command(aliases = ["nw"], help = "-nw, para saber o nome da música tocada no momento.")
    async def nowplayer(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        song = player.now_playing()
        embed_np = discord.Embed(
            colour= 8900346, #Azul claro
            description = f"A música que está tocando agora é {song.name}."
        )   
        await ctx.send(embed = embed_np)

    @commands.command(help = "-remove, para tirar uma música da playlist(ordem numeral cotando a partir da 2° música)")
    async def remove(self, ctx, index):
        player = music.get_player(guild_id = ctx.guild.id)
        song = await player.remove_from_queue(int(index) )
        embed_r = discord.Embed(
            colour= 1646116, #Cinza
            description = f"{song.name} foi removido da fila! ⏏️"
        )   
        await ctx.send(embed = embed_r)

    @commands.command(help= "-skip, para pular uma música.")      
    async def skip(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        await player.skip()
        embed_s = discord.Embed(
            colour= 1646116, #Cinza
            description = f"Você pulou a música! ⏭️"
        )
        await ctx.send(embed = embed_s)
        

    @commands.command(help = "-stop, para finalizar as músicas.")
    async def stop(self, ctx):
        player = music.get_player(guild_id = ctx.guild.id)
        await player.stop()
        embed_stop = discord.Embed(
            colour= 8900346, #Azul claro
            description = f"Acabou as músicas! ⏹️"
        )
        await ctx.send(embed = embed_stop)

def setup(bot):
    bot.add_cog(Music(bot))

        