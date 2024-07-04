# YouTube Audio Downloader and Metadata Editor

## Overview
This project provides a simple command-line interface to download audio from YouTube videos and playlists, and to edit the metadata of audio files. 


### single.py
This script contains functions to download a single audio file from a YouTube video and to edit its metadata.

- `audio_down()`: Prompts the user for a YouTube link, downloads the audio, and saves it to the "Audios" folder.
- `audio_meta(output_path)`: Prompts the user to confirm the file path, then allows the user to edit the metadata of the specified audio file.

### playlist.py
This script contains functions to download all audio files from a YouTube playlist and to edit the metadata of the downloaded audio files.

- `playlist_down()`: Prompts the user for a YouTube playlist link, downloads all audio files in the playlist, and saves them to the "Playlists" folder.
- `playlist_meta()`: Allows the user to edit the metadata of all audio files in the "Playlists" folder.

### main.py
This script provides a command-line interface for the user to interact with the functionalities provided in `single.py` and `playlist.py`.

- The user can choose to download a single audio file, edit the metadata of a single audio file, download a YouTube playlist, or edit the metadata of a playlist.

## Usage
1. Run the `main.py` script.
2. Follow the on-screen prompts to choose an action:
   - Download a single audio file from YouTube.
   - Edit the metadata of a single audio file.
   - Download all audio files from a YouTube playlist.
   - Edit the metadata of all audio files in a playlist.
3. Follow the prompts to provide necessary information such as YouTube links, file paths, and metadata details.

## Requirements
- Python 3.x
- `pytube` library
- `music_tag` library
- `os` library (standard library)

## Installation
1. Clone the repository.
2. Install the required libraries using pip:
   ```
   pip install pytube music_tag
   ```
3. Run the `main.py` script to start the program.