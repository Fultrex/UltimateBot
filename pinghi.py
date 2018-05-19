import discord
from discord.ext import commands


bot = commands.Bot ("!")

@bot.event
async def on_ready():
    print("bot online")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")


@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say ("Hey! :wave:")

@bot.command(pass_context=True)
async def credits(ctx):
    await bot.say ("``Bot created by Fultrex#2789``")

@bot.command(pass_context=True)
async def updates(ctx):
    await bot.say ("Bot is officially created!")

@bot.command(pass_context=True)
async def cmds(ctx):
     await bot.say ("Prefix: ! List of Commands: ban | kick | credits | cmds | commands | hello | ping | updates")

@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say ("Prefix: ! List of Commands: ban | kick | credits | cmds | commands | hello | ping | updates")

@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)

@bot.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    await bot.ban(userName)


bot.run ("NDQ3NDI2NjEwMDgyMjE3OTg0.DeHqpw.a0XMLc3rNBmBcCAgTQxEYWujYVw")
