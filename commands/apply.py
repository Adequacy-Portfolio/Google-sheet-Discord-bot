import discord
from discord import app_commands
from discord.ext import commands
from view.modal import Modal
import json

# Chargement du fichier de configuration
with open("configuration.json", "r") as configuration:
    config = json.load(configuration)


class Application(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    # Slash command to create the Application Form
    @app_commands.command(
        name=config["command"]["nom"], description=config["command"]["description"]
    )
    async def apply(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal())


async def setup(bot):
    await bot.add_cog(Application(bot=bot))
