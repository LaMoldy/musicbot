import disnake as discord
from disnake.ext import commands

class MusicPlayer(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @commands.slash_command(name="play", description="Plays music")
    async def play_music(self, interaction: discord.ApplicationCommandInteraction, song_name: str) -> None:
        # TODO:Place music playing code here
        pass

    @commands.slash_command(name="pause", description="Pauses the music")
    async def pause_music(self, interaction: discord.ApplicationCommandInteraction) -> None:
        # TODO:Pauce the music playing code here
        pass

    @commands.slash_command(name="stop", description="Stops the music")
    async def stop_music(self, interaction: discord.ApplicationCommandInteraction) -> None:
        # TODO:Stop the music
        pass

def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(MusicPlayer(bot))
