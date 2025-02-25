from tkinter import*
screen = Tk()

screen.title = ("listbox")
listbox = Listbox(screen,height=10,width=15,bg="blue",activestyle='dotbox',font="arial",fg="light blue")
screen.geometry=("300x400")
label = Label(screen,text="fooditems")
listbox.insert(1,"chicken")
listbox.insert(2,"nuggets")
listbox.insert(3,"fries")
listbox.insert(4,"pizza")
listbox.insert(5,"popcorn")
listbox.insert(6,"chips")
label.pack()
listbox.pack()

screen.mainloop()
