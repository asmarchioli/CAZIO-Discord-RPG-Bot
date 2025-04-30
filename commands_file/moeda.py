from discord.ext import commands
import random

@commands.command()
async def moeda(ctx):
    resultado = random.choice(["Cara", "Coroa"])
    await ctx.reply(f"A moeda deu {resultado}!")