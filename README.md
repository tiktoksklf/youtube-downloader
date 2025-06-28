# YouTube Downloader (Python)

A simple graphical YouTube downloader built in Python, using `yt-dlp`, `tkinter`, and `pillow`.  
Designed to be easy to use with a clean GUI and no extra dependencies like FFmpeg required for basic downloads.

---

## Features

- Download YouTube videos as MP4 (progressive format, no merging required)  
- Download audio-only files in original format (no conversion, no FFmpeg needed)  
- Preview video thumbnail and title before downloading  
- GUI built with Tkinter for ease of use  
- Saves files automatically to your Documents folder (configurable)  
- Supports multiple formats: MP4 video and MP3 audio (actually best audio format downloaded, no actual MP3 conversion)  

---

## Requirements

- Python 3.7 or newer  
- Python packages:
  - `yt-dlp` — YouTube downloading backend  
  - `pillow` — Image processing (thumbnail display)  
  - `requests` — HTTP requests for thumbnails

Install required packages via:

```bash
pip install yt-dlp pillow requests
tkinter: Usually included in Python on Windows/macOS.

Linux users may need to install it separately, e.g., on Ubuntu/Debian:

bash
Copy
Edit
sudo apt-get install python3-tk
Installation
Download or clone the repository.

Make sure Python and dependencies are installed.

Run the script:

bash
Copy
Edit
python zasoytdownloader.py
How to Use
Paste a YouTube video URL into the input box.

Click Preview Video to load and display the video’s thumbnail and title.

Choose download format:

MP4 for video (includes audio, no extra software required)

MP3 for audio only (downloads original audio format, e.g., .webm or .m4a, no conversion)

Click Download.

The file downloads to your Documents folder (or configured folder).

A popup message confirms when the download completes.

Important Details and Limitations
The MP4 download uses YouTube’s progressive formats, which already include audio and video combined — so no FFmpeg is needed to merge.

Audio-only download saves the best audio stream without converting to MP3 (so the extension may be .webm or .m4a). This is compatible with most modern media players.

If you want full MP3 conversion or advanced features, FFmpeg installation is required (not included).

The downloader does not bypass any YouTube restrictions, age gates, or geo-blocks.

Downloading copyrighted content without permission may violate YouTube’s Terms of Service. Use responsibly.

Where Are Files Saved?
By default, downloads save to your Documents folder:

Windows: C:\Users\<YourUsername>\Documents

macOS/Linux: /Users/<YourUsername>/Documents or /home/<YourUsername>/Documents

You can change this folder by modifying the download_folder variable in the script.

Troubleshooting
Permission Denied Errors:

Run the script with Administrator privileges or ensure the script saves to a folder where you have write permissions.

Change the download folder to a writable directory.

Missing tkinter:

On Linux, install python3-tk package.

On Windows/macOS, reinstall Python with tcl/tk support enabled.

FFmpeg Warnings:

These are harmless unless you want video+audio merging or format conversions.

To remove warnings, install FFmpeg from ffmpeg.org and add it to your system PATH.

Network Issues or YouTube Errors:

Some videos may be geo-restricted, private, or age-restricted and won’t download.

Check your internet connection.

How to Run as Administrator (Windows)
Open Start Menu, type cmd, right-click Command Prompt, and select Run as administrator.

Run the script via command line:

bash
Copy
Edit
python "C:\path\to\zasoytdownloader.py"
License
This project is licensed under the MIT License. Feel free to use, modify, and share!

Disclaimer
This tool is provided as-is without warranty.

Downloading copyrighted videos may violate YouTube’s Terms of Service and local laws.

The author is not responsible for misuse or legal consequences.

Contributing
Contributions, bug reports, and feature requests are welcome! Please open issues or submit pull requests on GitHub.

Acknowledgments
yt-dlp — Powerful YouTube downloading backend

Python’s tkinter — GUI toolkit

Pillow and Requests — For thumbnail handling

Contact
Feel free to reach out with questions or feedback!

Thank you for using this YouTube Downloader!

yaml
Copy
Edit
