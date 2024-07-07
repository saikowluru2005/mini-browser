from tkinter import *
import webbrowser

win=Tk()
win.title("Mini browser")
def search():
    url=entry.get()
    webbrowser.open(url)
label1=Label(win,text="Enter URL here : ",font=("arial",10,"bold"))
label1.grid(row=0,column=0)
entry=Entry(win,width=30)
entry.grid(row=0,column=1)
