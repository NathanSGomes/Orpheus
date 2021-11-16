from discord.ext import commands
import random


class Smart(commands.Cog, description = "Comandos para usuabilidades."):
    """A lot of Smart Commands"""
    def __init__(self, bot):
        self.bot = bot

    #@bot.command -> @commands.command
    @commands.command(name="calcular", help="Digite -calcular e adicione a equação.") #Calculadora
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

    @commands.command(aliases =["fp", "coc"], help ="Digite -fp, para jogar cara ou coroa.")
    async def flipcoin(self, ctx):
        variavel = random.randint(1,2)
        if variavel == 1:
            await ctx.send("Você tirou ||cara||!")
        elif variavel == 2:
            await ctx.send("Você tirou ||coroa||!")


def setup(bot):
    bot.add_cog(Smart(bot))

        