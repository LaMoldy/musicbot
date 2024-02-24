from utils.cogs import load_cogs
import disnake as discord
from disnake.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @commands.slash_command(name="ping", description="Pings the bot")
    async def ping(self, interaction: discord.ApplicationCommandInteraction) -> None:
        await interaction.response.send_message("Pong!")

    @commands.slash_command(name="author", description="Displays the author of the bot")
    async def author(self, interaction: discord.ApplicationCommandInteraction) -> None:
        await interaction.response.send_message("I was created by LaMoldy")

    @commands.slash_command(name="reload", description="Reloads the commands")
    @commands.default_member_permissions(administrator=True)
    async def reload(self, interaction: discord.ApplicationCommandInteraction) -> None:
        load_cogs(self.bot, True)
        await interaction.response.send_message(
            "Reloading all of the cogs",
            ephemeral = True,
            delete_after = 5
        )

def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(General(bot))

