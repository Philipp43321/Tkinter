from tkinter import*
from tkinter.ttk import *
screen = Tk()
screen.title("multiplication table")
toptext = Label(screen,text="Multiplication Table")
toptext.grid(row=0,column=1,columnspan = 1,pady = 20)

numbers = IntVar()
dropdown = Combobox(screen,textvariable=numbers,width=10)
dropdown["values"] = tuple(range(101))
dropdown.grid(row = 1, column= 1)

NandR = Label(screen,text="Number and Range:")
NandR.grid(row=1,column=0)

def generator():
    tables = ""
    for i in range(buttonchoice.get()+1):
        tables+=str(numbers.get())+" X "+str(i)+" = "+str(numbers.get()*i)+"\n"
    table.configure(text=tables)

buttonchoice = IntVar()
b1 = Radiobutton(screen,text="10",variable=buttonchoice,value=10)
b2 = Radiobutton(screen,text="20",variable=buttonchoice,value=20)
b3 = Radiobutton(screen,text="30",variable=buttonchoice,value=30)
b1.grid(row=1,column=2)
b2.grid(row=2,column=2)
b3.grid(row=3,column=2)

table = Label(screen,anchor="center")
table.grid(row=5, column= 1)

generate = Button(screen,text="Generate",command=generator)
generate.grid(row = 4, column=1,pady =5)



screen.mainloop()