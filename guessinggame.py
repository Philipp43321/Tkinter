from tkinter import *
from tkinter.ttk import *
from random import randint
from tkinter import messagebox

screen = Tk()
screen.title("Guess!")

def generator():
    x = randint(1,10)
    y = randint (1,10)
    return x,y,x*y 
x,y,product = generator()

def checker():
    try:
        z = int(entry.get())
        if product == z:
            messagebox.showinfo("You won!","You guessed it right, good job!")
        elif product != z:
            messagebox.showerror("You lost","Wrong guess try again.")
    except ValueError:
        messagebox.showerror("Invalid input","Please guess with a valid number.")

def new():
    global x,y,product
    x,y,product = generator()
    question.config(text='Guess the product of {} and ?'.format(x))
    messagebox.showinfo("Guess the number","Random number is {}".format(x))
    entry.delete(0,END)


question = Label(screen,text='Guess the product of {} and ?'.format(x))
question.grid(row = 0, column=0,pady = 5)

entry = Entry(screen,width=10)
entry.grid(row = 1, column=0)

check = Button(screen,text="Check?",command=checker)
check.grid(row=2,column=0)

newgame = Button(screen,text="New Game",command=new)
newgame.grid(row=3,column=0)
#new()
screen.mainloop()