import yt_dlp
import pywhatkit

def YouTubeDownloader(url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert audio to mp3
            'preferredquality': '192',  # Set the preferred quality (bitrate)
        }],
        'outtmpl': f'{output_path}/audio',  # Set output template (optional)
    }
    # Download the video and extract audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def PlayOnYouTube(topic):
    return pywhatkit.playonyt(topic, open_video=False)
