import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googleapiclient.discovery import build

# โหลดค่าในไฟล์ .env
load_dotenv()

# ค่า Token และ API Key จาก .env
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# กำหนด intents และสร้าง instance ของ bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ฟังก์ชันสำหรับค้นหาวิดีโอจาก YouTube
def search_youtube_video(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        part='snippet',
        maxResults=1,
        q=query
    )
    response = request.execute()
    if response['items']:
        video = response['items'][0]
        return f"https://www.youtube.com/watch?v={video['id']['videoId']}"
    return "ไม่พบวิดีโอที่ค้นหา"

# เมื่อบอทพร้อมทำงาน
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# คำสั่งสำหรับการค้นหาวิดีโอใน YouTube
@bot.command(name='search', help='ค้นหาวิดีโอบน YouTube')
async def search(ctx, *, query):
    video_url = search_youtube_video(query)
    await ctx.send(f'เจอวิดีโอ: {video_url}')

# เริ่มการทำงานของบอท
bot.run(DISCORD_TOKEN)
