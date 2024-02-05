import discord
from discord.ext import commands
import json
import os

# Chargement du fichier de configuration
with open("configuration.json", "r") as configuration:
    config = json.load(configuration)

token = config["bot"]["token"]
command_prefix = "!"


# Bot Core
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix=command_prefix)

    # Chargement de modules
    async def setup_hook(self):
        for file in os.listdir("./commands"):
            if file.endswith(".py"):
                await self.load_extension(f"commands.{file[:-3]}")
        for file in os.listdir("./events"):
            if file.endswith(".py"):
                await self.load_extension(f"events.{file[:-3]}")


# Lancement du bot
Bot().run(token=token)
