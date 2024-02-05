import discord
from discord import app_commands
from discord.ext import commands
import json

# Chargement du fichier de configuration
with open("configuration.json", "r") as configuration:
    config = json.load(configuration)


class Redirect(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    # Redirection of the Acceptence
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id == int(
            config["secret_bot"]["id"]
        ) and message.channel.id == int(config["secret_bot"]["channel"]):
            userID = await self.bot.fetch_user(int(message.content))
            await userID.send(config["secret_bot"]["message"])
            await message.delete()


async def setup(bot):
    await bot.add_cog(Redirect(bot=bot))
