from tkinter import*
from tkinter.ttk import*
screen = Tk()
screen.title("menu")
menu1 = Menu(screen)
#adding file menu commands
file = Menu(menu1,tearoff=0)
menu1.add_cascade(label="file",menu=file)
file.add_command(label="New file",command=None)
file.add_command(label="Open file",command=None)
file.add_command(label="Save",command=None)
file.add_command(label="Save as",command=None)
file.add_separator()
file.add_command(label="Exit",command=None)

help = Menu(menu1,tearoff=0)
menu1.add_cascade(label="help",menu=help)
help.add_command(label="welcome",command=None)
help.add_command(label="youtube",command=None)
help.add_separator()
help.add_command(label="exit",command=None)
screen.config(menu=menu1)


mainloop()