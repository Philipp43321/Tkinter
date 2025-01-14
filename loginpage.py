from tkinter import *
screen=Tk()
screen.geometry("400x280")
screen.config(background="gray")
#gui elements
username = Label(screen,text="username").place(x=100,y=80)
password = Label(screen,text="password").place(x=100,y=130)
login = Label(screen,text="login",background="gray").place(x=200,y=30)
usernameentry = Entry(screen,width=15).place(x=160,y=80)
passwordentry = Entry(screen,show="*",width=15).place(x=160,y=130)
submit = Button(screen,text="SUBMIT",command=screen.destroy).place(x=190,y=170)

screen.mainloop()
