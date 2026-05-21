import yt_dlp
import os

# Get the exact folder path where ytdown.py is located
SAVE_PATH = os.path.dirname(os.path.abspath(__file__))

video_link = input("Please enter the video URL: ")

ydl_args = {
    'format': 'best',
    # Tell yt-dlp to save the file inside this exact folder
    'outtmpl': os.path.join(SAVE_PATH, '%(title)s.%(ext)s'),
    'nocheckcertificate': True,
    'quiet': False,
    'no_warnings': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_args) as ydl:
        print("Download started...")
        ydl.download([video_link])
    print("Download successful!")
except Exception as e:
    print(f"An error occurred: {e}")