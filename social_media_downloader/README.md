# **Social Media Downloader**

## **Overview**

The **Social Media Downloader** is a powerful, terminal-based tool that allows you to download media from popular platforms like YouTube, Facebook, and Instagram. This project is designed to simplify media downloading by offering a clean interface where you can choose the platform and download media in various formats.

## **Key Features**

- **YouTube Downloader:** Download videos with both audio and video, selecting from available formats, and automatically merging the best available audio with your chosen video quality.
- **Facebook Video Downloader:** Scrapes the webpage to extract and download Facebook videos in MP4 format.
- **Instagram Post Downloader:** Download Instagram photos and videos directly using the post URL.
- **Cross-platform:** Works seamlessly on Windows, macOS, and Linux.

## **Installation**

### **Prerequisites**

Ensure you have **Python 3.x** installed on your system. You can check this by running:

```bash
python --version
```

You also need to install the required libraries. You can do this by running the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

### **Required Python Libraries**

- `yt-dlp` for downloading YouTube videos.
- `instaloader` for downloading Instagram posts.
- `requests` and `beautifulsoup4` for scraping Facebook videos.

## **Usage**

### **Running the Script in Terminal**

1. **Clone or download the project files**.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the script using Python:

    ```bash
    python downloader.py
    ```

4. **Follow the prompts**:
   - Select the platform (YouTube, Facebook, or Instagram) by entering the corresponding number.
   - Enter the media URL.
   - The downloader will fetch the media and save it in the `media/` folder.

### **Building an Executable (Windows)**

If you prefer to run the tool as an executable without needing Python installed, you can convert the Python script into an EXE file using **cx_Freeze**.

1. Install **cx_Freeze**:

    ```bash
    pip install cx_Freeze
    ```

2. Run the following command to create the executable:

    ```bash
    python setup.py build
    ```

3. Find the executable in the `build` folder. Simply double-click the `downloader.exe` file to start the downloader.

### **Post-download Message**

Once the download completes, a message will be displayed confirming the successful download, and the terminal will remain open. You can press **Enter** to close the terminal.

## **Folder Structure**

```plaintext
Social_Media_Downloader/
│
├── downloader.py       # Main script for downloading media
├── requirements.txt    # Python libraries required for the script
├── setup.py            # Script for building the executable using cx_Freeze
├── README.md           # Project instructions and documentation
└── media/              # Folder where downloaded media is saved
```

## **Customization**

### Changing the Download Directory

By default, downloaded media is saved in the `media/` directory. You can change this by modifying the `download_directory` variable in the `downloader.py` script:

```python
download_directory = 'your/custom/path'
```

### Supported Platforms

1. **YouTube:** Downloads video with the best audio and chosen video format.
2. **Facebook:** Extracts and downloads videos from public posts.
3. **Instagram:** Downloads posts using Instaloader for photos and videos.

## **Troubleshooting**

### Common Issues

- **Error: 'ffmpeg' not found**: Ensure `ffmpeg` is installed and available in your system's PATH. This is necessary for merging audio and video streams when downloading from YouTube.
  - Install ffmpeg from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- **Invalid URL error**: Make sure you're using valid URLs from YouTube, Facebook, or Instagram.
- **Permission Denied**: Ensure you have the proper permissions to save files in the download directory.

## **Contributing**

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Final Notes**

The **Social Media Downloader** is a simple, efficient, and flexible tool for downloading media from some of the most popular social platforms. Whether you want to download videos for offline viewing or store Instagram photos, this tool has you covered.

Happy downloading!
