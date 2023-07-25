import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

win = Tk()
win.title("MP3 Music Player")
win.geometry("920x600+290+85")
win.resizable(False, False)
mixer.init()
image_icon = PhotoImage(file="D:\TechnoHacks/ic_bg.png")
win.iconphoto(False, image_icon)

botom = PhotoImage(file="D:\TechnoHacks/bg_Music.png")
Label(win, image=botom, bg="#0f1a2b").pack()

ButtonFolder = PhotoImage(file="D:\TechnoHacks/folder.png")
Button(win, image=ButtonFolder, bg="black", bd=0,command=AddMusic).place(x=150, y=400)

ButtonPlay = PhotoImage(file="D:\TechnoHacks/play.png")
Button(win, image=ButtonPlay, bg="black", bd=0,command=PlayMusic).place(x=250, y=400)

ButtonStop = PhotoImage(file="D:\TechnoHacks/stop.png")
Button(win, image=ButtonStop, bg="black", bd=0,command=mixer.music.stop).place(x=550, y=400)

ButtonResume = PhotoImage(file="D:\TechnoHacks/resume.png")
Button(win, image=ButtonResume, bg="black", bd=0,command=mixer.music.unpause).place(x=450, y=400)

ButtonPause = PhotoImage(file="D:\TechnoHacks/pause.png")
Button(win, image=ButtonPause, bg="black", bd=0,command=mixer.music.pause).place(x=350, y=400)

ButtonExit = PhotoImage(file="D:\TechnoHacks/exit.png")
Button(win, image=ButtonExit, bg="black", bd=0,command=win.destroy).place(x=650, y=400)

Frame_Music = Frame(win, bd=8, relief=RAISED)
Frame_Music.place(x=205, y=120, width=500, height=200)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Aloja", 10), bg="#000000",fg="white", selectbackground="#21b3de", cursor="hand2", bd=0)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
win.mainloop()