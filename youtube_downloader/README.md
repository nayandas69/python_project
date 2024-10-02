# YouTube Video Downloader

This is a simple Python-based YouTube video downloader using `yt-dlp`. It allows users to download YouTube videos by selecting their preferred format (audio or video) and saving it to a specified directory.

## Features
- **Format Selection**: Users can choose the format (resolution, audio, video) they want to download.
- **Custom Download Directory**: Videos can be saved to a user-specified directory, or default to the current directory.
- **Automatic Merging**: If the video and audio are separate, they will be merged into a single file (mp4).
- **Error Handling**: Handles missing format details and download errors smoothly.

## Requirements

- Python 3.7+
- `yt-dlp`
- `ffmpeg` (optional but recommended for merging audio and video)

## Installation

### 1. Clone the repository:

```bash
git clone 
cd youtube-downloader
```

### 2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install `yt-dlp` and any other necessary dependencies.

### 3. (Optional) Install `ffmpeg`:

To ensure smooth merging of audio and video streams, it’s recommended to install `ffmpeg`. You can download it from the [official site](https://ffmpeg.org/download.html) and add it to your system's PATH.

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Follow the prompts**:

   - Paste the **YouTube URL** when prompted.
   - Specify the **download directory** (or leave it empty to download to the current directory).
   - Select the desired format from the list of available formats.

3. **Download the video**:

   The selected video will be downloaded and saved to the specified location.

### Example

```bash
Enter the YouTube video URL: https://youtu.be/f8bOKEwXZJo?si=7-9D2EeGo74wuJsT
Enter the download directory (leave empty for current directory): 
Available formats:
18 - mp4 - 360p - 640x360 - 221k - 21.26MiB
22 - mp4 - hd720 - 1280x720 - 471k - 50.23MiB
140 - m4a - audio only - N/A - 128k - 4.5MiB

Enter the format code to download (leave empty for best quality): 18
Downloading video from: https://youtu.be/f8bOKEwXZJo?si=7-9D2EeGo74wuJsT
Download complete! Video saved to /path/to/download
```

## Project Structure

```
youtube_downloader/
│
├── downloader.py        # Core logic for listing formats and downloading videos
├── main.py              # Main script to run the downloader
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Known Issues

- Ensure that **`ffmpeg`** is installed if you encounter issues with merging video and audio formats.
- Some formats may not provide a `filesize` field; in those cases, the downloader handles it gracefully by showing `N/A`.

## License

This project is licensed under the MIT License.

## Credits

This project uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading functionality.

