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
