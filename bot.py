import dotenv
import os
import disnake as discord

from disnake.ext import commands
from utils.cogs import load_cogs

# Load the environment variables
dotenv.load_dotenv()

# Setup command sync
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

# Create the intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Sets the bot activity
activity = discord.Activity(name="to Music", type=discord.ActivityType.listening)

# Setup the bot
bot = commands.InteractionBot(
    command_sync_flags = command_sync_flags,
    intents = intents,
    activity = activity
)

# Load the cogs
print("Loading cogs...")
load_cogs(bot)

# Get the token and run the bot
token = ""
environment = os.getenv("ENVIRONMENT")
if environment == "prod":
    token = os.getenv("PROD_TOKEN")
else:
    token = os.getenv("DEV_TOKEN")

# Run the bot
print("Attempting to run server")
bot.run(token)
