from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr

screen = Tk()
screen.title("Speech To Text")
screen.geometry("550x300")

def stt():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        popup.config(text="You can speak now")
        screen.update()
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
        except:
            text = "No input detected"
        textbox.delete(1.0,END)
        textbox.insert(END,text)

def saveinput():
    audiosave = filedialog.asksaveasfile(defaultextension=".txt")
    if audiosave:
        audiosave.write(textbox.get(1.0,END))
        audiosave.close()
    else:
        messagebox.showinfo("Error","Text not saved")

popup = Label(screen,text="",font=("arial",12))
popup.place(x=190,y=250)

label = Label(screen,text="Voice Notepad",font=("arial",30))
label.place(x=150,y=20)

startbutton = Button(screen,text="Click on me!... \n To start recording",font=("arial",15),command=stt)
startbutton.place(x=5,y=100)

textbox = Text(screen,height=5,width=20)
textbox.place(x=200,y=100)

savebutton = Button(screen,text="Save the text",font=("arial",15),command=saveinput)
savebutton.place(x=380,y=100)
screen.mainloop()