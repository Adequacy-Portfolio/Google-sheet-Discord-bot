import discord
from discord import ui
from google_api.upload import upload_to_google_sheet
import json

# Chargement du fichier de configuration
with open("configuration.json", "r") as configuration:
    config = json.load(configuration)


def timestamp(created_at):
    return created_at.strftime("%Y-%m-%d %H:%M:%S")


# formulaire de candidature
class Modal(ui.Modal, title="Application du travail"):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timestamp = None
        self.pseudo = None
        self.reason = None
        self.discordid = None

    Pseudo = ui.TextInput(
        label=config["formulaire"]["champ_d'entree_1"]["name"],
        placeholder=config["formulaire"]["champ_d'entree_1"]["espace reserve"],
        style=discord.TextStyle.short,
    )
    ID = ui.TextInput(
        label=config["formulaire"]["champ_d'entree_2"]["name"],
        placeholder=config["formulaire"]["champ_d'entree_2"]["espace reserve"],
        style=discord.TextStyle.short,
    )
    Raison = ui.TextInput(
        label=config["formulaire"]["champ_d'entree_3"]["name"],
        placeholder=config["formulaire"]["champ_d'entree_3"]["espace reserve"],
        style=discord.TextStyle.long,
    )

    # Interaction Form/Sheet
    async def on_submit(self, interaction: discord.Interaction):
        self.timestamp = timestamp(interaction.created_at)
        pseudo = self.Pseudo.value
        reason = self.Raison.value
        id = self.ID.value
        discordid = interaction.user.id
        await interaction.response.send_message(config["formulaire"]["message"])
        data = {
            "DiscordID": str(discordid),
            "ID": id,
            "Pseudo": pseudo,
            "Timestamp": self.timestamp,
            "Reason": reason,
        }
        upload_to_google_sheet(data)
