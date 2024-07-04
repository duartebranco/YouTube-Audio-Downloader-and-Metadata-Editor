import music_tag
from pytube import YouTube
import os


def audio_down():
    download_folder = "Audios"
    os.makedirs(download_folder, exist_ok=True)

    while True:
        link = input("Enter the YouTube link to download the audio: ")
        try:
            yt = YouTube(link)
            print("\nDownloading audio...")
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream:
                output_path = audio_stream.download(output_path=download_folder)
                print(f"Audio downloaded successfully to '/{download_folder}'")
                return output_path
            else:
                print("No audio streams found! Please try another link.")
                continue
        except Exception as e:
            print(f"Failed to download audio: {e}.\nPlease try again.")


def audio_meta(output_path):
    supported_formats = ['.mp3', '.flac', '.m4a', '.wav', '.wma', '.aac', '.ogg', '.opus', '.mp4']
    while True:
        choice = input(f"\nIs: '{output_path}' your file? (y/n): ")
        if choice == "y":
            name = output_path
        else:
            name = input("Enter the path of the file: ")
        
        if not os.path.exists(name):
            print("File does not exist.")
            continue
        
        file_extension = os.path.splitext(name)[1]
        if file_extension not in supported_formats:
            print("Unsupported file type. Please enter a valid audio file.")
            continue
        
        break

    try:
        audio_file = music_tag.load_file(name)
        audio_file['artist'] = input("Enter the name of the artist (press Enter to skip): ")
        audio_file['title'] = input("Enter the title of the audio (press Enter to skip): ")
        audio_file['album'] = input("Enter the name of the album (press Enter to skip): ")
        audio_file.save()
        print("Metadata changed successfully!!")
    except Exception as e:
        print(f"Error loading file: {e}")
