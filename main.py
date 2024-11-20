import discord
from discord.ext import commands

import VARIABLE

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix="-", intents=permissions)


async def resposta(interact: discord.Integration):
    await interact.response.send_message("Botão")


@bot.command()
async def jogar(ctx: commands.Context):
    await ctx.send("Vamos Jogar **Três Dragões!**")


@bot.command()
async def play(ctx: commands.Context):

    view = discord.ui.View()
    botao = discord.ui.Button(label="Jogar 2d6",
                              style=discord.ButtonStyle.blurple)
    botao_two = discord.ui.Button(label="Jogar 2d6",
                                  style=discord.ButtonStyle.red)
    botao.callback = resposta

    view.add_item(botao)
    view.add_item(botao_two)
    await ctx.reply("Vamos jogar Três Dragões", view=view)


@bot.command()
async def m_help(ctx: commands.Context):
    await ctx.reply(VARIABLE.ALL_COMMANDS)


bot.run(VARIABLE.BOT)
