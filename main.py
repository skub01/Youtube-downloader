import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import certifi
import ssl

# Set the SSL certificate path
ssl._create_default_https_context = ssl._create_unverified_context
ssl._DEFAULT_CERT_FILE = certifi.where()

def startDownload():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        progressBar.set(0.0)
        progressBar.pack(padx=10, pady=10)
        video.download()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="Downloaded!")
        download.configure(text="Start new download")
    except RegexMatchError: 
        finishLabel.configure(text="Invalid YouTube link!")
    except Exception as e:
        finishLabel.configure(text=f"An error occurred: {str(e)}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements 
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percent
pPercentage = customtkinter.CTkLabel(app, text="")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
