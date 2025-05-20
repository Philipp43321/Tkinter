from tkinter import*
from tkinter.filedialog import *
screen = Tk()

#functions 

def funadd():
    listbox.insert(END,entry.get())
    entry.delete(0,END)

def deletefun():
    selection = listbox.curselection()
    listbox.delete(selection)

def savefun():
    file1 = asksaveasfile(defaultextension=".txt")
    if file1 is not None:
        for i in listbox.get(0,END):
            print(i.strip(),file=file1)
        listbox.delete(0,END)

def openfun():
    file2 = askopenfile(title="which file would you like to open?")
    if file2 is not None:
        listbox.delete(0,END)
        newfile = file2.readlines()
        for i in newfile:
            listbox.insert(END,i.strip())




frame = Frame(screen)
bframe = Frame(screen)
bframe.pack(side=TOP,anchor="w",padx=10,pady=5)
screen.title("Open/Delete file")
save = Button(bframe,text = "Save",command=savefun)
save.pack(side=LEFT,pady = 5)
entry = Entry(screen,width=10)
entry.pack(side=TOP,pady = 5)
add = Button(bframe,text = "Add",command=funadd)
add.pack(side=LEFT,pady = 5)
open = Button(bframe,text = "Open",command = openfun)
open.pack(side=LEFT,pady = 5)
delete = Button(bframe,text = "Delete",command=deletefun)
delete.pack(side=LEFT,pady = 5)


scrollbar = Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,width=50,yscrollcommand=scrollbar.set,bg="gray")
for i in range (100):
    listbox.insert(END,"file"+str(i))
listbox.pack(side=RIGHT,padx=5)
scrollbar.config(command=listbox.yview)
frame.pack(side=TOP)
screen.mainloop()
