import discord
from discord import app_commands
from discord.ext import commands
import json

# Chargement du fichier de configuration
with open("configuration.json", "r") as configuration:
    config = json.load(configuration)


class OnReady(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        await self.bot.change_presence(
            activity=discord.CustomActivity(name=config["bot"]["status"])
        )

        print("Connexion réussie! ")


async def setup(bot):
    await bot.add_cog(OnReady(bot=bot))
