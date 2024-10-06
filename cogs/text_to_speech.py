import pyttsx3
import discord

class TextToSpeech(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='tts')
  async def text_to_speech(self, ctx, *, text):
    engine = pyttsx3.init()


    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)


    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    

    await ctx.send(file=discord.File('output.mp3'))  
    
