from tkinter import*
from tkinter.filedialog import *
screen = Tk()
frame = Frame(screen)
bframe = Frame(screen)
bframe.pack(side=TOP,anchor="w",padx=10,pady=5)
screen.title("Open/Delete file")
save = Button(bframe,text = "Save")
save.pack(side=LEFT,pady = 5)
entry = Entry(screen,width=10)
entry.pack(side=TOP,pady = 5)
add = Button(bframe,text = "Add")
add.pack(side=LEFT,pady = 5)
open = Button(bframe,text = "Open")
open.pack(side=LEFT,pady = 5)
delete = Button(bframe,text = "Delete")
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
