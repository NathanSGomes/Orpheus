import discord
from discord.ext import commands


class Talk(commands.Cog, description = "Comandos de interação."):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    #@bot.command -> @commands.command
    @commands.command(name = "oi", help = "Digite -oi, para receber saudações.") #Comando para resposta = !oi
    async def send_hello(self, ctx):
        name = ctx.author.mention
        response = (f"Olá,{name} estou só de passagem, pois aguardam minhas músicas ao longo dos rios.") 

        await ctx.send(response)

    
    @commands.command(name = "historia", help = "Digite -historia, para receber um conto.") #Private Message
    async def history(self, ctx):
        try:
            await ctx.author.send("Vou lhe contar minha história.")
            await ctx.author.send("Que engano cometeram os deuses na morte do pobre Orfeu... Não foram as mênades que o mataram, com certeza. Nem poderiam. Alma alguma já não habitava aquele corpo, nem tocava mais aquela triste lira. Orfeu já havia partido. Morrera no próprio Hades, abandonando a si próprio ao olhar para trás, tão tomado pela saudade estava, de sua amada Eurídice. Na Terra dos Mortos, por este ato, ela ficara. E naquele instante, ele também. Seu espírito não voltara a ver a luz do dia, apenas o coração vazio, porque no seu corpo ainda batia.")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar essa história, habilite receber mensagens diretas de membros do servidor (Conf. de usuário > Privacidade)")

    @commands.command(name = "creditos", help = "Digite -creditos, para saber mais sobre meu criador.") #Private Message
    async def credits(self, ctx):
        try:
            await ctx.author.send("Fui criado pelo Dev. Nathan (https://github.com/NathanSGomes), com objetivo de estudar Python, por ele adorar mitologias todos seus projetos acabam com nomes icônicos assim como o meu ^^.")
        except discord.errors.Forbidden:
            await ctx.send("Não posso revelar meu criador, habilite receber mensagens diretas de membros do servidor (Conf. de usuário > Privacidade)")
    

def setup(bot):
    bot.add_cog(Talk(bot))

        