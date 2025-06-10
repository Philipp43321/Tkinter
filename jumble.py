from tkinter import *
import random
from tkinter import messagebox
screen= Tk()
#list of correct words
correct = ["plant","dog","mouse","cat","keyboard","zombie","battery","screen","microphone","speaker"]
#list of jumbled words
jumbled = ["anplt","ogd","euoms","atc","dkreyaob","omzieb","tatyreb","ercsen","rohonpcmie","rsepeka"]

picker = random.randint(0,9)
#variables
score = 0
attempts = 0
ss = ""
scoretext = Label(screen)

def words():
    global correct,jumbled,picker
    word.config(text=jumbled[picker])

def checker():
    global jumbled,correct,picker,score,attempts,ss,scoretext
    attempts += 1
    answer = text.get()
    if answer ==correct[picker]:
        messagebox.showinfo("correct","you answered the question right!")
        score +=1
    else:
        messagebox.showerror("wrong","you did not answer correctly")
    ss="score:"+str(score)+"/"+str(attempts)
    scoretext=Label(screen,text=ss,font=("arial",15))
    scoretext.place(x=0,y=70)
    reset()
def reset():
    global jumbled,correct,picker
    picker = random.randint(0,9)
    word.config(text=jumbled[picker])
    text.delete(0,END)



screen.geometry("400x500")

title = Label(screen,text="JUMBLED WORD GAME",font=("arial",20))
title.place(x=40,y=20)

text = Entry(screen,width=20,bg="gray",font=("arial",20))
text.place(x=50,y=200)

check = Button(screen,text="Check",font=("arial",20),bg="green",command=checker)
check.place(x=150,y=250)

restart = Button(screen,text="Skip",font=("arial",20),bg="yellow",command=reset)
restart.place(x=150,y=320)

word=Label(screen,text="",font=("arial",15),bg="orange")
word.place(x=150,y=100)

words()

screen.mainloop()