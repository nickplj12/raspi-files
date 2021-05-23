from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import os
import vlc


filetoplay = ''

vlc_obj = vlc.Instance()
player = vlc_obj.media_player_new()

def selfile():
       global filetoplay
       fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select file", filetypes=(("Music File", "*.mp3 *.wav *.ogg *.wma"), ("Video File", "*.mp4 *.mov *.flv"), ("Picture File", "*.png *.jpg *.jpeg"), ("All FIles", "*.*")))
       txt.set(os.path.basename(fln))
       filetoplay = fln

def playmusic():
       if filetoplay == "":
           messagebox.showerror(title="nepmp", message="please select a file")
           return False
       track = vlc_obj.media_new(filetoplay)
       player.set_media(track)
       player.play()

def stopmusic():
       player.stop()

root = Tk()

txt = StringVar()
txt.set("no file selected")

root.title("nicks epic python media player")

wrapper = LabelFrame(root, text = "the media player")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(wrapper, textvariable=txt)
lbl.pack()

btn1 = Button(wrapper, text="open file", command=selfile)
btn1.pack(side=LEFT, anchor=W, padx=10)

btn2 = Button(wrapper, text="open/play", command=playmusic)
btn2.pack(side=LEFT, anchor=W, padx=5)

btn3 = Button(wrapper, text="unshow/stop", command=stopmusic)
btn3.pack(side=LEFT, anchor=W, padx=5)

btn4 = Button(wrapper, text="exit", command=lambda: exit())
btn4.pack(side=LEFT, anchor=W, padx=5)


    

root.geometry("400x150")
root.resizable(False,False)
root.mainloop()