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
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        finishLabel.configure(text="Downloaded!")
    except RegexMatchError: 
        print("Invalid YouTube link!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

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

#Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()