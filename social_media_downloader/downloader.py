import os
import yt_dlp
import instaloader
import requests
from bs4 import BeautifulSoup

# Create a directory to store downloaded media
download_directory = 'media'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Download YouTube video using yt-dlp ensuring audio and video are combined for any resolution
def download_youtube_video(url):
    ydl_opts = {
        'listformats': True  # Option to list available formats
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract format information without downloading
        info = ydl.extract_info(url, download=False)
        formats = info['formats']

        # List available formats in the terminal
        print("\nAvailable formats (audio+video recommended):")
        for i, format in enumerate(formats):
            height = format.get('height', 'Unknown')
            fps = format.get('fps', 'Unknown')
            vcodec = format.get('vcodec', 'none')
            acodec = format.get('acodec', 'none')
            format_note = format.get('format_note', '')
            print(f"{i + 1}. {format['format_id']} - {format['ext']} - {height}p - {fps}fps - {vcodec} - {acodec} - {format_note}")

        # Ask the user to choose a format by entering the corresponding ID
        choice = input("\nEnter the format ID to download: ")

        # Confirm selection and set options to ensure audio and video are combined
        ydl_opts = {
            'format': f'{choice}+bestaudio/best',  # Download chosen resolution with best available audio
            'merge_output_format': 'mp4',  # Ensure output is in mp4 format
            'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s')
        }

        # Download the video in the selected format
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"\nDownloaded video: {info['title']} with both audio and video.")
        except Exception as e:
            print(f"Error downloading video: {str(e)}")

# Download Instagram posts using instaloader
def download_instagram_post(url):
    try:
        L = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target=download_directory)
        print(f"Downloaded Instagram post from {url}")
    except Exception as e:
        print(f"Failed to download Instagram post: {str(e)}")

# Function to download videos from Facebook (scraping approach)
def download_facebook_video(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find video URL in page source
        video_url = soup.find('meta', property="og:video")['content']
        if video_url:
            video_response = requests.get(video_url)
            file_path = os.path.join(download_directory, 'facebook_video.mp4')
            with open(file_path, 'wb') as f:
                f.write(video_response.content)
            print("Downloaded Facebook video")
        else:
            print("Failed to find video URL")
    except Exception as e:
        print(f"Failed to download Facebook video: {str(e)}")

# Main function with CLI interface
def main():
    while True:
        print("\nSelect the platform to download from:")
        print("1. YouTube")
        print("2. Facebook")
        print("3. Instagram")
        print("4. Exit")
        platform = input("Enter the number: ")

        if platform == '4':
            print("Exiting the downloader. Goodbye!")
            break

        url = input("Enter the URL of the media: ")

        if platform == '1':
            download_youtube_video(url)
        elif platform == '2':
            download_facebook_video(url)
        elif platform == '3':
            download_instagram_post(url)
        else:
            print("Invalid platform")

        # Inform the user that the download is complete
        print("\nDownload complete!")

if __name__ == '__main__':
    main()
