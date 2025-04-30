import discord
from discord.ext import commands
import os
from discord.ext.commands.converter import IDConverter
from dotenv import load_dotenv
import datetime
import commands_file
import asyncio

current_time = datetime.datetime.now(datetime.timezone.utc)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='z!', intents=intents, case_insensitive=True)
bot.remove_command('help')
load_dotenv()   
my_secret = os.environ["DISCORD_TOKEN"]

#PRINTA NO CONSOLE QUE ESTÁ CONECTADO
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('z!help'))
    print(f"Conectado como {bot.user.name}#{bot.user.discriminator}")
    print(f"ID do bot: {bot.user.id}")

#COMANDOS ESPECÍFICOS EM CERTOS CHATS (JUNTAR ELE COM O ACIMA)
    """
  chat_atualizações = bot.get_channel(726223906729361438)
  mensagem = await chat_atualizações.send("https://web.archive.org/web/20221111204258if_/https://i.redd.it/8lsbrojwy9d21.jpg")
    """

#EMBED PARA CANAL ESPECIFICO ASSIM QUE O BOT FICAR NO AR:
'''
@bot.event
async def on_ready():
    # Canal onde a mensagem será enviada
    channel_id = 1349532054978822224  # Canal de atualizações: 726223906729361438
    channel = bot.get_channel(channel_id)
    
    # Criação do embed
    embed = discord.Embed(
        title=f"🏆 **PREMIAÇÕES DE MARÇO DO SERVIDOR {(bot.guilds[0].name).lower()}!!** 🏆",
        description=f"Boa noite, aventureiros! É uma honra anunciar nosso novo canal de premiações, o <#1349532054978822224>!\nE para inaugurar essa iniciativa, teremos duas premiações:\n\nA primeira premiação de hoje será para aqueles que jogaram sua primeira campanha de RPG no servidor {(bot.guilds[0].name)}. Jogaram a campanha \"Dies Irae\", do sistema de RPG \"KULT Divindade Perdida\", mestrada presencialmente por <@579295917002457101>.\nEles deixaram o cargo de <@&886008502617780235> e agora são oficialmente <@&939303701892460555> da Socidade do Tridente! <a:luladancing:1349013379372552255>\nParabéns aos nossos premiados:\n<@876821529780973638>\n<@766377882238058546>\n\nComo segunda premiação, também pelo RPG de Kult, serão presenteados os novos <@&939303701892460555> e alguns dos <@&726228738530082876> pela campanha \"Dies Irae\". Eles receberão o mérito <@&1349530453622657105>! <a:letsgoo:1204778517116620800>\nParabéns aos nossos premiados:\n<@579295917002457101>\n<@876821529780973638>\n<@766377882238058546>"
        "\n<@596772923348484142>\n<@1243049618325897216>\n\nParabéns e a todos e aproveitem as aventuras! Lembrando que tem RPG saindo esse mês! E que os dados estejam sempre a seu favor! 🎲 <:cazio:1204778067374112839>\n",
        color=discord.Color.green()

    )
 
    # Definindo o autor como o bot
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    embed.timestamp = current_time

    # Adicionando a imagem do servidor ao footer
    embed.set_footer(text=f"{bot.guilds[0].name}", icon_url=bot.guilds[0].icon.url)
    
    # Enviando o embed para o canal especificado
    await channel.send(embed=embed)
'''
@bot.command()
async def reagir(ctx, mensagem_link, emoji):
    try:
        # Dividindo o link para obter IDs (Servidor, Canal e Mensagem)
        partes = mensagem_link.split("/")
        canal_id = int(partes[-2])  # Penúltima parte é o ID do canal
        mensagem_id = int(partes[-1])  # Última parte é o ID da mensagem

        # Pegando o canal e a mensagem
        canal = bot.get_channel(canal_id)
        if canal is None:
            await ctx.send("Canal não encontrado.")
            return

        mensagem = await canal.fetch_message(mensagem_id)
        if mensagem is None:
            await ctx.send("Mensagem não encontrada.")
            return

        # Reagindo à mensagem
        await mensagem.add_reaction(emoji)
        await ctx.send(f"Reagi à mensagem com '{emoji}'!")

    except Exception as e:
        await ctx.send(f"Ocorreu um erro: {e}")
#AVISO
"""
@bot.command()
async def aviso(ctx):
  embed = discord.Embed(title="**🐸 SAUDAÇÕES JOVENS AVENTUREIROS! 🐸**", description="Sou Cazio, o sapo mago das trevas! Serei o substitudo da <@723651741589176432>, já que meio que ela teve uns problemas de sobrecarregamento de código... Javascript é meio complicado às vezes. Por isso que minha linguagem agora é Python... mas vamos falar de outra coisa...\n\n**O RETORNO DAS CAMPANHAS!**\n Isso mesmo, depois de 763 anos vamos fazer uma campanha física e oficial de D&D, narrada pelo nosso queridíssimo mestre <@518526742449618945>. A seguir, seguem todas as informações:", color=discord.Color.dark_green()) #mandar pro site do CAZIO, adicionar: "url="https://google.com.br", "
  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1368048592569708544/YB4_um_E_400x400.jpg")
  embed.add_field(name="Dia: 16/02, sexta-feira", value="Horário: 19h", inline=True)
  embed.add_field(name="Local: casa do Rhuano", value="O endereço será mandado no [GRUPO SUPREMO DO ZAPZAP](https://chat.whatsapp.com/KSSOG2WlFU63zUeiLduPZn)", inline=True)
  embed.set_footer(text="(Se você ainda não possui ficha, avisa no zapzap o quanto antes)")
  await ctx.channel.send(embed=embed)
  await ctx.send("@here")
"""


# Registrar comandos automaticamente
commands_file.register_commands(bot)
print(f"Comandos carregados: {', '.join([command.name for command in bot.commands])}")


#COMANDOS DE CHAT ABERTO
canais_codigos_permitidos = [1344375658502951026, 848211727903752242, 1271123322733596772, 1359903963943800922]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  #Ignora as mensagens do próprio bot (sem spam!)
    if message.author.id == 723651741589176432:  #Ignora a Megumin
        return
    if message.content.lower().startswith('opa'):  #lower().startswith OU lower().count
        await message.channel.send("Opa, bora um rpgzin?")
    if ('jogar' in message.content.lower() and 'rpg' in message.content.lower()) or ('narrar' in message.content.lower() and 'rpg' in message.content.lower()):
        await message.channel.send("Se quiser jogar ou mestrar um RPG, mande `z!querojogar` ou `z!queronarrar` que eu falo com um dos mestres pra você! <:cazio:1204778067374112839>")
    if message.content.lower().count('cazio'):
        await message.channel.send(
            "Sou o grande Cazio Bot! Digite `z!help` se precisar de ajuda <:cazio:1204778067374112839>"
        )
    if message.content.lower().startswith('z!') and message.channel.id not in canais_codigos_permitidos:
        await message.channel.send("Para usar comandos, vá para o canal <#1271123322733596772>!")
    else:
        await bot.process_commands(message)  #Processa os comandos do bot (z!help, z!ping, etc) e não buga


#MENSAGEM DE BOAS-VIDAS
@bot.event  
async def on_member_join(member):
    genesis = bot.get_channel(740222073712017509)
    leis = bot.get_channel(875917223728922635)
    embed = discord.Embed(title="**E É AQUI QUE SUA AVENTURA COMEÇA...**",
                          color=discord.Color.dark_red())
    embed.set_author(name=member.display_name,
                     icon_url=member.display_avatar.url)
    embed.set_image(
        url=
        "https://i.pinimg.com/originals/9a/4d/60/9a4d60fc3b438877a2dc36da0d066780.gif")
    embed.set_thumbnail(url=member.display_avatar.with_size(1024))
    embed.description = f"**Olá, {member.mention}**, seja bem-vindo(a) ao **{member.guild.name}**. Estamos com **{member.guild.member_count} aventureiros**, um a mais do que ontem!\nLembre-se de ler as {leis.mention} e sinta-se em casa."
    embed.set_footer(text=f"{member.guild.name}")
    await genesis.send(embed=embed)



bot.run(my_secret)