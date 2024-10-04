import moviepy.editor as mp

def create_video_with_text_and_image(audio_file, output_video_file, story_text, image_file):
    # Create a blank video clip (black background)
    video_clip = mp.ColorClip(size=(1280, 720), color=(0, 0, 0), duration=20)

    # Load the audio clip
    audio_clip = mp.AudioFileClip(audio_file)

    # Add text overlay
    txt_clip = mp.TextClip(story_text, fontsize=50, color='white', size=(1280, 200), font='Amiri-Bold', method='caption')
    txt_clip = txt_clip.set_duration(video_clip.duration).set_position('center')

    # Add image overlay
    img_clip = mp.ImageClip(image_file)
    img_clip = img_clip.set_duration(video_clip.duration).resize(height=300).set_position(("center", "bottom"))

    # Combine video, text, and image
    final_video = mp.CompositeVideoClip([video_clip, txt_clip, img_clip])

    # Set the audio of the final video
    final_video = final_video.set_audio(audio_clip)

    # Write the final video to file
    final_video.write_videofile(output_video_file, fps=24)
