import asyncio
import moviepy.config as mpc
from cogs.text_to_speech import text_to_speech
from cogs.video_creation import create_video_with_text_and_image
from cogs.story_ideas import get_story_idea
from moviepy.editor import TextClip

# Set ImageMagick path
mpc.change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.x.x-Q16-HDRI\magick.exe"})


async def main():
    story_idea = await get_story_idea()
    print("Generated Story Idea:", story_idea)

    audio_filename = "story_idea.mp3"
    video_filename = "story_idea_video_with_text_and_image.mp4"
    image_file = "your_image.png"  # Replace with the path to your image

    # Convert text to speech
    text_to_speech(story_idea, audio_filename)

    # Create video with text and image overlay
    create_video_with_text_and_image(audio_filename, video_filename, story_idea, image_file)

if __name__ == "__main__":
    asyncio.run(main())

# Create a text clip to test
txt_clip = TextClip("Hello, World!", fontsize=70, color='white', size=(640, 480))
txt_clip.save_frame("test_frame.png")  # This should create an image file

print("TextClip created successfully!")