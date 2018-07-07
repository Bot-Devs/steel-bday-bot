import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def about():
    embed=discord.Embed(title="About me", description="This will list everyone that helped!", color=0x4ffd1c)
    embed.add_field(name=Author/Papi/Creator, value=XXWolfBane#5559, inline=False)
    await self.bot.say(embed=embed)
                
                
bot.run("NDY1MTEzNzAwNzIyODAyNjk4.DiIyaQ.oaEeUImFeCIQBI5n3S1eMNnLofI")
