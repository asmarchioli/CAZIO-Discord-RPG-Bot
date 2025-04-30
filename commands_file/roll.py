from discord.ext import commands
import random

DICES = [4, 6, 8, 10, 12, 20, 100]

@commands.command()
async def roll(ctx, n_dice: str):
    try:
        n_dice = int(n_dice)
    except ValueError:
        await ctx.reply(f"{ctx.author.display_name}, você precisa informar o número de faces do dado como um número válido!")
        return
    if not n_dice in DICES:
        await ctx.reply(f"{ctx.author.display_name}, o número de faces do dado que você informou não é válido. Por favor, informe um número válido.")
        return
    
    resultado = random.randint(1, n_dice)
    if resultado == 1:
        await ctx.reply(f"🎲 Dado de {n_dice} faces: {resultado} - Falha crítica!")
    elif resultado == n_dice:
        await ctx.reply(f"🎲 Dado de {n_dice} faces: {resultado} - Sucesso crítico!")
    else:
        await ctx.reply(f"🎲 Dado de {n_dice} faces: {resultado}")

@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"Ei, {ctx.author.display_name}, você esqueceu de informar o número de faces do dado! Tente novamente.")