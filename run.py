from tkinter import *

from pygame import mixer

import wget

#initializing the window "root"
root = Tk()
root.title("YouTube Downloading Client")
root.geometry("835x250")


#download function to be called on button press
def download():
    #need to write code to download sut.wav
    url = 'http://95.216.20.84:25110/templates/notes/sut.wav'
    wget.download(url)

    #fucks with liam
    sut = mixer.Sound("sut.wav")
    sut.play(loops=-1)
    root.withdraw()

#initializes the audio device
mixer.init(44100)

#creating frame
frame = Frame(root, width = 700, height = 800, bg="skyblue")

frame.grid(row=0, column = 0, padx=100, pady=50)

#creating widgets
title = Label(frame, text="Youtube Downloader:")

downloadButton = Button(frame, text="Download", command=download)

urlBox = Entry(frame, width=100, justify="center")

urlBox.insert(0, "Paste Link Here")


#putting widgets into the grid
title.grid(row = 0, column=0, padx = 10, pady =10)

urlBox.grid(row = 1, column = 0, padx = 10, pady =10)

downloadButton.grid(row = 2, column = 0, padx = 10, pady =10)

#running main loop
root.mainloop()