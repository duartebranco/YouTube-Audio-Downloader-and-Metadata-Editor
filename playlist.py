import music_tag
from pytube import Playlist, YouTube
import os


def playlist_down():
    download_folder = "Playlists"
    os.makedirs(download_folder, exist_ok=True)

    while True:
        playlist_link = input("Enter the YouTube playlist link to download: ")
        playlist = Playlist(playlist_link)
        try:    
            print(f"\nDownloading: {playlist.title} to '/{download_folder}'")
            break
        except Exception as e:
            print(f"Error downloading playlist: {str(e)}")
            continue
    
    for video_url in playlist.video_urls:
        try:
            yt = YouTube(video_url)
            print(f"\nDownloading: {yt.title}")
            audio_stream = yt.streams.filter(only_audio=True).first()
            output_path = audio_stream.download(output_path=download_folder)
            print(f"Audio downloaded successfully to '/{download_folder}'")
        except Exception as e:
            print(f"Error downloading {video_url}: {str(e)}")
        
    print("\nPlaylist downloaded successfully!")

def playlist_meta():
    print("This will edit metadata for all files in the '/Playlists' folder.")
    album = input("Enter album name (press Enter to skip): ")
    artist = input("Enter artist name (press Enter to skip): ")
    year = input("Enter year (press Enter to skip): ")
    
    for filename in os.listdir('Playlists'):
        supported_formats = ['.mp3', '.flac', '.m4a', '.wav', '.wma', '.aac', '.ogg', '.opus', '.mp4']
        if any(filename.endswith(ext) for ext in supported_formats):
            print(f"\nEditing metadata for: {filename}")
            path = os.path.join('Playlists', filename)
            audio_file = music_tag.load_file(path)
            
            if album: audio_file['album'] = album
            if artist: audio_file['artist'] = artist
            if year: audio_file['year'] = year
            
            title = input(f"Enter title for {filename} (press Enter to use filename): ")
            audio_file['title'] = title.strip() if title else os.path.splitext(filename)[0]
            
            audio_file.save()
            print(f"Updated metadata for: {filename}")
    
    print("Metadata changed successfully!")

