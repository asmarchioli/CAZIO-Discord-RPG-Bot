import aiohttp # Importando aiohttp para requisições asíncronas HTML
from discord.ext import commands

@commands.command()
async def ficha_rapida(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    #Obter as classes válidas da API
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.dnd5eapi.co/api/classes") as response:
            if response.status != 200:
                await ctx.send("Não foi possível obter as classes válidas. Tente novamente mais tarde.")
                return
            data = await response.json()
            classes_validas = [item['name'] for item in data['results']]
        async with session.get("https://www.dnd5eapi.co/api/2014/races") as response:
            if response.status != 200:
                await ctx.send("Não foi possível obter as raças válidas. Tente novamente mais tarde.")
                return
            data = await response.json()
            racas_validas = [item['name'] for item in data['results']]

    await ctx.send("Perfeito! Vamos montar uma ficha rápida para D&D! Qual é a classe do seu personagem?")
    try:
        while True:
            classe = await ctx.bot.wait_for('message', check=check, timeout=60.0)
            if classe.content not in classes_validas:
                await ctx.send(f"Classe inválida! Escolha entre: {', '.join(classes_validas)}")
                continue
            break
    except TimeoutError:
        await ctx.send("Você demorou muito para responder. Tente novamente.")
        return

    await ctx.send("Qual é a raça do personagem?")
    try:
        while True:
            raca = await ctx.bot.wait_for('message', check=check, timeout=60.0)
            if raca.content not in racas_validas:
                await ctx.send(f"Raça inválida! Escolha entre: {', '.join(racas_validas)}")
                continue
            break
    except TimeoutError:
        await ctx.send("Você demorou muito para responder. Tente novamente.")
        return

    ficha = f"**Ficha Rápida**\nClasse: {classe.content}\nRaça: {raca.content}"
    await ctx.send(ficha)