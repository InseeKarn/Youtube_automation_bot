import discord
import requests
import os
import nltk
import google.generativeai as genai
from discord.ext import commands
from dotenv import load_dotenv
from cogs.text_to_speech import text_to_speech
from cogs.image_fetcher import fetch_image

nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

load_dotenv()



class StoryIdeas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='get_idea')
    async def get_story_idea(self, ctx, *, prompt="Write an idea"):
        story_idea = await self.create_story_idea(prompt)
        
        if len(story_idea) > 2000:
            chunks = [story_idea[i:i+2000] for i in range(0, len(story_idea), 2000)]
            for chunk in chunks:
                await ctx.send(chunk)
        else:
            await ctx.send(story_idea)
        
        keywords = self.extract_keywords(story_idea)
        image_url = fetch_image(keywords)
        
        await text_to_speech(ctx, story_idea)

        image_url = fetch_image(prompt)
        if image_url:
            await ctx.send(image_url)
        else:
            await ctx.send('Cant find a reach image')

    async def create_story_idea(self, prompt):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if response:
            return response.text
        else:
            return "Cant create idea"
        
    def extract_keywords(self, text):
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))

        keywords = [word for word in words if word.isalnum() and word not in stop_words]

        return ' '.joiin(keywords)
        
def setup(bot):
  bot.add_cog(StoryIdeas(bot))