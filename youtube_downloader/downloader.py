import yt_dlp
import os

class YouTubeDownloader:
    def __init__(self, url, download_path=None):
        self.url = url
        self.download_path = download_path if download_path else os.getcwd()

    def list_formats(self):
        """List all available formats for the video."""
        try:
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(self.url, download=False)
                formats = result.get('formats', [])
                return formats
        except Exception as e:
            print(f"An error occurred while fetching formats: {e}")
            return None

    def download_video(self, format_code=None):
        """Download video with the selected format code."""
        ydl_opts = {
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'format': format_code if format_code else 'bestvideo+bestaudio',
            'merge_output_format': 'mp4'  # Ensures audio and video are merged into mp4
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading video from: {self.url}")
                ydl.download([self.url])
                print(f"Download complete! Video saved to {self.download_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
