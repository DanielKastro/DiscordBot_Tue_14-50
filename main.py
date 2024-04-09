import discord
from discord.ext import commands


token = "OTg1Nzc1MTIyNzMwMzUyNjYx.G_i5sy._CHqcjRs0s1QBBZMOBWVUWvwhvvkUtT2jyTC7o"
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())

@bot.command()
async def test(ctx):
    await ctx.channel.send("Hello!")

bot.run(token)