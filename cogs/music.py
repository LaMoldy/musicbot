import disnake as discord
from disnake.ext import commands

class MusicPlayer(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @commands.slash_command(name="play", description="Plays music")
    async def play_music(self, interaction: discord.ApplicationCommandInteraction, song_name: str):
        try:
            channel = interaction.author.voice.channel
            await channel.connect()
            # TODO: Place music code here
            await interaction.response.send_message("I have joined the voice channel")
        except Exception as error:
            print(error)
            await interaction.response.send_message("There was an error joining the voice chat")

    @commands.slash_command(name="stop", description="Stops the music")
    async def stop_music(self, interaction: discord.ApplicationCommandInteraction) -> None:
        try:
            # Don't think this is how you do it properly
            connections = interaction.client.voice_clients

            # TODO: Place destruction of music player here

            for connection in connections:
                await channel.disconnect()
            await interaction.response.send_message("I have left the voice channel.")
        except Exception as error:
            print(error)
            await interaction.response.send_message("There was an error leaving the voice chat.")

def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(MusicPlayer(bot))
