import disnake as discord
from disnake.ext import commands
import youtube_dl

class MusicPlayer(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @staticmethod
    def bot_in_voice_channel(bot, channel) -> bool:
        if bot.voice_clients:
            return True
        return False

    @staticmethod
    async def join_voice_channel(bot, interaction):
        if interaction.author.voice:
            channel = interaction.author.voice.channel
            if MusicPlayer.bot_in_voice_channel(bot, channel):
                return bot.voice_clients[0]
            else:
                await interaction.response.send_message("I have joined the voice channel")
                return await channel.connect()
        else:
            await interaction.response.send_message("There is no active voice channel")

    @commands.slash_command(name="play", description="Plays music")
    async def play_music(self, interaction: discord.ApplicationCommandInteraction, url: str) -> None:
        channel = await MusicPlayer.join_voice_channel(self.bot, interaction)
        if not channel.is_playing():
            if channel:
                ydl_opts = {
                    "format": "bestaudio/best",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality":  "192",
                    }]
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    song_url = info["formats"][0]["url"]

                ffmpeg_options = {
                    "options": "-vn",
                    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
                }

                channel.play(discord.FFmpegPCMAudio(song_url, **ffmpeg_options))
        await interaction.response.send_message("I am already playing a song.")

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
