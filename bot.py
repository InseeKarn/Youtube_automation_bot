import asyncio
import moviepy.config as mpc
from cogs.text_to_speech import text_to_speech
from cogs.video_creation import create_video_with_text_and_image
from cogs.story_ideas import get_story_idea
from cogs.image_fetcher import get_free_image
import os
from dotenv import load_dotenv

load_dotenv()  # โหลดข้อมูลจากไฟล์ .env

# Set ImageMagick path
mpc.change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

async def main():
    story_idea = await get_story_idea()
    print("Generated Story Idea:", story_idea)

    # ดึงภาพจาก Unsplash
    image_file = get_free_image(story_idea)  # ใช้ฟังก์ชันที่สร้างขึ้น

    if image_file:
        audio_filename = "story_idea.mp3"
        video_filename = "story_idea_video_with_text_and_image.mp4"

        # Convert text to speech
        text_to_speech(story_idea, audio_filename)

        # Create video with text and image overlay
        create_video_with_text_and_image(audio_filename, video_filename, story_idea, image_file)
    else:
        print("ไม่สามารถดึงภาพได้.")

if __name__ == "__main__":
    asyncio.run(main())
