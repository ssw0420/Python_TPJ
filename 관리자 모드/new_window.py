from tkinter import *
import tkinter.ttk as ttk

app = Tk()

def new_window():
    global new
    new = Toplevel()

making_window_btn = Button(app, text = "새창만들기", command = new_window)
making_window_btn.pack(pady = "5")

app.title('scribblinganything.tistory.com')
app.geometry("200x50")

app.mainloop()
