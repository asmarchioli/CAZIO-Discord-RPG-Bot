from discord.ext import commands

@commands.command(name="listarservidores")
async def listar_servidores(ctx):
    servidores = ctx.bot.guilds
    lista_servidores = "\n".join([f"{guild.name} (ID: {guild.id})" for guild in servidores])

    if not servidores:
        await ctx.send("O bot não está em nenhum servidor.")
    else:
        await ctx.send(f"O bot está nos seguintes servidores:\n{lista_servidores}")
