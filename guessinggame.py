from tkinter import *
from tkinter.ttk import *
from random import randint
from tkinter import messagebox

screen = Tk()
screen.title("Guess!")

question = Label(screen,text='Guess the product of {} and ?')
question.grid(row = 0, column=0,pady = 5)

entry = Entry(screen,width=10)
entry.grid(row = 1, column=0)

screen.mainloop()