import disnake as discord
from disnake.ext import commands

class MusicPlayer(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @staticmethod
    def bot_in_voice_channel(bot, channel) -> bool:
        if bot.voice_clients:
            return True
        return False



    @commands.slash_command(name="play", description="Plays music")
    async def play_music(self, interaction: discord.ApplicationCommandInteraction, url: str) -> None:
        if interaction.author.voice:
            channel = interaction.author.voice.channel
            if MusicPlayer.bot_in_voice_channel(self.bot, channel):
                await interaction.response.send_message("I am already in the voice channel")
            else:
                await channel.connect()
                await interaction.response.send_message("I have join the voice channel")
        else:
            await interaction.response.send_message("There is no active voice channel")

    @commands.slash_command(name="stop", description="Stops the music")
    async def stop_music(self, interaction: discord.ApplicationCommandInteraction) -> None:
        if self.bot.voice_clients:
            for voice_client in self.bot.voice_clients:
                if interaction.author.voice.channel == voice_client.channel:
                    await voice_client.disconnect()
                    await interaction.response.send_message("I have left the voice channel")
                else:
                    await interaction.response.send_message(f"I am not in the same channel as you, {interaction.author.name}")

def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(MusicPlayer(bot))
