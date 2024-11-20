import discord
from discord.ext import commands

import VARIABLE

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix="-", intents=permissions)


@bot.command()
async def embed(ctx: commands.Context):
    view = discord.ui.View()
    my_embed = discord.Embed(title="Três Dragões",
                             description="Score:")
    botao = discord.ui.Button(label="Jogar 2d6",
                              style=discord.ButtonStyle.blurple)
    view.add_item(botao)
    await ctx.send(embed=my_embed, view=view)


@bot.command()
async def play(ctx: commands.Context):

    view = discord.ui.View()
    botao = discord.ui.Button(label="Jogar 2d6",
                              style=discord.ButtonStyle.blurple)
    botao_two = discord.ui.Button(label="Jogar 2d6",
                                  style=discord.ButtonStyle.red)

    view.add_item(botao)
    view.add_item(botao_two)
    await ctx.reply("Vamos jogar Três Dragões", view=view)


@bot.command()
async def m_help(ctx: commands.Context):
    await ctx.reply(VARIABLE.ALL_COMMANDS)


bot.run(VARIABLE.BOT)
