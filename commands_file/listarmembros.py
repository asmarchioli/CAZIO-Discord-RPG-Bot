from discord.ext import commands

@commands.command()
async def listarmembros(ctx, *role_name):
    if not role_name:
        await ctx.reply(f"Ei, {ctx.author.display_name}, você precisa informar um cargo para listar os membros.")
        return
    
    # Junta os argumentos em uma única stringZ
    role_name_str = " ".join(role_name)
    
    try:
        role = await commands.RoleConverter().convert(ctx, role_name_str)
        guild = ctx.guild
        members = [member for member in guild.members if role in member.roles]
        member_names = "\n".join([member.display_name for member in members])

        if len(members) == 0:
            await ctx.reply("Nenhum membro encontrado com esse cargo.")
            return
        else:
            await ctx.reply(f"Membros com o cargo {role.name}:\n{member_names}")
            return
    except commands.MissingRequiredArgument:
        await ctx.reply(f"Ei, {ctx.author.display_name}, o cargo que você mencionou não foi encontrado. Por favor, verifique e tente novamente.")
