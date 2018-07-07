import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def about(ctx):
     embed = discord.Embed(title="B-Day Bot!", description="Hello, this is the about command of B-Day Bot!"
     embed.add_field(title="Author/Creater/Papi", value="XXWolfBane#5559")

     await ctx.send(embed=embed)
                           
bot.run("NDY1MTEzNzAwNzIyODAyNjk4.DiIyaQ.oaEeUImFeCIQBI5n3S1eMNnLofI")
