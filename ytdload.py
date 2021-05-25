def click_func():
    url=yt_url.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror('error','pytube did not service or url is wrong')
        return
    urls=m.get_urls(url)
    if urls and messagebox.askyesno('checkbox','download all the video in the list?'):
        print('start to download')
        for u in urls:
            threading.Thread(target=m.start_dload,
                             args=(u,listbox)).start()
    else:
        yt=YouTube(url)
        if messagebox.askyesno('checkbox',
                              f'donwload{yt.title} or not?'):
            threading.Thread(target=m.start_dload,
                             args=(url,listbox)).start()
        else:
            print('cancel')
import ytube_module as m
import tkinter as tk
from tkinter import *
from pytube import YouTube
import threading
window=tk.Tk()
window.geometry('480x360')
window.title("Youtube Download")
#window.config(bg="light blue")

input_fm=tk.Frame(window,bg='light yellow',width=480,height=120)
input_fm.pack()

lb=tk.Label(input_fm,text='Please insert a URL',fg='black',font=('Arial',12))
lb.place(rely=0.25,relx=0.5,anchor='center')

yt_url=tk.StringVar()
entry=tk.Entry(input_fm,textvariable=yt_url,width=45)
entry.place(rely=0.5,relx=0.5,anchor='center')

btn=tk.Button(input_fm,text='download',command=click_func,bg='Gray',fg='Black')
btn.place(rely=0.5,relx=0.91,anchor='center')

dload_fm=tk.Frame(window,bg='light blue',width=480,height=240)
dload_fm.pack()

lb=tk.Label(dload_fm,text='State',
            fg='black',font=('Arial',12))
lb.place(rely=0.1,relx=0.5,anchor='center')

listbox=tk.Listbox(dload_fm,width=45,height=10)
listbox.place(rely=0.5,relx=0.5,anchor='center')

sbar=tk.Scrollbar(dload_fm)
sbar.place(rely=0.5,relx=0.81,anchor='center',relheight=0.65)

window.mainloop()