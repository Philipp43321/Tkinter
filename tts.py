from tkinter import*
from gtts import gTTS
import os
screen = Tk()
screen.geometry("550x500")
#frame for label
frame1 = Frame(screen,bg="red",height=250)
frame1.pack(fill = X)

frame2 = Frame(screen,bg="green",height=300)
frame2.pack(fill=X)

label = Label(frame1,text="TEXT TO SPEECH",font="bold,300",bg="white")
label.place(x=200,y=100)


screen.mainloop()