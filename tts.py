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

label = Label(frame1,text="TEXT TO SPEECH",font=("Arial",30,"bold"),bg="white")
label.place(x=100,y=100)

entry = Entry(frame2,width=30,bd=5,font=15)
entry.place(x=130,y=50)

button = Button(frame2,text="CONVERT",font=("Arial",12,"bold"),bg="red")
button.place(x=220,y=125)

screen.mainloop()
