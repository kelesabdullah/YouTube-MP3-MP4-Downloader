import tkinter as tk
from tkinter import messagebox
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
from tkinter.ttk import *
import pytube

window = tk.Tk()
window.geometry('500x250')
icon = PhotoImage(file="erhan-ufak-kimdir-1280x720.png")
window.iconphoto(False,icon)


window.resizable(0,0)

window.title("Youtube Video Downloader V1.1 August 17")
tk.Label(window, text ="Youtube Video Downloader", font ="arial 20 bold").pack()
link = tk.StringVar()

checkmp4ormp3 = tk.IntVar()
checkmp4ormp3.set(1)
tk.Label(window, text ="Linki buraya yapıştır", font ="arial 15 bold").place(x=10, y=80)
link_error = tk.Entry(window, width =70, textvariable = link).place(x =10, y=110)
mp4check = ttk.Radiobutton(window,text="MP4 OLARAK İNDİR",variable=checkmp4ormp3,value=1).pack()
mp3check = ttk.Radiobutton(window,text="MP3 OLARAK İNDİR",variable=checkmp4ormp3,value=2).pack()
def Downloader():
    checker = checkmp4ormp3.get()
    if checker==1:
        try:
            url =YouTube(str(link.get()))
            video =url.streams.get_highest_resolution()
            dosyayolu = pathsave()   
            video.download(dosyayolu)
            messagebox.showinfo("Youtube Video Downloader V1.2 August 17",f"{video.title}\nYükleme tamamlandı.\n Kaydedilen dizin: \n {dosyayolu}")
        except pytube.exceptions.RegexMatchError:
            messagebox.showerror("Youtube Video Downloader V1.2 August 17","Hatalı link girişi!")
        
        
        
                

    else:
        try:

            yt = YouTube(str(link.get()))
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(pathsave())
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            messagebox.showinfo("Youtube Video Downloader V1.2 August 17",f"{video.title}\nYükleme tamamlandı.\n Kaydedilen dizin: \n {downloaded_file}")
        except pytube.exceptions.RegexMatchError:
            messagebox.showerror("Youtube Video Downloader V1.2 August 17","Hatalı link girişi!")
        
            
        
                


def pathsave():
    return filedialog.askdirectory()


downloadbutton = ttk.Button(window,text ="DOWNLOAD", command =Downloader).place(x=200, y=150,height=40,width=100)
window.mainloop()
