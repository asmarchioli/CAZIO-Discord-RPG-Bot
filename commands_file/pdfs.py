import discord
from discord.ext import commands
import datetime

# Comando pdfs
@commands.command()
async def pdfs(ctx):
    current_time = datetime.datetime.now(datetime.timezone.utc)

    embed = discord.Embed(
        title="**LIVROS E FICHAS - D&D 5E**",
        description=(
            "O grande sapo mago das trevas, Cazio, compartilhará com vocês sua sabedoria anfíbia! (na verdade são só os livros do D&D que eu encontrei na [Biblioteca Élfica](https://bibliotecaelfica.org/)). De qualquer forma, eles estão disponíveis para download ou apenas leitura, é só apertar no link.\n\n"
            "**[Livro do Jogador:](https://bibliotecaelfica.org/2023/01/15/dd-5e-livro-do-jogador-fundo-branco/)** Um livro para todos os iniciantes e perítos. Aqui você irá encontrar tudo sobre as raças e classes básicas, além de todas as habilidades e mágias do seu personagem.\n"
            "**[Manual dos Monstros:](https://bibliotecaelfica.org/2023/01/15/old-dd-5e-manual-dos-monstros/)** Uma aventura não existe sem monstros, desde fantasmas até devoradores de mente.\n"
            "**[Guia do Mestre:](https://bibliotecaelfica.org/2023/01/15/dd-5e-guia-do-mestre/)** Vai mestrar uma campanha? Esse livro vai te auxiliar a criar aventuras, npcs e até multiversos!\n"
            "**[Guia de Xanathar para Todas as Coisas:](https://bibliotecaelfica.org/2023/01/15/dd-5e-guia-de-xanathar-para-todas-as-coisas-fundo-branco/)** Procurando por subclasses, mágias novas e armadilhas? Esse livro traz tudo isso e muito mais. *Atenção: o livro é feito por fãs, lembre-se de verificar antes com o mestre da partida se será permitido o uso de recursos adicionais.*\n\n"
            "**[Ficha de Personagem - Editável e Automática:](https://bibliotecaelfica.org/2023/01/15/dd-5e-ficha-de-personagem-automatica/)** O papel do seu personagem. Vê se lembra de trazer nas campanhas!\n"
            "**[Mil Fichas Prontas:](https://bibliotecaelfica.org/2023/01/15/dd-5e-ficha-de-personagem-automatica/)** Esqueceu de fazer ficha e quer jogar? Esse livro trás uma cacetada de fichas **nível 1** (não há níveis superiores no livro)."
        ),
        color=discord.Color.dark_red()
    )
    embed.set_thumbnail(url="https://imgur.com/u0aN19t.png")
    embed.add_field(
        name="Comandos de RPG",
        value="Precisando de uma ajudinha com as fichas? Teste o comando `z!rpg` no chat <#1271123322733596772>.",
        inline=True
    )

    # Verifica se bot.user está disponível antes de definir o footer
    if ctx.bot.user:
        embed.set_footer(text=ctx.bot.user.name, icon_url=ctx.bot.user.avatar.url)

    embed.timestamp = current_time
    await ctx.channel.send(embed=embed)
