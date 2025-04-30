from discord.ext import commands
from datetime import datetime

@commands.command()
async def queronarrar(ctx):
    cargo_id = 707275619754311814  # ID do cargo que você deseja buscar
    cargo = ctx.guild.get_role(cargo_id)
    
    if cargo is None:
        await ctx.reply("Não encontrei o cargo especificado!")
        return
    
    hora_atual = datetime.now().hour
    if 6 <= hora_atual < 12:
        saudacao = "Bom dia"
    elif 12 <= hora_atual < 18:
        saudacao = "Boa tarde"
    elif 18 <= hora_atual < 24:
        saudacao = "Boa noite"
    else:
        saudacao = "Boa madruga"

    # Itera por todos os membros da guilda que possuem o cargo
    for membro in cargo.members:
        mensagem = f"{saudacao}, mestre {membro.display_name}! O usuário @{ctx.author} quer narrar uma campanha!"
        try:
            await membro.send(mensagem)
        except Exception as e:
            print(f"Não foi possível enviar mensagem para {membro.name}: {e}")
    
    await ctx.reply("Aprecio sua disposição por narrar! Acabei de mandar mensagem para os <@&707275619754311814> sobre isso! Cazio a seu dispor!")
