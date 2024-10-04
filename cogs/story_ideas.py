import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# ฟังก์ชันสำหรับสร้างเรื่องราว
async def get_story_idea():
    chat_session = model.start_chat(
        history=[]
    )
    response = chat_session.send_message("Make a stories script for youtube shorts video which is about space, humanity, future, horror.")
    return response.text

# ฟังก์ชันสำหรับส่งข้อความไปยัง Discord
async def send_story_idea(ctx):
    story_idea = await get_story_idea()  # เรียกใช้งานฟังก์ชันเพื่อสร้างเนื้อเรื่อง
    print(story_idea)
    await ctx.send(story_idea)  # ส่งข้อความไปยัง Discord

