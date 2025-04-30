import discord
from discord.ext import commands
import datetime

current_time = datetime.datetime.now(datetime.timezone.utc)

#COMANDO HELP COM EMBED
@commands.command()
async def help(ctx):
    embed = discord.Embed(
        title="**Lista de comandos - CAZIO BOT**",
        description=
        "Precisando de uma ajudinha? Deixa comigo:\n\n`z!ping` - Testa o bot, caso esteje online\n`z!help` - Lista os comandos do bot\n`z!rpg` - Mostra a lista de RPGs da Sociedade do Tridente\n`z!roll [n]` - Comando para rolar um dado de **n** faces (Ex: `z!roll 20`)\n`z!querojogar` - Mande esse comando caso esteja interessado em jogar\n`z!queronarrar` - Mande esse comando caso esteja interessado em narrar uma campanha",
        color=discord.Color.dark_green()
    )
    embed.set_thumbnail(url="https://i.imgur.com/UWbgVxD.png")
    embed.set_footer(text=f"Comando solicitado por @{ctx.author.name}", icon_url=ctx.author.avatar.url)
    embed.timestamp = current_time
    await ctx.channel.send(embed=embed)