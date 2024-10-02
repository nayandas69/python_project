from downloader import YouTubeDownloader

def main():
    url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download directory (leave empty for current directory): ").strip()

    # If no download path is provided, use current directory
    if not download_path:
        download_path = None

    # Initialize the downloader
    downloader = YouTubeDownloader(url, download_path)

    # List available formats
    formats = downloader.list_formats()

    if formats:
        print("\nAvailable formats:")
        # Display available formats with safety checks for missing values
        for f in formats:
            # Display format details
            format_id = f.get('format_id', 'N/A')
            ext = f.get('ext', 'N/A')
            format_note = f.get('format_note', 'N/A')
            resolution = f.get('resolution', 'N/A')
            filesize = f.get('filesize', 'N/A')
            filesize_str = f"{filesize} bytes" if filesize != 'N/A' else "N/A"
            print(f"{format_id} - {ext} - {format_note} - {resolution} - {filesize_str}")

        # Allow the user to select the format code
        format_code = input("\nEnter the format code to download (leave empty for best quality): ").strip()

        # Start downloading the video with the chosen format
        downloader.download_video(format_code if format_code else None)
    else:
        print("No formats found for this video.")

if __name__ == "__main__":
    main()
