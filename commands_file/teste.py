import discord
from discord import app_commands
from discord.ext import commands

# Definição de um comando simples de teste
class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="teste", description="Comando de teste para verificar funcionamento.")
    async def teste(self, interaction: discord.Interaction):
        await interaction.response.send_message("O comando de teste está funcionando corretamente! 🚀", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Teste(bot))
