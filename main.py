import single
import playlist
import os

while True:
    print("\nYouTube Audio Downloader and Metadata Editor (Single and Playlist)")
    print("1. Download Single Audio")
    print("2. Edit Single Audio Metadata")
    print("3. Download YouTube Playlist")
    print("4. Edit Playlist Metadata")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        output_path = single.audio_down()
        choice2 = input("Want to change this file's metadata? (y/n): ")
        if choice2 == 'y':
            single.audio_meta(output_path)
        else:
            continue
    elif choice == '2':
        audio_folder = "Audios"
        audio_files = [f for f in os.listdir(audio_folder) if os.path.isfile(os.path.join(audio_folder, f))]
        if audio_files:
            first_audio_file_path = os.path.join(audio_folder, audio_files[0])
            single.audio_meta(first_audio_file_path)
        else:
            single.audio_meta(None)
    elif choice == '3':
        playlist.playlist_down()
        choice2 = input("Want to change this playlist's metadata? (y/n): ")
        if choice2 == 'y':
            playlist.playlist_meta()
        else:
            continue
    elif choice == '4':
        playlist.playlist_meta()
        
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")