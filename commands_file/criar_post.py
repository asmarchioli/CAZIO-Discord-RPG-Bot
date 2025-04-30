from discord.ext import commands
import discord
import asyncio

# Função para obter resposta interativa
async def obter_resposta(ctx, pergunta):
    await ctx.send(pergunta)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        resposta = await ctx.bot.wait_for('message', check=check, timeout=60.0)
        return resposta.content
    except asyncio.TimeoutError:
        await ctx.send("Tempo esgotado. Comando cancelado.")
        return None

# Comando criar_post
@commands.command()
async def criar_post(ctx):
    # Coleta interativa de dados
    titulo = await obter_resposta(ctx, "Qual é o título da postagem?")
    if titulo is None: return

    conteudo = await obter_resposta(ctx, "Qual é o conteúdo da postagem?")
    if conteudo is None: return

    imagem_url = await obter_resposta(ctx, "Qual é a URL da imagem?")
    if imagem_url is None: return

    tags_input = await obter_resposta(ctx, "Quais são as tags? (separadas por vírgula)")
    if tags_input is None: return

    tags_escolhidas = [tag.strip() for tag in tags_input.split(',')]

    forum_channel = ctx.bot.get_channel(1349345197502500946)  # Substitua pelo ID do canal de fórum
    if forum_channel is None:
        await ctx.send("Canal do fórum não encontrado!")
        return

    # Mapeamento das tags disponíveis no canal
    tags_disponiveis = {tag.name.lower(): tag for tag in forum_channel.available_tags}
    tags_para_adicionar = [tags_disponiveis[tag.lower()] for tag in tags_escolhidas if tag.lower() in tags_disponiveis]

    try:
        # Criação do embed com título, descrição e imagem
        embed = discord.Embed(title=titulo, description=conteudo, color=0xff010b)
        embed.set_image(url=imagem_url)

        # Criação da thread no fórum
        thread_with_message = await forum_channel.create_thread(
            name=titulo,
            embed=embed,
            applied_tags=tags_para_adicionar
        )

        thread = thread_with_message.thread
        await ctx.send(f"Post criado no fórum: https://discord.com/channels/{ctx.guild.id}/{forum_channel.id}/{thread.id}")
    except Exception as e:
        await ctx.send(f"Erro ao criar o post: {e}")
