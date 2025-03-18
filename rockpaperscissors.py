from tkinter import*
import tkinter.font as font
import random
screen = Tk()

#creating functions
playerscore = 0
computerscore = 0
selection = [("rock",0),("paper",1),("scissors",2)]

def compchoice():
    return random.choice(selection)

def tie():
    global playerscore,computerscore
    changingtext.config(text="It is a tie, nobody gets a point",fg="gray")
    compscore.config(text="Computer's score: "+str(computerscore))
    youscore.config(text="Your score: "+str(playerscore))

def compwin():
    global playerscore,computerscore
    computerscore +=1
    changingtext.config(text="You lost, computer gets a point",fg="red")
    compscore.config(text="Computer's score: "+str(computerscore))
    youscore.config(text="Your score: "+str(playerscore))

def youwin():
    global playerscore,computerscore
    playerscore +=1
    changingtext.config(text="You won, you get a point",fg="green")
    compscore.config(text="Computer's score: "+str(computerscore))
    youscore.config(text="Your score: "+str(playerscore))

def youchoice(pc):
    global playerscore,computerscore
    cc = compchoice()
    yousel.config(text="Your selection: "+pc[0])
    
    

title = Label(screen,text="ROCK PAPER SCISSORS",font=("Comic Sans MS",30,"bold"),fg="purple")
title.pack(padx=10,pady=20)

changingtext = Label(screen,text="Let's start the game...",font=("Comic Sans MS",12),fg="green")
changingtext.pack()

frame = Frame(screen)
frame.pack()

options = Label(frame,text="Your Options:",font=("Comic Sans MS",12))
options.grid(row=0,column=0)

rock = Button(frame,text="ROCK",width=15,bg="gray")
rock.grid(row=0,column=1,padx=15,pady=10)
paper = Button(frame,text="PAPER",width=15,bg="beige")
paper.grid(row=0,column=2,padx=15,pady=10)
scissors = Button(frame,text="SCISSORS",width=15,bg="red")
scissors.grid(row=0,column=3,padx=15,pady=10)

score = Label(frame,text="Score:",font=("Comic Sans MS",12))
score.grid(row=1,column=0,pady=10)

yousel = Label(frame,text="Your selection: ---",font=("Comic Sans MS",12))
yousel.grid(row=1,column=1,pady=10,padx=15)

compsel = Label(frame,text="Computer's selection ---",font=("Comic Sans MS",12))
compsel.grid(row=1,column=2,pady=10,padx=15)

youscore = Label(frame,text="Your score: -",font=("Comic Sans MS",12))
youscore.grid(row=2,column=1,pady=10,padx=15)

compscore = Label(frame,text="Computer's score: -",font=("Comic Sans MS",12))
compscore.grid(row=2,column=2,pady=10,padx=15)

screen.geometry("700x300")
screen.mainloop()
