import discord
from discord.ext import commands
import button_paginator as pg

# Comando rpg
@commands.command()
async def rpg(ctx: commands.Context):
    embeds = [
        discord.Embed(
            title="Lista de RPGs",
            description=(
                "**1 - Sumário**\n2 - Campanhas em andamento\n3 - Campanhas pausadas\n4 - Campanhas em programação\n5 - Campanhas passadas"
            )
        ),
        discord.Embed(
            title="Campanhas em andamento",
            description=(
                "Estamos sem campanhas sendo jogadas no momento. Acompanhe o canal <#681201881271631923> para saber quando novas campanhas serão iniciadas!"
            )
        ).set_thumbnail(
            url="https://media.tenor.com/LMz_TrIOxV8AAAAM/mr-bean-mrbean.gif"
        ),
        discord.Embed(
            title="Campanhas em pausa",
            description=(
                "**1 - Campanha de D&D 5E**\nMestre: <@1243049618325897216>\nStatus: Pausada"
                "\n\n**2 - Dies Irae: Uma campanha Kult: Divinity Lost**\nMestre: <@579295917002457101>\n**Status: Pausada (retorna em Junho)\n[Link para leitura do Prólogo](https://achieved-hamster-e96.notion.site/Pr-logo-Dies-Ir-160198640d288022ac51f1befee3e27d)."
            )
        ).set_thumbnail(
            url="https://www.rederpg.com.br/wp/wp-content/uploads/2020/05/DD-Logo.png"
        ),
        discord.Embed(
            title="Campanhas em programação",
            description=("**Campanha de Tormenta 20 RPG**\nMestre: <@596772923348484142>\nStatus: Programado para esse mês")
        ).set_thumbnail(
            url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cb5ffb133888121.61c9082a7453f.png"
        ),
        discord.Embed(
            title="Campanhas passadas",
            description=("**Era Clássica (D&D5)**\nMestre: <@643085058844131358>\nStatus: Terminado\n"
            "As primeiras campanhas jogadas no CAIC, todas administradas pelo grande Mestre Supremo Cássio.\n\n"
            "**Sociedade do Tridente - Prólogo + P1 (D&D5)**\nMestre: <@643085058844131358>\nStatus: Terminado\n"
            "A campanha que deu início à primeira geração dos magos da Sociedade do Tridente.\n\n"
            "**O Grande Norte e as Montanhas Sanguinárias (T20)**\nMestres: <@579295917002457101> e <@596772923348484142>\nStatus: Descontinuado\n"
            "Uma campanha que se inicia em uma taverna qualquer na cidade de Vectora. Um grupo de aventureiros se encontra na cidade e é convocado para destruir duas grandes ameaças ao mundo de Ardon. Para conferir a história da campanha, [clique aqui](https://docs.google.com/document/d/1vOB4f6A3aeg5Yz8bmCutZyknRvrYXDHLQT7zp-TCr7U/edit?usp=sharing).\n\n"
            )
        ).set_thumbnail(
            url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cb5ffb133888121.61c9082a7453f.png"
        )
    ]
    
    paginator = pg.Paginator(ctx.bot, embeds, ctx)  # Passando ctx.bot aqui em vez de 'bot'
    paginator.add_button(
        "prev",
        emoji="<:seta_outra_direita:1205355241038549043>",
        style=discord.ButtonStyle.blurple
    )
    paginator.add_button("page", style=discord.ButtonStyle.blurple)
    paginator.add_button(
        "next",
        emoji="<:seta_direita:1205354785537003530>",
        style=discord.ButtonStyle.blurple
    )
    await paginator.start()