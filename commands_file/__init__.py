import os
import importlib
from discord.ext import commands

def register_commands(bot):
    commands_folder = os.path.dirname(__file__)
    for filename in os.listdir(commands_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  #Remove .py
            module = importlib.import_module(f"commands_file.{module_name}")
            #Itera pelas funções e registra os comandos
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                #Verifica se a função é um comando válido (@commands.command())
                if callable(attribute) and isinstance(attribute, commands.Command):
                    bot.add_command(attribute)
