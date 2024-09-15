
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(youtube_url, output_path='video'):
    yt = YouTube(youtube_url,on_progress_callback = on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=output_path)
    path = yt.title+'.mp4'
    return path


file_path = 'test_videos.txt'

# Read the links from the file
with open(file_path, 'r') as file:
    youtube_links = file.readlines()

# Remove any extra whitespace (like newlines)
youtube_links = [link.strip() for link in youtube_links if link.strip()]

# Download each video
for link in youtube_links:
    try:
        download_youtube_video(link)
        print(f"Downloaded video from: {link} - {download_youtube_video(link)} ")
    except Exception as e:
        print(f"Failed to download video from: {link}. Error: {e}")

# video_path = download_youtube_video("https://www.youtube.com/watch?v=9qjk-Sq415s&list=PL5B0D2D5B4BFE92C1&index=7")   
# print(video_path)