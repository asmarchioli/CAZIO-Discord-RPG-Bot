from discord.ext import commands

#COMANDO INVERSE (RETORNA A MENSAGEM AO CONTRÁRIO)
@commands.command()
async def inverse(ctx, *args):
    message = ' '.join(args)
    if not message:
        await ctx.reply("Mande um texto na frente do código para eu inverter :upside_down:")
    else:
        await ctx.send(message[::-1])