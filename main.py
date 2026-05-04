import yt_dlp

url = input("Please paste your YouTube link: ")

settings = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    # මෙන්න මේ පේළිය තමයි වැදගත්ම!
    # ඔයා පාවිච්චි කරන්නේ Chrome නම් 'chrome' කියලා තියන්න.
    # Microsoft Edge නම් 'edge' කියලා වෙනස් කරන්න.
    'cookiesfrombrowser': ('chrome', ), 
    
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    print("Verifying with cookies and starting download...")
    with yt_dlp.YoutubeDL(settings) as downloader:
        downloader.download([url])
    print("Finally! Your MP3 is ready.")
except Exception as error:
    print(f"Still having trouble: {error}")