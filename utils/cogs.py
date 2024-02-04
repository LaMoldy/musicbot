import os
from disnake.ext import commands

def load_cogs(bot: commands.InteractionBot, reload: bool = False) -> None:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if reload is True:
                bot.reload_extension(f"cogs.{filename[:-3]}")
            else:
                bot.load_extension(f"cogs.{filename[:-3]}")
