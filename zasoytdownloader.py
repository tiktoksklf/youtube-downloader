import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
import yt_dlp

def download():
    def run():
        url = url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a YouTube URL.")
            return

        download_btn.config(state='disabled')
        try:
            if format_var.get() == "MP3":
                # Audio only, no conversion (original format)
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                }
            else:
                # Video + audio progressive format (no merging, no ffmpeg needed)
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': '%(title)s.%(ext)s',
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title_var.set(info.get('title', ''))
                messagebox.showinfo("Success", f"Downloaded: {info.get('title', '')}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            download_btn.config(state='normal')

    threading.Thread(target=run).start()

def fetch_thumbnail():
    try:
        url = url_entry.get().strip()
        if not url:
            return
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            thumb_url = info.get('thumbnail')
            title_var.set(info.get('title', ''))

        if thumb_url:
            response = requests.get(thumb_url)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((160, 90))
            img = ImageTk.PhotoImage(img_data)
            thumbnail_label.config(image=img)
            thumbnail_label.image = img
    except Exception:
        thumbnail_label.config(image='', text='')

root = tk.Tk()
root.title("YouTube Downloader (yt-dlp)")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#222222")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#0078D7", foreground="white", font=("Segoe UI", 10))
style.configure("TLabel", background="#222222", foreground="white", font=("Segoe UI", 10))

tk.Label(root, text="YouTube URL:", bg="#222222", fg="white", font=("Segoe UI", 12)).pack(pady=(20, 5))
url_entry = tk.Entry(root, font=("Segoe UI", 10), width=40)
url_entry.pack(pady=5)

ttk.Button(root, text="Preview Video", command=fetch_thumbnail).pack(pady=5)

thumbnail_label = tk.Label(root, bg="#222222")
thumbnail_label.pack(pady=5)

title_var = tk.StringVar()
ttk.Label(root, textvariable=title_var, wraplength=300).pack(pady=(5, 2))

format_var = tk.StringVar(value="MP4")
ttk.Combobox(root, textvariable=format_var, values=["MP4", "MP3"], state="readonly").pack(pady=10)

download_btn = ttk.Button(root, text="Download", command=download)
download_btn.pack(pady=10)

root.mainloop()
