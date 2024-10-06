import discord
import os
import moviepy.config as mpc
from dotenv import load_dotenv
from discord.ext import commands
from cogs.story_ideas import StoryIdeas

load_dotenv()

mpc.change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
  await bot.add_cog(StoryIdeas(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  print(f'Message from {message.author}: {repr(message.content)}')

  await bot.process_commands(message)



if __name__ == "__main__":
  bot.run(os.getenv("DISCORD_TOKEN"))