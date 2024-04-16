import discord
from discord.ext import commands


token = "OTg1Nzc1MTIyNzMwMzUyNjYx.G_i5sy._CHqcjRs0s1QBBZMOBWVUWvwhvvkUtT2jyTC7o"
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())


@bot.command()
async def test(ctx):
    await ctx.channel.send("Hello!")


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    ch = ctx.channel
    if ctx.content.startswith("*"):
        return
    if ctx.author.bot:
        return
    if ch.id == 1229770349176946829:
        await ctx.channel.send(":triumph: ")
    if ctx.author.id == 629337655158767626:
        await ctx.channel.send(":video_game: ")


bot.run(token)