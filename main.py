import discord
from discord.ext import commands

from VARIABLE import BOT

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix="-", intents=permissions)


@bot.command()
async def play(ctx: commands.Context):
    user = ctx.author.display_name
    await ctx.send(f"Saudações {user}!\nVamos jogar **Três Dragões?**")


@bot.command()
async def ola(ctx: commands.Context):
    user = ctx.author.display_name
    await ctx.send(f"Olá {user}!")


bot.run(BOT)
